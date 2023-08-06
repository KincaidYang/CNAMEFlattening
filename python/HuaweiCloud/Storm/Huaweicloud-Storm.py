import sys
import requests
import json
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkdns.v2.region.dns_region import DnsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkdns.v2 import *

# 配置参数
# 请根据实际情况替换以下参数
# 域名
domain = 'r2wind.cn'
# 子域名, 如果是@，代表解析根域名
subdomain = 'ipv6'
# CDN域名
CDNCNAME = 'resources.r2wind.cn.cdn.dnsv1.com.cn'
# AK/SK, 可以从 https://console.huaweicloud.com/iam/#/myCredential 获取
ak = 'ZF5U********6LDNRLS'
sk = 'PGDpq7zW7w********rMKX6VTeLZ'
# DoH服务器地址，可根据需要选择是否替换
DoH = 'https://dns.alidns.com/resolve'
# 记录类型，IPv4为A，IPv6为AAAA
record_type = 'AAAA'
# TTL，单位为秒
TTL = 120
# Region ID, 可以从 https://developer.huaweicloud.com/endpoint 获取, 例如cn-north-4
# 请注意请前往 https://console.huaweicloud.com/iam/ > 项目 中查看自己是否开通了对应的区域
regionid = 'cn-north-4'

if subdomain == '@':
    subdomain = ''
subdomains = subdomain if subdomain == '' else subdomain + '.'
FQDN = subdomains + domain + '.'

# DNS 服务器信息
DNS_SERVERS = {
    "Dianxin_Liaoning": "219.148.204.66",
    "Yidong_Liaoning": "211.137.32.178",
    "Liantong_Liaoning": "202.96.64.68",
    "Dianxin_Jilin": "219.149.194.55",
    "Yidong_Jilin": "211.141.16.99",
    "Liantong_Jilin": "202.98.0.68",
    "Dianxin_Heilongjiang": "112.100.100.100",
    "Yidong_Heilongjiang": "211.137.241.34",
    "Liantong_Heilongjiang": "202.97.224.68",
    "Dianxin_Beijing": "219.141.136.10",
    "Yidong_Beijing": "221.130.33.52",
    "Liantong_Beijing": "202.106.196.115",
    "Dianxin_Tianjin": "219.150.32.132",
    "Yidong_Tianjin": "211.137.160.5",
    "Liantong_Tianjin": "202.99.96.68",
    "Dianxin_Hebei": "222.222.222.222",
    "Yidong_Hebei": "211.138.13.66",
    "Liantong_Hebei": "202.99.160.68",
    "Dianxin_Shanxi": "219.149.135.188",
    "Yidong_Shanxi": "211.138.106.3",
    "Liantong_Shanxi": "202.99.216.113",
    "Dianxin_Neimenggu": "219.148.162.31",
    "Yidong_Neimenggu": "211.138.91.1",
    "Liantong_Neimenggu": "202.99.224.68",
    "Dianxin_Hainan": "202.100.192.68",
    "Yidong_Hainan": "221.176.88.95",
    "Liantong_Hainan": "221.11.132.2",
    "Dianxin_Guangdong": "202.96.134.133",
    "Yidong_Guangdong": "211.139.163.6",
    "Liantong_Guangdong": "210.21.196.6",
    "Dianxin_Guangxi": "202.103.225.68",
    "Yidong_Guangxi": "211.138.245.180",
    "Liantong_Guangxi": "221.7.128.68",
    "Dianxin_Fujian": "218.85.152.99",
    "Yidong_Fujian": "211.138.151.161",
    "Liantong_Fujian": "218.104.128.106",
    "Dianxin_Hunan": "222.246.129.80",
    "Yidong_Hunan": "211.142.210.98",
    "Liantong_Hunan": "58.20.127.238",
    "Dianxin_Hubei": "202.103.24.68",
    "Yidong_Hubei": "211.137.58.20",
    "Liantong_Hubei": "218.104.111.114",
    "Dianxin_Henan": "222.85.85.85",
    "Yidong_Henan": "211.138.24.71",
    "Liantong_Henan": "202.102.224.68",
    "Dianxin_Jiangxi": "202.101.224.69",
    "Yidong_Jiangxi": "211.141.90.68",
    "Liantong_Jiangxi": "220.248.192.12",
    "Dianxin_Shanghai": "202.96.209.133",
    "Yidong_Shanghai": "211.136.112.50",
    "Liantong_Shanghai": "210.22.70.3",
    "Dianxin_Jiangsu": "218.2.2.2",
    "Yidong_Jiangsu": "221.131.143.69",
    "Liantong_Jiangsu": "221.6.4.66",
    "Dianxin_Zhejiang": "202.101.172.35",
    "Yidong_Zhejiang": "211.140.13.188",
    "Liantong_Zhejiang": "221.12.1.227",
    "Dianxin_Anhui": "61.132.163.68",
    "Yidong_Anhui": "211.138.180.2",
    "Liantong_Anhui": "218.104.78.2",
    "Dianxin_Shandong": "219.146.1.66",
    "Yidong_Shandong": "218.201.96.130",
    "Liantong_Shandong": "202.102.128.68",
    "Dianxin_Chongqing": "61.128.192.68",
    "Yidong_Chongqing": "218.201.4.3",
    "Liantong_Chongqing": "221.5.203.98",
    "Dianxin_Sichuan": "61.139.2.69",
    "Yidong_Sichuan": "211.137.82.4",
    "Liantong_Sichuan": "119.6.6.6",
    "Dianxin_Guizhou": "202.98.192.67",
    "Yidong_Guizhou": "211.139.5.29",
    "Liantong_Guizhou": "221.13.28.234",
    "Dianxin_Yunnan": "222.172.200.68",
    "Yidong_Yunnan": "211.139.29.68",
    "Liantong_Yunnan": "221.3.131.11",
    "Dianxin_Xizang": "202.98.224.68",
    "Yidong_Xizang": "211.139.73.34",
    "Liantong_Xizang": "221.13.65.34",
    "Dianxin_Shaanxi": "218.30.19.40",
    "Yidong_Shaanxi": "211.137.130.3",
    "Liantong_Shaanxi": "221.11.1.67",
    "Dianxin_Gansu": "202.100.64.68",
    "Yidong_Gansu": "218.203.160.194",
    "Liantong_Gansu": "221.7.34.10",
    "Dianxin_Qinghai": "202.100.128.68",
    "Yidong_Qinghai": "211.138.75.123",
    "Liantong_Qinghai": "221.207.58.58",
    "Dianxin_Ningxia": "222.75.152.129",
    "Yidong_Ningxia": "218.203.123.116",
    "Liantong_Ningxia": "211.93.0.81",
    "Dianxin_Xinjiang": "61.128.114.166",
    "Yidong_Xinjiang": "218.202.152.130",
    "Liantong_Xinjiang": "221.7.1.21",
    "Jiaoyuwang": "202.112.144.30",
    "default_view": "202.96.209.133"
}

# 从 DOH 查询结果中提取 IP 地址
def extract_ip_from_doh_answer(answer):
    for record in answer:
        try:
            ipaddress.ip_address(record['data'])
            return record['data']
        except ValueError:
            continue
    return None

# 查询 DOH 接口获取 CDN 调度结果
def query_doh_cdn_result(session, dns_server):
    response = session.get(DoH, params={'name': CDNCNAME, 'type': record_type, 'edns_client_subnet': dns_server}, timeout=5)
    response_json = json.loads(response.text)
    return extract_ip_from_doh_answer(response_json['Answer'])

# 更新记录集
def update_record_sets(client, zone_id, line_id, recordset_id, cdn_result):
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = recordset_id
        listRecordsbody = [cdn_result]
        request.body = UpdateRecordSetsReq(records=listRecordsbody, ttl=TTL, type=record_type, name=FQDN)
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)

def process_dns_server(client, zone_id, line_id, dns_server):
    session = requests.Session()
    cdn_result = query_doh_cdn_result(session, dns_server)

    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = line_id
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_record_set_id = client.show_record_set_by_zone(request)
        print(resp_record_set_id)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)

    result_record_set_id = json.dumps(resp_record_set_id.to_json_object())
    result_record_set_id_json = json.loads(result_record_set_id)
    record_set_id = result_record_set_id_json['recordsets'][0]['id']
    print(record_set_id)

    update_record_sets(client, zone_id, line_id, record_set_id, cdn_result)


if __name__ == "__main__":
    credentials = BasicCredentials(ak, sk)
    client = DnsClient.new_builder().with_credentials(credentials).with_region(DnsRegion.value_of(regionid)).build()

    try:
        request = ListPublicZonesRequest()
        request.type = "public"
        request.name = domain
        resp_zone_id = client.list_public_zones(request)
        print(resp_zone_id)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)

    result_ZONE_ID = json.dumps(resp_zone_id.to_json_object())
    result_ZONE_ID_json = json.loads(result_ZONE_ID)
    zone_id = result_ZONE_ID_json['zones'][0]['id']

    with ThreadPoolExecutor() as executor:
        for line_id, dns_server in DNS_SERVERS.items():
            executor.submit(process_dns_server, client, zone_id, line_id, dns_server)