# 本脚本依赖于华为云Python SDK，使用前请完成安装pip3 install huaweicloudsdkdns
# 使用前请先参照说明使用模板导入记录
# coding=utf-8
import sys
import requests
import json
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkdns.v2.region.dns_region import DnsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkdns.v2 import *
# 配置参数
# domanin替换为自己的域名,如'example.com'或'example.cn'
domain=''
# sub_domain替换为自己的主机记录或域名前缀，如'www'或'dl'如果是根域名则写'@'或留空
subdomain=''
# CDNCNAME请替换为CDN提供的CNAME地址,如'r2wind.cn.cdn.qcloudcdn.cn'或'r2wind.cn.cdn.dnsv1.com'
CDNCNAME=''
# ak请替换为自己的华为云Access Key Id，可前往https://console.huaweicloud.com/iam/?locale=zh-cn#/mine/accessKey 获取
ak=''
# sk请替换为自己的华为云Secret Access Key，可前往https://console.huaweicloud.com/iam/?locale=zh-cn#/mine/accessKey 获取
sk=''
# URL为 DNSPod DOH接口地址，用以获取CDN实时解析情况，可自行替换（当前DNSPod DOH接口对IPv6返回存在问题，暂时替换为阿里）
DoH='https://dns.alidns.com/resolve'
# 记录类型("A"为IPv4，"AAAA"为IPv6)
record_type='AAAA'
# ttl为解析记录生存时间，单位为秒，可自行修改
TTL=120
# 使用各省运营商 DNSIP，以确保可以正常使用 ECS 协议调度
# 东北
DNS_LIAONING_CU='202.96.64.68'
DNS_LIAONING_CT='219.148.204.66'
DNS_LIAONING_CM='211.137.32.178'
DNS_JILIN_CU='202.98.0.68'
DNS_JILIN_CT='219.149.194.55'
DNS_JILIN_CM='211.141.16.99'
DNS_HEILONGJIANG_CU='202.97.224.68'
DNS_HEILONGJIANG_CT='112.100.100.100'
DNS_HEILONGJIANG_CM='211.137.241.34'
# 华北
DNS_BEIJING_CU='202.106.196.115'
DNS_BEIJING_CT='219.141.136.10'
DNS_BEIJING_CM='221.130.33.52'
DNS_TIANJIN_CU='202.99.96.68'
DNS_TIANJIN_CT='219.150.32.132'
DNS_TIANJIN_CM='211.137.160.5'
DNS_HEBEI_CU='202.99.160.68'
DNS_HEBEI_CT='222.222.222.222'
DNS_HEBEI_CM='211.138.13.66'
DNS_SHANXI_CU='202.99.216.113'
DNS_SHANXI_CT='219.149.135.188'
DNS_SHANXI_CM='211.138.106.3'
DNS_NEIMENGGU_CU='202.99.224.68'
DNS_NEIMENGGU_CT='219.148.162.31'
DNS_NEIMENGGU_CM='211.138.91.1'
# 华南
DNS_HAINAN_CU='221.11.132.2'
DNS_HAINAN_CT='202.100.192.68'
DNS_HAINAN_CM='221.176.88.95'
DNS_GUANGDONG_CU='210.21.196.6'
DNS_GUANGDONG_CT='202.96.134.133'
DNS_GUANGDONG_CM='211.139.163.6'
DNS_GUANGXI_CU='221.7.128.68'
DNS_GUANGXI_CT='202.103.225.68'
DNS_GUANGXI_CM='211.138.245.180'
DNS_Fujian_CU='218.104.128.106'
DNS_Fujian_CT='218.85.152.99'
DNS_Fujian_CM='211.138.151.161'
# 华中
DNS_HUNAN_CU='58.20.127.238'
DNS_HUNAN_CT='222.246.129.80'
DNS_HUNAN_CM='211.142.210.98'
DNS_HUBEI_CU='218.104.111.114'
DNS_HUBEI_CT='202.103.24.68'
DNS_HUBEI_CM='211.137.58.20'
DNS_HENAN_CU='202.102.224.68'
DNS_HENAN_CT='222.85.85.85'
DNS_HENAN_CM='211.138.24.71'
DNS_Jiangxi_CU='220.248.192.12'
DNS_Jiangxi_CT='202.101.224.69'
DNS_Jiangxi_CM='211.141.90.68'
# 华东
DNS_SHANGHAI_CU='210.22.70.3'
DNS_SHANGHAI_CT='202.96.209.133'
DNS_SHANGHAI_CM='211.136.112.50'
DNS_JIANGSU_CU='221.6.4.66'
DNS_JIANGSU_CT='218.2.2.2'
DNS_JIANGSU_CM='221.131.143.69'
DNS_ZHEJIANG_CU='221.12.1.227'
DNS_ZHEJIANG_CT='202.101.172.35'
DNS_ZHEJIANG_CM='211.140.13.188'
DNS_Anhui_CU='218.104.78.2'
DNS_Anhui_CT='61.132.163.68'
DNS_Anhui_CM='211.138.180.2'
DNS_SHANDONG_CU='202.102.128.68'
DNS_SHANDONG_CT='219.146.1.66'
DNS_SHANDONG_CM='218.201.96.130'
# 西南
DNS_CHONGQING_CU='221.5.203.98'
DNS_CHONGQING_CT='61.128.192.68'
DNS_CHONGQING_CM='218.201.4.3'
DNS_SICHUAN_CU='119.6.6.6'
DNS_SICHUAN_CT='61.139.2.69'
DNS_SICHUAN_CM='211.137.82.4'
DNS_GUIZHOU_CU='221.13.28.234'
DNS_GUIZHOU_CT='202.98.192.67'
DNS_GUIZHOU_CM='211.139.5.29'
DNS_YUNNAN_CU='221.3.131.11'
DNS_YUNNAN_CT='222.172.200.68'
DNS_YUNNAN_CM='211.139.29.68'
DNS_XIZANG_CU='221.13.65.34'
DNS_XIZANG_CT='202.98.224.68'
DNS_XIZANG_CM='211.139.73.34'
# 西北
DNS_SHAANXI_CU='221.11.1.67'
DNS_SHAANXI_CT='218.30.19.40'
DNS_SHAANXI_CM='211.137.130.3'
DNS_GANSU_CU='221.7.34.10'
DNS_GANSU_CT='202.100.64.68'
DNS_GANSU_CM='218.203.160.194'
DNS_QINGHAI_CU='221.207.58.58'
DNS_QINGHAI_CT='202.100.128.68'
DNS_QINGHAI_CM='211.138.75.123'
DNS_NINGXIA_CU='211.93.0.81'
DNS_NINGXIA_CT='222.75.152.129'
DNS_NINGXIA_CM='218.203.123.116'
DNS_XINJIANG_CU='221.7.1.21'
DNS_XINJIANG_CT='61.128.114.166'
DNS_XINJIANG_CM='218.202.152.130'
# 教育网（全国各地域都覆盖不太现实，选取北京交通大学 DNS 获取调度IP）
DNS_JIAOYU='202.112.144.30'
# 如果subdomain为@，则subdoamin重新赋值为空，否则subdoamin不变
if subdomain=='@':
    subdomain=''
else:
    subdomain=subdomain
# 如果subdoamin为空，则sbudomains=subdomain,否则subdomains=subdomain+'.'
if subdomain=='':
    subdomains=subdomain
else:
    subdomains=subdomain+'.'
FQDN=subdomains+domain+'.'
print(FQDN)
# 获取 zone_id
if __name__ == "__main__":
    credentials = BasicCredentials(ak, sk) \

    client = DnsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(DnsRegion.value_of("cn-east-2")) \
        .build()

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
    # 获取 CDN 调度结果并将调度结果推送到 Huawei
    # 华北
    # 北京
    # 北京电信
    # 获取北京电信调度结果
    Dianxin_Beijing_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_BEIJING_CT})
    print(Dianxin_Beijing_CDN.text)
    Dianxin_Beijing_CDN_json = json.loads(Dianxin_Beijing_CDN.text)
    Dianxin_Beijing_CDN_result1 = Dianxin_Beijing_CDN_json['Answer'][1]['data']
    Dianxin_Beijing_CDN_result2 = Dianxin_Beijing_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Beijing"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Beijing_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Beijing_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Beijing_CT_RecordSetId=json.dumps(resp_Beijing_CT_RecordSetId.to_json_object())
    result_Beijing_CT_RecordSetId_json=json.loads(result_Beijing_CT_RecordSetId)
    Beijing_CT_RecordSetId=result_Beijing_CT_RecordSetId_json['recordsets'][0]['id']
    print(Beijing_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Beijing_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Beijing_CDN_result1,
            Dianxin_Beijing_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 北京移动
    # 获取北京移动调度结果
    Yidong_Beijing_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_BEIJING_CM})
    print(Yidong_Beijing_CDN.text)
    Yidong_Beijing_CDN_json = json.loads(Yidong_Beijing_CDN.text)
    Yidong_Beijing_CDN_result1 = Yidong_Beijing_CDN_json['Answer'][1]['data']
    Yidong_Beijing_CDN_result2 = Yidong_Beijing_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Beijing"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Beijing_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Beijing_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Beijing_CM_RecordSetId=json.dumps(resp_Beijing_CM_RecordSetId.to_json_object())
    result_Beijing_CM_RecordSetId_json=json.loads(result_Beijing_CM_RecordSetId)
    Beijing_CM_RecordSetId=result_Beijing_CM_RecordSetId_json['recordsets'][0]['id']
    print(Beijing_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Beijing_CM_RecordSetId
        listRecordsbody = [
            Yidong_Beijing_CDN_result1,
            Yidong_Beijing_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 北京联通
    # 获取北京联通调度结果
    Liantong_Beijing_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_BEIJING_CU})
    print(Liantong_Beijing_CDN.text)
    Liantong_Beijing_CDN_json = json.loads(Liantong_Beijing_CDN.text)
    Liantong_Beijing_CDN_result1 = Liantong_Beijing_CDN_json['Answer'][1]['data']
    Liantong_Beijing_CDN_result2 = Liantong_Beijing_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Beijing"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Beijing_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Beijing_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Beijing_CU_RecordSetId=json.dumps(resp_Beijing_CU_RecordSetId.to_json_object())
    result_Beijing_CU_RecordSetId_json=json.loads(result_Beijing_CU_RecordSetId)
    Beijing_CU_RecordSetId=result_Beijing_CU_RecordSetId_json['recordsets'][0]['id']
    print(Beijing_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Beijing_CU_RecordSetId
        listRecordsbody = [
            Liantong_Beijing_CDN_result1,
            Liantong_Beijing_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 天津
    # 天津电信
    # 获取天津电信调度结果
    Dianxin_Tianjin_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_TIANJIN_CT})
    print(Dianxin_Tianjin_CDN.text)
    Dianxin_Tianjin_CDN_json = json.loads(Dianxin_Tianjin_CDN.text)
    Dianxin_Tianjin_CDN_result1 = Dianxin_Tianjin_CDN_json['Answer'][1]['data']
    Dianxin_Tianjin_CDN_result2 = Dianxin_Tianjin_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Tianjin"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Tianjin_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Tianjin_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Tianjin_CT_RecordSetId=json.dumps(resp_Tianjin_CT_RecordSetId.to_json_object())
    result_Tianjin_CT_RecordSetId_json=json.loads(result_Tianjin_CT_RecordSetId)
    Tianjin_CT_RecordSetId=result_Tianjin_CT_RecordSetId_json['recordsets'][0]['id']
    print(Tianjin_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Tianjin_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Tianjin_CDN_result1,
            Dianxin_Tianjin_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 天津移动
    # 获取天津移动调度结果
    Yidong_Tianjin_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_TIANJIN_CM})
    print(Yidong_Tianjin_CDN.text)
    Yidong_Tianjin_CDN_json = json.loads(Yidong_Tianjin_CDN.text)
    Yidong_Tianjin_CDN_result1 = Yidong_Tianjin_CDN_json['Answer'][1]['data']
    Yidong_Tianjin_CDN_result2 = Yidong_Tianjin_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Tianjin"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Tianjin_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Tianjin_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Tianjin_CM_RecordSetId=json.dumps(resp_Tianjin_CM_RecordSetId.to_json_object())
    result_Tianjin_CM_RecordSetId_json=json.loads(result_Tianjin_CM_RecordSetId)
    Tianjin_CM_RecordSetId=result_Tianjin_CM_RecordSetId_json['recordsets'][0]['id']
    print(Tianjin_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Tianjin_CM_RecordSetId
        listRecordsbody = [
            Yidong_Tianjin_CDN_result1,
            Yidong_Tianjin_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 天津联通
    # 获取天津联通调度结果
    Liantong_Tianjin_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_TIANJIN_CU})
    print(Liantong_Tianjin_CDN.text)
    Liantong_Tianjin_CDN_json = json.loads(Liantong_Tianjin_CDN.text)
    Liantong_Tianjin_CDN_result1 = Liantong_Tianjin_CDN_json['Answer'][1]['data']
    Liantong_Tianjin_CDN_result2 = Liantong_Tianjin_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Tianjin"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Tianjin_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Tianjin_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Tianjin_CU_RecordSetId=json.dumps(resp_Tianjin_CU_RecordSetId.to_json_object())
    result_Tianjin_CU_RecordSetId_json=json.loads(result_Tianjin_CU_RecordSetId)
    Tianjin_CU_RecordSetId=result_Tianjin_CU_RecordSetId_json['recordsets'][0]['id']
    print(Tianjin_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Tianjin_CU_RecordSetId
        listRecordsbody = [
            Liantong_Tianjin_CDN_result1,
            Liantong_Tianjin_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 河北
    # 河北电信
    # 获取河北电信调度结果
    Dianxin_Hebei_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HEBEI_CT})
    print(Dianxin_Hebei_CDN.text)
    Dianxin_Hebei_CDN_json = json.loads(Dianxin_Hebei_CDN.text)
    Dianxin_Hebei_CDN_result1 = Dianxin_Hebei_CDN_json['Answer'][1]['data']
    Dianxin_Hebei_CDN_result2 = Dianxin_Hebei_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Hebei"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hebei_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hebei_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hebei_CT_RecordSetId=json.dumps(resp_Hebei_CT_RecordSetId.to_json_object())
    result_Hebei_CT_RecordSetId_json=json.loads(result_Hebei_CT_RecordSetId)
    Hebei_CT_RecordSetId=result_Hebei_CT_RecordSetId_json['recordsets'][0]['id']
    print(Hebei_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hebei_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Hebei_CDN_result1,
            Dianxin_Hebei_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 河北移动
    # 获取河北移动调度结果
    Yidong_Hebei_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HEBEI_CM})
    print(Yidong_Hebei_CDN.text)
    Yidong_Hebei_CDN_json = json.loads(Yidong_Hebei_CDN.text)
    Yidong_Hebei_CDN_result1 = Yidong_Hebei_CDN_json['Answer'][1]['data']
    Yidong_Hebei_CDN_result2 = Yidong_Hebei_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Hebei"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hebei_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hebei_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hebei_CM_RecordSetId=json.dumps(resp_Hebei_CM_RecordSetId.to_json_object())
    result_Hebei_CM_RecordSetId_json=json.loads(result_Hebei_CM_RecordSetId)
    Hebei_CM_RecordSetId=result_Hebei_CM_RecordSetId_json['recordsets'][0]['id']
    print(Hebei_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hebei_CM_RecordSetId
        listRecordsbody = [
            Yidong_Hebei_CDN_result1,
            Yidong_Hebei_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 河北联通
    # 获取河北联通调度结果
    Liantong_Hebei_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HEBEI_CU})
    print(Liantong_Hebei_CDN.text)
    Liantong_Hebei_CDN_json = json.loads(Liantong_Hebei_CDN.text)
    Liantong_Hebei_CDN_result1 = Liantong_Hebei_CDN_json['Answer'][1]['data']
    Liantong_Hebei_CDN_result2 = Liantong_Hebei_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Hebei"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hebei_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hebei_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hebei_CU_RecordSetId=json.dumps(resp_Hebei_CU_RecordSetId.to_json_object())
    result_Hebei_CU_RecordSetId_json=json.loads(result_Hebei_CU_RecordSetId)
    Hebei_CU_RecordSetId=result_Hebei_CU_RecordSetId_json['recordsets'][0]['id']
    print(Hebei_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hebei_CU_RecordSetId
        listRecordsbody = [
            Liantong_Hebei_CDN_result1,
            Liantong_Hebei_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 山西
    # 山西电信
    # 获取山西电信调度结果
    Dianxin_Shanxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHANXI_CT})
    print(Dianxin_Shanxi_CDN.text)
    Dianxin_Shanxi_CDN_json = json.loads(Dianxin_Shanxi_CDN.text)
    Dianxin_Shanxi_CDN_result1 = Dianxin_Shanxi_CDN_json['Answer'][1]['data']
    Dianxin_Shanxi_CDN_result2 = Dianxin_Shanxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Shanxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shanxi_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shanxi_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shanxi_CT_RecordSetId=json.dumps(resp_Shanxi_CT_RecordSetId.to_json_object())
    result_Shanxi_CT_RecordSetId_json=json.loads(result_Shanxi_CT_RecordSetId)
    Shanxi_CT_RecordSetId=result_Shanxi_CT_RecordSetId_json['recordsets'][0]['id']
    print(Shanxi_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shanxi_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Shanxi_CDN_result1,
            Dianxin_Shanxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 山西移动
    # 获取山西移动调度结果
    Yidong_Shanxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHANXI_CM})
    print(Yidong_Shanxi_CDN.text)
    Yidong_Shanxi_CDN_json = json.loads(Yidong_Shanxi_CDN.text)
    Yidong_Shanxi_CDN_result1 = Yidong_Shanxi_CDN_json['Answer'][1]['data']
    Yidong_Shanxi_CDN_result2 = Yidong_Shanxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Shanxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shanxi_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shanxi_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shanxi_CM_RecordSetId=json.dumps(resp_Shanxi_CM_RecordSetId.to_json_object())
    result_Shanxi_CM_RecordSetId_json=json.loads(result_Shanxi_CM_RecordSetId)
    Shanxi_CM_RecordSetId=result_Shanxi_CM_RecordSetId_json['recordsets'][0]['id']
    print(Shanxi_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shanxi_CM_RecordSetId
        listRecordsbody = [
            Yidong_Shanxi_CDN_result1,
            Yidong_Shanxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 山西联通
    # 获取山西联通调度结果
    Liantong_Shanxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHANXI_CU})
    print(Liantong_Shanxi_CDN.text)
    Liantong_Shanxi_CDN_json = json.loads(Liantong_Shanxi_CDN.text)
    Liantong_Shanxi_CDN_result1 = Liantong_Shanxi_CDN_json['Answer'][1]['data']
    Liantong_Shanxi_CDN_result2 = Liantong_Shanxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Shanxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shanxi_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shanxi_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shanxi_CU_RecordSetId=json.dumps(resp_Shanxi_CU_RecordSetId.to_json_object())
    result_Shanxi_CU_RecordSetId_json=json.loads(result_Shanxi_CU_RecordSetId)
    Shanxi_CU_RecordSetId=result_Shanxi_CU_RecordSetId_json['recordsets'][0]['id']
    print(Shanxi_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shanxi_CU_RecordSetId
        listRecordsbody = [
            Liantong_Shanxi_CDN_result1,
            Liantong_Shanxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 内蒙古
    # 内蒙古电信
    # 获取内蒙古电信调度结果
    Dianxin_Neimenggu_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_NEIMENGGU_CT})
    print(Dianxin_Neimenggu_CDN.text)
    Dianxin_Neimenggu_CDN_json = json.loads(Dianxin_Neimenggu_CDN.text)
    Dianxin_Neimenggu_CDN_result1 = Dianxin_Neimenggu_CDN_json['Answer'][1]['data']
    Dianxin_Neimenggu_CDN_result2 = Dianxin_Neimenggu_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Neimenggu"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Neimenggu_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Neimenggu_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Neimenggu_CT_RecordSetId=json.dumps(resp_Neimenggu_CT_RecordSetId.to_json_object())
    result_Neimenggu_CT_RecordSetId_json=json.loads(result_Neimenggu_CT_RecordSetId)
    Neimenggu_CT_RecordSetId=result_Neimenggu_CT_RecordSetId_json['recordsets'][0]['id']
    print(Neimenggu_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Neimenggu_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Neimenggu_CDN_result1,
            Dianxin_Neimenggu_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 内蒙古移动
    # 获取内蒙古移动调度结果
    Yidong_Neimenggu_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_NEIMENGGU_CM})
    print(Yidong_Neimenggu_CDN.text)
    Yidong_Neimenggu_CDN_json = json.loads(Yidong_Neimenggu_CDN.text)
    Yidong_Neimenggu_CDN_result1 = Yidong_Neimenggu_CDN_json['Answer'][1]['data']
    Yidong_Neimenggu_CDN_result2 = Yidong_Neimenggu_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Neimenggu"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Neimenggu_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Neimenggu_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Neimenggu_CM_RecordSetId=json.dumps(resp_Neimenggu_CM_RecordSetId.to_json_object())
    result_Neimenggu_CM_RecordSetId_json=json.loads(result_Neimenggu_CM_RecordSetId)
    Neimenggu_CM_RecordSetId=result_Neimenggu_CM_RecordSetId_json['recordsets'][0]['id']
    print(Neimenggu_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Neimenggu_CM_RecordSetId
        listRecordsbody = [
            Yidong_Neimenggu_CDN_result1,
            Yidong_Neimenggu_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 内蒙古联通
    # 获取内蒙古联通调度结果
    Liantong_Neimenggu_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_NEIMENGGU_CU})
    print(Liantong_Neimenggu_CDN.text)
    Liantong_Neimenggu_CDN_json = json.loads(Liantong_Neimenggu_CDN.text)
    Liantong_Neimenggu_CDN_result1 = Liantong_Neimenggu_CDN_json['Answer'][1]['data']
    Liantong_Neimenggu_CDN_result2 = Liantong_Neimenggu_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Neimenggu"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Neimenggu_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Neimenggu_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Neimenggu_CU_RecordSetId=json.dumps(resp_Neimenggu_CU_RecordSetId.to_json_object())
    result_Neimenggu_CU_RecordSetId_json=json.loads(result_Neimenggu_CU_RecordSetId)
    Neimenggu_CU_RecordSetId=result_Neimenggu_CU_RecordSetId_json['recordsets'][0]['id']
    print(Neimenggu_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Neimenggu_CU_RecordSetId
        listRecordsbody = [
            Liantong_Neimenggu_CDN_result1,
            Liantong_Neimenggu_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 辽宁
    # 辽宁电信
    # 获取辽宁电信调度结果
    Dianxin_Liaoning_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_LIAONING_CT})
    print(Dianxin_Liaoning_CDN.text)
    Dianxin_Liaoning_CDN_json = json.loads(Dianxin_Liaoning_CDN.text)
    Dianxin_Liaoning_CDN_result1 = Dianxin_Liaoning_CDN_json['Answer'][1]['data']
    Dianxin_Liaoning_CDN_result2 = Dianxin_Liaoning_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Liaoning"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Liaoning_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Liaoning_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Liaoning_CT_RecordSetId=json.dumps(resp_Liaoning_CT_RecordSetId.to_json_object())
    result_Liaoning_CT_RecordSetId_json=json.loads(result_Liaoning_CT_RecordSetId)
    Liaoning_CT_RecordSetId=result_Liaoning_CT_RecordSetId_json['recordsets'][0]['id']
    print(Liaoning_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Liaoning_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Liaoning_CDN_result1,
            Dianxin_Liaoning_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 辽宁移动
    # 获取辽宁移动调度结果
    Yidong_Liaoning_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_LIAONING_CM})
    print(Yidong_Liaoning_CDN.text)
    Yidong_Liaoning_CDN_json = json.loads(Yidong_Liaoning_CDN.text)
    Yidong_Liaoning_CDN_result1 = Yidong_Liaoning_CDN_json['Answer'][1]['data']
    Yidong_Liaoning_CDN_result2 = Yidong_Liaoning_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Liaoning"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Liaoning_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Liaoning_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Liaoning_CM_RecordSetId=json.dumps(resp_Liaoning_CM_RecordSetId.to_json_object())
    result_Liaoning_CM_RecordSetId_json=json.loads(result_Liaoning_CM_RecordSetId)
    Liaoning_CM_RecordSetId=result_Liaoning_CM_RecordSetId_json['recordsets'][0]['id']
    print(Liaoning_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Liaoning_CM_RecordSetId
        listRecordsbody = [
            Yidong_Liaoning_CDN_result1,
            Yidong_Liaoning_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 辽宁联通
    # 获取辽宁联通调度结果
    Liantong_Liaoning_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_LIAONING_CU})
    print(Liantong_Liaoning_CDN.text)
    Liantong_Liaoning_CDN_json = json.loads(Liantong_Liaoning_CDN.text)
    Liantong_Liaoning_CDN_result1 = Liantong_Liaoning_CDN_json['Answer'][1]['data']
    Liantong_Liaoning_CDN_result2 = Liantong_Liaoning_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Liaoning"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Liaoning_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Liaoning_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Liaoning_CU_RecordSetId=json.dumps(resp_Liaoning_CU_RecordSetId.to_json_object())
    result_Liaoning_CU_RecordSetId_json=json.loads(result_Liaoning_CU_RecordSetId)
    Liaoning_CU_RecordSetId=result_Liaoning_CU_RecordSetId_json['recordsets'][0]['id']
    print(Liaoning_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Liaoning_CU_RecordSetId
        listRecordsbody = [
            Liantong_Liaoning_CDN_result1,
            Liantong_Liaoning_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 吉林
    # 吉林电信
    # 获取吉林电信调度结果
    Dianxin_Jilin_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_JILIN_CT})
    print(Dianxin_Jilin_CDN.text)
    Dianxin_Jilin_CDN_json = json.loads(Dianxin_Jilin_CDN.text)
    Dianxin_Jilin_CDN_result1 = Dianxin_Jilin_CDN_json['Answer'][1]['data']
    Dianxin_Jilin_CDN_result2 = Dianxin_Jilin_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Jilin"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Jilin_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Jilin_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Jilin_CT_RecordSetId=json.dumps(resp_Jilin_CT_RecordSetId.to_json_object())
    result_Jilin_CT_RecordSetId_json=json.loads(result_Jilin_CT_RecordSetId)
    Jilin_CT_RecordSetId=result_Jilin_CT_RecordSetId_json['recordsets'][0]['id']
    print(Jilin_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Jilin_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Jilin_CDN_result1,
            Dianxin_Jilin_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 吉林移动
    # 获取吉林移动调度结果
    Yidong_Jilin_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_JILIN_CM})
    print(Yidong_Jilin_CDN.text)
    Yidong_Jilin_CDN_json = json.loads(Yidong_Jilin_CDN.text)
    Yidong_Jilin_CDN_result1 = Yidong_Jilin_CDN_json['Answer'][1]['data']
    Yidong_Jilin_CDN_result2 = Yidong_Jilin_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Jilin"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Jilin_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Jilin_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Jilin_CM_RecordSetId=json.dumps(resp_Jilin_CM_RecordSetId.to_json_object())
    result_Jilin_CM_RecordSetId_json=json.loads(result_Jilin_CM_RecordSetId)
    Jilin_CM_RecordSetId=result_Jilin_CM_RecordSetId_json['recordsets'][0]['id']
    print(Jilin_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Jilin_CM_RecordSetId
        listRecordsbody = [
            Yidong_Jilin_CDN_result1,
            Yidong_Jilin_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 吉林联通
    # 获取吉林联通调度结果
    Liantong_Jilin_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_JILIN_CU})
    print(Liantong_Jilin_CDN.text)
    Liantong_Jilin_CDN_json = json.loads(Liantong_Jilin_CDN.text)
    Liantong_Jilin_CDN_result1 = Liantong_Jilin_CDN_json['Answer'][1]['data']
    Liantong_Jilin_CDN_result2 = Liantong_Jilin_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Jilin"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Jilin_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Jilin_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Jilin_CU_RecordSetId=json.dumps(resp_Jilin_CU_RecordSetId.to_json_object())
    result_Jilin_CU_RecordSetId_json=json.loads(result_Jilin_CU_RecordSetId)
    Jilin_CU_RecordSetId=result_Jilin_CU_RecordSetId_json['recordsets'][0]['id']
    print(Jilin_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Jilin_CU_RecordSetId
        listRecordsbody = [
            Liantong_Jilin_CDN_result1,
            Liantong_Jilin_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 黑龙江
    # 黑龙江电信
    # 获取黑龙江电信调度结果
    Dianxin_Heilongjiang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HEILONGJIANG_CT})
    print(Dianxin_Heilongjiang_CDN.text)
    Dianxin_Heilongjiang_CDN_json = json.loads(Dianxin_Heilongjiang_CDN.text)
    Dianxin_Heilongjiang_CDN_result1 = Dianxin_Heilongjiang_CDN_json['Answer'][1]['data']
    Dianxin_Heilongjiang_CDN_result2 = Dianxin_Heilongjiang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Heilongjiang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Heilongjiang_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Heilongjiang_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Heilongjiang_CT_RecordSetId=json.dumps(resp_Heilongjiang_CT_RecordSetId.to_json_object())
    result_Heilongjiang_CT_RecordSetId_json=json.loads(result_Heilongjiang_CT_RecordSetId)
    Heilongjiang_CT_RecordSetId=result_Heilongjiang_CT_RecordSetId_json['recordsets'][0]['id']
    print(Heilongjiang_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Heilongjiang_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Heilongjiang_CDN_result1,
            Dianxin_Heilongjiang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 黑龙江移动
    # 获取黑龙江移动调度结果
    Yidong_Heilongjiang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HEILONGJIANG_CM})
    print(Yidong_Heilongjiang_CDN.text)
    Yidong_Heilongjiang_CDN_json = json.loads(Yidong_Heilongjiang_CDN.text)
    Yidong_Heilongjiang_CDN_result1 = Yidong_Heilongjiang_CDN_json['Answer'][1]['data']
    Yidong_Heilongjiang_CDN_result2 = Yidong_Heilongjiang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Heilongjiang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Heilongjiang_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Heilongjiang_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Heilongjiang_CM_RecordSetId=json.dumps(resp_Heilongjiang_CM_RecordSetId.to_json_object())
    result_Heilongjiang_CM_RecordSetId_json=json.loads(result_Heilongjiang_CM_RecordSetId)
    Heilongjiang_CM_RecordSetId=result_Heilongjiang_CM_RecordSetId_json['recordsets'][0]['id']
    print(Heilongjiang_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Heilongjiang_CM_RecordSetId
        listRecordsbody = [
            Yidong_Heilongjiang_CDN_result1,
            Yidong_Heilongjiang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 黑龙江联通
    # 获取黑龙江联通调度结果
    Liantong_Heilongjiang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HEILONGJIANG_CU})
    print(Liantong_Heilongjiang_CDN.text)
    Liantong_Heilongjiang_CDN_json = json.loads(Liantong_Heilongjiang_CDN.text)
    Liantong_Heilongjiang_CDN_result1 = Liantong_Heilongjiang_CDN_json['Answer'][1]['data']
    Liantong_Heilongjiang_CDN_result2 = Liantong_Heilongjiang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Heilongjiang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Heilongjiang_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Heilongjiang_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Heilongjiang_CU_RecordSetId=json.dumps(resp_Heilongjiang_CU_RecordSetId.to_json_object())
    result_Heilongjiang_CU_RecordSetId_json=json.loads(result_Heilongjiang_CU_RecordSetId)
    Heilongjiang_CU_RecordSetId=result_Heilongjiang_CU_RecordSetId_json['recordsets'][0]['id']
    print(Heilongjiang_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Heilongjiang_CU_RecordSetId
        listRecordsbody = [
            Liantong_Heilongjiang_CDN_result1,
            Liantong_Heilongjiang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 陕西
    # 陕西电信
    # 获取陕西电信调度结果
    Dianxin_Shaanxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHAANXI_CT})
    print(Dianxin_Shaanxi_CDN.text)
    Dianxin_Shaanxi_CDN_json = json.loads(Dianxin_Shaanxi_CDN.text)
    Dianxin_Shaanxi_CDN_result1 = Dianxin_Shaanxi_CDN_json['Answer'][1]['data']
    Dianxin_Shaanxi_CDN_result2 = Dianxin_Shaanxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Shaanxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shaanxi_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shaanxi_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shaanxi_CT_RecordSetId=json.dumps(resp_Shaanxi_CT_RecordSetId.to_json_object())
    result_Shaanxi_CT_RecordSetId_json=json.loads(result_Shaanxi_CT_RecordSetId)
    Shaanxi_CT_RecordSetId=result_Shaanxi_CT_RecordSetId_json['recordsets'][0]['id']
    print(Shaanxi_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shaanxi_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Shaanxi_CDN_result1,
            Dianxin_Shaanxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 陕西移动
    # 获取陕西移动调度结果
    Yidong_Shaanxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHAANXI_CM})
    print(Yidong_Shaanxi_CDN.text)
    Yidong_Shaanxi_CDN_json = json.loads(Yidong_Shaanxi_CDN.text)
    Yidong_Shaanxi_CDN_result1 = Yidong_Shaanxi_CDN_json['Answer'][1]['data']
    Yidong_Shaanxi_CDN_result2 = Yidong_Shaanxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Shaanxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shaanxi_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shaanxi_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shaanxi_CM_RecordSetId=json.dumps(resp_Shaanxi_CM_RecordSetId.to_json_object())
    result_Shaanxi_CM_RecordSetId_json=json.loads(result_Shaanxi_CM_RecordSetId)
    Shaanxi_CM_RecordSetId=result_Shaanxi_CM_RecordSetId_json['recordsets'][0]['id']
    print(Shaanxi_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shaanxi_CM_RecordSetId
        listRecordsbody = [
            Yidong_Shaanxi_CDN_result1,
            Yidong_Shaanxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 陕西联通
    # 获取陕西联通调度结果
    Liantong_Shaanxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHAANXI_CU})
    print(Liantong_Shaanxi_CDN.text)
    Liantong_Shaanxi_CDN_json = json.loads(Liantong_Shaanxi_CDN.text)
    Liantong_Shaanxi_CDN_result1 = Liantong_Shaanxi_CDN_json['Answer'][1]['data']
    Liantong_Shaanxi_CDN_result2 = Liantong_Shaanxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Shaanxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shaanxi_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shaanxi_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shaanxi_CU_RecordSetId=json.dumps(resp_Shaanxi_CU_RecordSetId.to_json_object())
    result_Shaanxi_CU_RecordSetId_json=json.loads(result_Shaanxi_CU_RecordSetId)
    Shaanxi_CU_RecordSetId=result_Shaanxi_CU_RecordSetId_json['recordsets'][0]['id']
    print(Shaanxi_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shaanxi_CU_RecordSetId
        listRecordsbody = [
            Liantong_Shaanxi_CDN_result1,
            Liantong_Shaanxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 甘肃
    # 甘肃电信
    # 获取甘肃电信调度结果
    Dianxin_Gansu_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GANSU_CT})
    print(Dianxin_Gansu_CDN.text)
    Dianxin_Gansu_CDN_json = json.loads(Dianxin_Gansu_CDN.text)
    Dianxin_Gansu_CDN_result1 = Dianxin_Gansu_CDN_json['Answer'][1]['data']
    Dianxin_Gansu_CDN_result2 = Dianxin_Gansu_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Gansu"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Gansu_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Gansu_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Gansu_CT_RecordSetId=json.dumps(resp_Gansu_CT_RecordSetId.to_json_object())
    result_Gansu_CT_RecordSetId_json=json.loads(result_Gansu_CT_RecordSetId)
    Gansu_CT_RecordSetId=result_Gansu_CT_RecordSetId_json['recordsets'][0]['id']
    print(Gansu_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Gansu_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Gansu_CDN_result1,
            Dianxin_Gansu_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 甘肃移动
    # 获取甘肃移动调度结果
    Yidong_Gansu_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GANSU_CM})
    print(Yidong_Gansu_CDN.text)
    Yidong_Gansu_CDN_json = json.loads(Yidong_Gansu_CDN.text)
    Yidong_Gansu_CDN_result1 = Yidong_Gansu_CDN_json['Answer'][1]['data']
    Yidong_Gansu_CDN_result2 = Yidong_Gansu_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Gansu"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Gansu_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Gansu_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Gansu_CM_RecordSetId=json.dumps(resp_Gansu_CM_RecordSetId.to_json_object())
    result_Gansu_CM_RecordSetId_json=json.loads(result_Gansu_CM_RecordSetId)
    Gansu_CM_RecordSetId=result_Gansu_CM_RecordSetId_json['recordsets'][0]['id']
    print(Gansu_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Gansu_CM_RecordSetId
        listRecordsbody = [
            Yidong_Gansu_CDN_result1,
            Yidong_Gansu_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 甘肃联通
    # 获取甘肃联通调度结果
    Liantong_Gansu_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GANSU_CU})
    print(Liantong_Gansu_CDN.text)
    Liantong_Gansu_CDN_json = json.loads(Liantong_Gansu_CDN.text)
    Liantong_Gansu_CDN_result1 = Liantong_Gansu_CDN_json['Answer'][1]['data']
    Liantong_Gansu_CDN_result2 = Liantong_Gansu_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Gansu"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Gansu_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Gansu_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Gansu_CU_RecordSetId=json.dumps(resp_Gansu_CU_RecordSetId.to_json_object())
    result_Gansu_CU_RecordSetId_json=json.loads(result_Gansu_CU_RecordSetId)
    Gansu_CU_RecordSetId=result_Gansu_CU_RecordSetId_json['recordsets'][0]['id']
    print(Gansu_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Gansu_CU_RecordSetId
        listRecordsbody = [
            Liantong_Gansu_CDN_result1,
            Liantong_Gansu_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 青海
    # 青海电信
    # 获取青海电信调度结果
    Dianxin_Qinghai_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_QINGHAI_CT})
    print(Dianxin_Qinghai_CDN.text)
    Dianxin_Qinghai_CDN_json = json.loads(Dianxin_Qinghai_CDN.text)
    Dianxin_Qinghai_CDN_result1 = Dianxin_Qinghai_CDN_json['Answer'][1]['data']
    Dianxin_Qinghai_CDN_result2 = Dianxin_Qinghai_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Qinghai"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Qinghai_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Qinghai_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Qinghai_CT_RecordSetId=json.dumps(resp_Qinghai_CT_RecordSetId.to_json_object())
    result_Qinghai_CT_RecordSetId_json=json.loads(result_Qinghai_CT_RecordSetId)
    Qinghai_CT_RecordSetId=result_Qinghai_CT_RecordSetId_json['recordsets'][0]['id']
    print(Qinghai_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Qinghai_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Qinghai_CDN_result1,
            Dianxin_Qinghai_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 青海移动
    # 获取青海移动调度结果
    Yidong_Qinghai_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_QINGHAI_CM})
    print(Yidong_Qinghai_CDN.text)
    Yidong_Qinghai_CDN_json = json.loads(Yidong_Qinghai_CDN.text)
    Yidong_Qinghai_CDN_result1 = Yidong_Qinghai_CDN_json['Answer'][1]['data']
    Yidong_Qinghai_CDN_result2 = Yidong_Qinghai_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Qinghai"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Qinghai_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Qinghai_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Qinghai_CM_RecordSetId=json.dumps(resp_Qinghai_CM_RecordSetId.to_json_object())
    result_Qinghai_CM_RecordSetId_json=json.loads(result_Qinghai_CM_RecordSetId)
    Qinghai_CM_RecordSetId=result_Qinghai_CM_RecordSetId_json['recordsets'][0]['id']
    print(Qinghai_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Qinghai_CM_RecordSetId
        listRecordsbody = [
            Yidong_Qinghai_CDN_result1,
            Yidong_Qinghai_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 青海联通
    # 获取青海联通调度结果
    Liantong_Qinghai_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_QINGHAI_CU})
    print(Liantong_Qinghai_CDN.text)
    Liantong_Qinghai_CDN_json = json.loads(Liantong_Qinghai_CDN.text)
    Liantong_Qinghai_CDN_result1 = Liantong_Qinghai_CDN_json['Answer'][1]['data']
    Liantong_Qinghai_CDN_result2 = Liantong_Qinghai_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Qinghai"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Qinghai_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Qinghai_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Qinghai_CU_RecordSetId=json.dumps(resp_Qinghai_CU_RecordSetId.to_json_object())
    result_Qinghai_CU_RecordSetId_json=json.loads(result_Qinghai_CU_RecordSetId)
    Qinghai_CU_RecordSetId=result_Qinghai_CU_RecordSetId_json['recordsets'][0]['id']
    print(Qinghai_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Qinghai_CU_RecordSetId
        listRecordsbody = [
            Liantong_Qinghai_CDN_result1,
            Liantong_Qinghai_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 宁夏
    # 宁夏电信
    # 获取宁夏电信调度结果
    Dianxin_Ningxia_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_NINGXIA_CT})
    print(Dianxin_Ningxia_CDN.text)
    Dianxin_Ningxia_CDN_json = json.loads(Dianxin_Ningxia_CDN.text)
    Dianxin_Ningxia_CDN_result1 = Dianxin_Ningxia_CDN_json['Answer'][1]['data']
    Dianxin_Ningxia_CDN_result2 = Dianxin_Ningxia_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Ningxia"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Ningxia_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Ningxia_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Ningxia_CT_RecordSetId=json.dumps(resp_Ningxia_CT_RecordSetId.to_json_object())
    result_Ningxia_CT_RecordSetId_json=json.loads(result_Ningxia_CT_RecordSetId)
    Ningxia_CT_RecordSetId=result_Ningxia_CT_RecordSetId_json['recordsets'][0]['id']
    print(Ningxia_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Ningxia_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Ningxia_CDN_result1,
            Dianxin_Ningxia_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 宁夏移动
    # 获取宁夏移动调度结果
    Yidong_Ningxia_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_NINGXIA_CM})
    print(Yidong_Ningxia_CDN.text)
    Yidong_Ningxia_CDN_json = json.loads(Yidong_Ningxia_CDN.text)
    Yidong_Ningxia_CDN_result1 = Yidong_Ningxia_CDN_json['Answer'][1]['data']
    Yidong_Ningxia_CDN_result2 = Yidong_Ningxia_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Ningxia"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Ningxia_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Ningxia_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Ningxia_CM_RecordSetId=json.dumps(resp_Ningxia_CM_RecordSetId.to_json_object())
    result_Ningxia_CM_RecordSetId_json=json.loads(result_Ningxia_CM_RecordSetId)
    Ningxia_CM_RecordSetId=result_Ningxia_CM_RecordSetId_json['recordsets'][0]['id']
    print(Ningxia_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Ningxia_CM_RecordSetId
        listRecordsbody = [
            Yidong_Ningxia_CDN_result1,
            Yidong_Ningxia_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 宁夏联通
    # 获取宁夏联通调度结果
    Liantong_Ningxia_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_NINGXIA_CU})
    print(Liantong_Ningxia_CDN.text)
    Liantong_Ningxia_CDN_json = json.loads(Liantong_Ningxia_CDN.text)
    Liantong_Ningxia_CDN_result1 = Liantong_Ningxia_CDN_json['Answer'][1]['data']
    Liantong_Ningxia_CDN_result2 = Liantong_Ningxia_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Ningxia"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Ningxia_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Ningxia_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Ningxia_CU_RecordSetId=json.dumps(resp_Ningxia_CU_RecordSetId.to_json_object())
    result_Ningxia_CU_RecordSetId_json=json.loads(result_Ningxia_CU_RecordSetId)
    Ningxia_CU_RecordSetId=result_Ningxia_CU_RecordSetId_json['recordsets'][0]['id']
    print(Ningxia_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Ningxia_CU_RecordSetId
        listRecordsbody = [
            Liantong_Ningxia_CDN_result1,
            Liantong_Ningxia_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 新疆
    # 新疆电信
    # 获取新疆电信调度结果
    Dianxin_Xinjiang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_XINJIANG_CT})
    print(Dianxin_Xinjiang_CDN.text)
    Dianxin_Xinjiang_CDN_json = json.loads(Dianxin_Xinjiang_CDN.text)
    Dianxin_Xinjiang_CDN_result1 = Dianxin_Xinjiang_CDN_json['Answer'][1]['data']
    Dianxin_Xinjiang_CDN_result2 = Dianxin_Xinjiang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Xinjiang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Xinjiang_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Xinjiang_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Xinjiang_CT_RecordSetId=json.dumps(resp_Xinjiang_CT_RecordSetId.to_json_object())
    result_Xinjiang_CT_RecordSetId_json=json.loads(result_Xinjiang_CT_RecordSetId)
    Xinjiang_CT_RecordSetId=result_Xinjiang_CT_RecordSetId_json['recordsets'][0]['id']
    print(Xinjiang_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Xinjiang_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Xinjiang_CDN_result1,
            Dianxin_Xinjiang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 新疆移动
    # 获取新疆移动调度结果
    Yidong_Xinjiang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_XINJIANG_CM})
    print(Yidong_Xinjiang_CDN.text)
    Yidong_Xinjiang_CDN_json = json.loads(Yidong_Xinjiang_CDN.text)
    Yidong_Xinjiang_CDN_result1 = Yidong_Xinjiang_CDN_json['Answer'][1]['data']
    Yidong_Xinjiang_CDN_result2 = Yidong_Xinjiang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Xinjiang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Xinjiang_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Xinjiang_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Xinjiang_CM_RecordSetId=json.dumps(resp_Xinjiang_CM_RecordSetId.to_json_object())
    result_Xinjiang_CM_RecordSetId_json=json.loads(result_Xinjiang_CM_RecordSetId)
    Xinjiang_CM_RecordSetId=result_Xinjiang_CM_RecordSetId_json['recordsets'][0]['id']
    print(Xinjiang_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Xinjiang_CM_RecordSetId
        listRecordsbody = [
            Yidong_Xinjiang_CDN_result1,
            Yidong_Xinjiang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 新疆联通
    # 获取新疆联通调度结果
    Liantong_Xinjiang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_XINJIANG_CU})
    print(Liantong_Xinjiang_CDN.text)
    Liantong_Xinjiang_CDN_json = json.loads(Liantong_Xinjiang_CDN.text)
    Liantong_Xinjiang_CDN_result1 = Liantong_Xinjiang_CDN_json['Answer'][1]['data']
    Liantong_Xinjiang_CDN_result2 = Liantong_Xinjiang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Xinjiang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Xinjiang_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Xinjiang_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Xinjiang_CU_RecordSetId=json.dumps(resp_Xinjiang_CU_RecordSetId.to_json_object())
    result_Xinjiang_CU_RecordSetId_json=json.loads(result_Xinjiang_CU_RecordSetId)
    Xinjiang_CU_RecordSetId=result_Xinjiang_CU_RecordSetId_json['recordsets'][0]['id']
    print(Xinjiang_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Xinjiang_CU_RecordSetId
        listRecordsbody = [
            Liantong_Xinjiang_CDN_result1,
            Liantong_Xinjiang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 河南
    # 河南电信
    # 获取河南电信调度结果
    Dianxin_Henan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HENAN_CT})
    print(Dianxin_Henan_CDN.text)
    Dianxin_Henan_CDN_json = json.loads(Dianxin_Henan_CDN.text)
    Dianxin_Henan_CDN_result1 = Dianxin_Henan_CDN_json['Answer'][1]['data']
    Dianxin_Henan_CDN_result2 = Dianxin_Henan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Henan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Henan_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Henan_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Henan_CT_RecordSetId=json.dumps(resp_Henan_CT_RecordSetId.to_json_object())
    result_Henan_CT_RecordSetId_json=json.loads(result_Henan_CT_RecordSetId)
    Henan_CT_RecordSetId=result_Henan_CT_RecordSetId_json['recordsets'][0]['id']
    print(Henan_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Henan_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Henan_CDN_result1,
            Dianxin_Henan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 河南移动
    # 获取河南移动调度结果
    Yidong_Henan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HENAN_CM})
    print(Yidong_Henan_CDN.text)
    Yidong_Henan_CDN_json = json.loads(Yidong_Henan_CDN.text)
    Yidong_Henan_CDN_result1 = Yidong_Henan_CDN_json['Answer'][1]['data']
    Yidong_Henan_CDN_result2 = Yidong_Henan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Henan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Henan_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Henan_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Henan_CM_RecordSetId=json.dumps(resp_Henan_CM_RecordSetId.to_json_object())
    result_Henan_CM_RecordSetId_json=json.loads(result_Henan_CM_RecordSetId)
    Henan_CM_RecordSetId=result_Henan_CM_RecordSetId_json['recordsets'][0]['id']
    print(Henan_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Henan_CM_RecordSetId
        listRecordsbody = [
            Yidong_Henan_CDN_result1,
            Yidong_Henan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 河南联通
    # 获取河南联通调度结果
    Liantong_Henan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HENAN_CU})
    print(Liantong_Henan_CDN.text)
    Liantong_Henan_CDN_json = json.loads(Liantong_Henan_CDN.text)
    Liantong_Henan_CDN_result1 = Liantong_Henan_CDN_json['Answer'][1]['data']
    Liantong_Henan_CDN_result2 = Liantong_Henan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Henan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Henan_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Henan_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Henan_CU_RecordSetId=json.dumps(resp_Henan_CU_RecordSetId.to_json_object())
    result_Henan_CU_RecordSetId_json=json.loads(result_Henan_CU_RecordSetId)
    Henan_CU_RecordSetId=result_Henan_CU_RecordSetId_json['recordsets'][0]['id']
    print(Henan_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Henan_CU_RecordSetId
        listRecordsbody = [
            Liantong_Henan_CDN_result1,
            Liantong_Henan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 湖北
    # 湖北电信
    # 获取湖北电信调度结果
    Dianxin_Hubei_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HUBEI_CT})
    print(Dianxin_Hubei_CDN.text)
    Dianxin_Hubei_CDN_json = json.loads(Dianxin_Hubei_CDN.text)
    Dianxin_Hubei_CDN_result1 = Dianxin_Hubei_CDN_json['Answer'][1]['data']
    Dianxin_Hubei_CDN_result2 = Dianxin_Hubei_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Hubei"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hubei_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hubei_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hubei_CT_RecordSetId=json.dumps(resp_Hubei_CT_RecordSetId.to_json_object())
    result_Hubei_CT_RecordSetId_json=json.loads(result_Hubei_CT_RecordSetId)
    Hubei_CT_RecordSetId=result_Hubei_CT_RecordSetId_json['recordsets'][0]['id']
    print(Hubei_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hubei_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Hubei_CDN_result1,
            Dianxin_Hubei_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 湖北移动
    # 获取湖北移动调度结果
    Yidong_Hubei_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HUBEI_CM})
    print(Yidong_Hubei_CDN.text)
    Yidong_Hubei_CDN_json = json.loads(Yidong_Hubei_CDN.text)
    Yidong_Hubei_CDN_result1 = Yidong_Hubei_CDN_json['Answer'][1]['data']
    Yidong_Hubei_CDN_result2 = Yidong_Hubei_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Hubei"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hubei_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hubei_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hubei_CM_RecordSetId=json.dumps(resp_Hubei_CM_RecordSetId.to_json_object())
    result_Hubei_CM_RecordSetId_json=json.loads(result_Hubei_CM_RecordSetId)
    Hubei_CM_RecordSetId=result_Hubei_CM_RecordSetId_json['recordsets'][0]['id']
    print(Hubei_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hubei_CM_RecordSetId
        listRecordsbody = [
            Yidong_Hubei_CDN_result1,
            Yidong_Hubei_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 湖北联通
    # 获取湖北联通调度结果
    Liantong_Hubei_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HUBEI_CU})
    print(Liantong_Hubei_CDN.text)
    Liantong_Hubei_CDN_json = json.loads(Liantong_Hubei_CDN.text)
    Liantong_Hubei_CDN_result1 = Liantong_Hubei_CDN_json['Answer'][1]['data']
    Liantong_Hubei_CDN_result2 = Liantong_Hubei_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Hubei"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hubei_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hubei_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hubei_CU_RecordSetId=json.dumps(resp_Hubei_CU_RecordSetId.to_json_object())
    result_Hubei_CU_RecordSetId_json=json.loads(result_Hubei_CU_RecordSetId)
    Hubei_CU_RecordSetId=result_Hubei_CU_RecordSetId_json['recordsets'][0]['id']
    print(Hubei_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hubei_CU_RecordSetId
        listRecordsbody = [
            Liantong_Hubei_CDN_result1,
            Liantong_Hubei_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 湖南
    # 获取湖南电信调度结果
    Dianxin_Hunan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HUNAN_CT})
    print(Dianxin_Hunan_CDN.text)
    Dianxin_Hunan_CDN_json = json.loads(Dianxin_Hunan_CDN.text)
    Dianxin_Hunan_CDN_result1 = Dianxin_Hunan_CDN_json['Answer'][1]['data']
    Dianxin_Hunan_CDN_result2 = Dianxin_Hunan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Hunan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hunan_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hunan_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hunan_CT_RecordSetId=json.dumps(resp_Hunan_CT_RecordSetId.to_json_object())
    result_Hunan_CT_RecordSetId_json=json.loads(result_Hunan_CT_RecordSetId)
    Hunan_CT_RecordSetId=result_Hunan_CT_RecordSetId_json['recordsets'][0]['id']
    print(Hunan_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hunan_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Hunan_CDN_result1,
            Dianxin_Hunan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 湖南移动
    # 获取湖南移动调度结果
    Yidong_Hunan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HUNAN_CM})
    print(Yidong_Hunan_CDN.text)
    Yidong_Hunan_CDN_json = json.loads(Yidong_Hunan_CDN.text)
    Yidong_Hunan_CDN_result1 = Yidong_Hunan_CDN_json['Answer'][1]['data']
    Yidong_Hunan_CDN_result2 = Yidong_Hunan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Hunan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hunan_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hunan_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hunan_CM_RecordSetId=json.dumps(resp_Hunan_CM_RecordSetId.to_json_object())
    result_Hunan_CM_RecordSetId_json=json.loads(result_Hunan_CM_RecordSetId)
    Hunan_CM_RecordSetId=result_Hunan_CM_RecordSetId_json['recordsets'][0]['id']
    print(Hunan_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hunan_CM_RecordSetId
        listRecordsbody = [
            Yidong_Hunan_CDN_result1,
            Yidong_Hunan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 湖南联通
    # 获取湖南联通调度结果
    Liantong_Hunan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HUNAN_CU})
    print(Liantong_Hunan_CDN.text)
    Liantong_Hunan_CDN_json = json.loads(Liantong_Hunan_CDN.text)
    Liantong_Hunan_CDN_result1 = Liantong_Hunan_CDN_json['Answer'][1]['data']
    Liantong_Hunan_CDN_result2 = Liantong_Hunan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Hunan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hunan_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hunan_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hunan_CU_RecordSetId=json.dumps(resp_Hunan_CU_RecordSetId.to_json_object())
    result_Hunan_CU_RecordSetId_json=json.loads(result_Hunan_CU_RecordSetId)
    Hunan_CU_RecordSetId=result_Hunan_CU_RecordSetId_json['recordsets'][0]['id']
    print(Hunan_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hunan_CU_RecordSetId
        listRecordsbody = [
            Liantong_Hunan_CDN_result1,
            Liantong_Hunan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 上海
    # 上海电信
    # 获取上海电信调度结果
    Dianxin_Shanghai_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHANGHAI_CT})
    print(Dianxin_Shanghai_CDN.text)
    Dianxin_Shanghai_CDN_json = json.loads(Dianxin_Shanghai_CDN.text)
    Dianxin_Shanghai_CDN_result1 = Dianxin_Shanghai_CDN_json['Answer'][1]['data']
    Dianxin_Shanghai_CDN_result2 = Dianxin_Shanghai_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Shanghai"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shanghai_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shanghai_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shanghai_CT_RecordSetId=json.dumps(resp_Shanghai_CT_RecordSetId.to_json_object())
    result_Shanghai_CT_RecordSetId_json=json.loads(result_Shanghai_CT_RecordSetId)
    Shanghai_CT_RecordSetId=result_Shanghai_CT_RecordSetId_json['recordsets'][0]['id']
    print(Shanghai_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shanghai_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Shanghai_CDN_result1,
            Dianxin_Shanghai_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 上海移动
    # 获取上海移动调度结果
    Yidong_Shanghai_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHANGHAI_CM})
    print(Yidong_Shanghai_CDN.text)
    Yidong_Shanghai_CDN_json = json.loads(Yidong_Shanghai_CDN.text)
    Yidong_Shanghai_CDN_result1 = Yidong_Shanghai_CDN_json['Answer'][1]['data']
    Yidong_Shanghai_CDN_result2 = Yidong_Shanghai_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Shanghai"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shanghai_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shanghai_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shanghai_CM_RecordSetId=json.dumps(resp_Shanghai_CM_RecordSetId.to_json_object())
    result_Shanghai_CM_RecordSetId_json=json.loads(result_Shanghai_CM_RecordSetId)
    Shanghai_CM_RecordSetId=result_Shanghai_CM_RecordSetId_json['recordsets'][0]['id']
    print(Shanghai_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shanghai_CM_RecordSetId
        listRecordsbody = [
            Yidong_Shanghai_CDN_result1,
            Yidong_Shanghai_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 上海联通
    # 获取上海联通调度结果
    Liantong_Shanghai_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHANGHAI_CU})
    print(Liantong_Shanghai_CDN.text)
    Liantong_Shanghai_CDN_json = json.loads(Liantong_Shanghai_CDN.text)
    Liantong_Shanghai_CDN_result1 = Liantong_Shanghai_CDN_json['Answer'][1]['data']
    Liantong_Shanghai_CDN_result2 = Liantong_Shanghai_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Shanghai"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shanghai_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shanghai_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shanghai_CU_RecordSetId=json.dumps(resp_Shanghai_CU_RecordSetId.to_json_object())
    result_Shanghai_CU_RecordSetId_json=json.loads(result_Shanghai_CU_RecordSetId)
    Shanghai_CU_RecordSetId=result_Shanghai_CU_RecordSetId_json['recordsets'][0]['id']
    print(Shanghai_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shanghai_CU_RecordSetId
        listRecordsbody = [
            Liantong_Shanghai_CDN_result1,
            Liantong_Shanghai_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 江苏
    # 江苏电信
    # 获取江苏电信调度结果
    Dianxin_Jiangsu_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_JIANGSU_CT})
    print(Dianxin_Jiangsu_CDN.text)
    Dianxin_Jiangsu_CDN_json = json.loads(Dianxin_Jiangsu_CDN.text)
    Dianxin_Jiangsu_CDN_result1 = Dianxin_Jiangsu_CDN_json['Answer'][1]['data']
    Dianxin_Jiangsu_CDN_result2 = Dianxin_Jiangsu_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Jiangsu"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Jiangsu_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Jiangsu_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Jiangsu_CT_RecordSetId=json.dumps(resp_Jiangsu_CT_RecordSetId.to_json_object())
    result_Jiangsu_CT_RecordSetId_json=json.loads(result_Jiangsu_CT_RecordSetId)
    Jiangsu_CT_RecordSetId=result_Jiangsu_CT_RecordSetId_json['recordsets'][0]['id']
    print(Jiangsu_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Jiangsu_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Jiangsu_CDN_result1,
            Dianxin_Jiangsu_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 江苏移动
    # 获取江苏移动调度结果
    Yidong_Jiangsu_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_JIANGSU_CM})
    print(Yidong_Jiangsu_CDN.text)
    Yidong_Jiangsu_CDN_json = json.loads(Yidong_Jiangsu_CDN.text)
    Yidong_Jiangsu_CDN_result1 = Yidong_Jiangsu_CDN_json['Answer'][1]['data']
    Yidong_Jiangsu_CDN_result2 = Yidong_Jiangsu_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Jiangsu"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Jiangsu_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Jiangsu_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Jiangsu_CM_RecordSetId=json.dumps(resp_Jiangsu_CM_RecordSetId.to_json_object())
    result_Jiangsu_CM_RecordSetId_json=json.loads(result_Jiangsu_CM_RecordSetId)
    Jiangsu_CM_RecordSetId=result_Jiangsu_CM_RecordSetId_json['recordsets'][0]['id']
    print(Jiangsu_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Jiangsu_CM_RecordSetId
        listRecordsbody = [
            Yidong_Jiangsu_CDN_result1,
            Yidong_Jiangsu_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 江苏联通
    # 获取江苏联通调度结果
    Liantong_Jiangsu_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_JIANGSU_CU})
    print(Liantong_Jiangsu_CDN.text)
    Liantong_Jiangsu_CDN_json = json.loads(Liantong_Jiangsu_CDN.text)
    Liantong_Jiangsu_CDN_result1 = Liantong_Jiangsu_CDN_json['Answer'][1]['data']
    Liantong_Jiangsu_CDN_result2 = Liantong_Jiangsu_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Jiangsu"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Jiangsu_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Jiangsu_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Jiangsu_CU_RecordSetId=json.dumps(resp_Jiangsu_CU_RecordSetId.to_json_object())
    result_Jiangsu_CU_RecordSetId_json=json.loads(result_Jiangsu_CU_RecordSetId)
    Jiangsu_CU_RecordSetId=result_Jiangsu_CU_RecordSetId_json['recordsets'][0]['id']
    print(Jiangsu_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Jiangsu_CU_RecordSetId
        listRecordsbody = [
            Liantong_Jiangsu_CDN_result1,
            Liantong_Jiangsu_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 浙江
    # 浙江电信
    # 获取浙江电信调度结果
    Dianxin_Zhejiang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_ZHEJIANG_CT})
    print(Dianxin_Zhejiang_CDN.text)
    Dianxin_Zhejiang_CDN_json = json.loads(Dianxin_Zhejiang_CDN.text)
    Dianxin_Zhejiang_CDN_result1 = Dianxin_Zhejiang_CDN_json['Answer'][1]['data']
    Dianxin_Zhejiang_CDN_result2 = Dianxin_Zhejiang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Zhejiang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Zhejiang_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Zhejiang_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Zhejiang_CT_RecordSetId=json.dumps(resp_Zhejiang_CT_RecordSetId.to_json_object())
    result_Zhejiang_CT_RecordSetId_json=json.loads(result_Zhejiang_CT_RecordSetId)
    Zhejiang_CT_RecordSetId=result_Zhejiang_CT_RecordSetId_json['recordsets'][0]['id']
    print(Zhejiang_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Zhejiang_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Zhejiang_CDN_result1,
            Dianxin_Zhejiang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 浙江移动
    # 获取浙江移动调度结果
    Yidong_Zhejiang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_ZHEJIANG_CM})
    print(Yidong_Zhejiang_CDN.text)
    Yidong_Zhejiang_CDN_json = json.loads(Yidong_Zhejiang_CDN.text)
    Yidong_Zhejiang_CDN_result1 = Yidong_Zhejiang_CDN_json['Answer'][1]['data']
    Yidong_Zhejiang_CDN_result2 = Yidong_Zhejiang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Zhejiang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Zhejiang_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Zhejiang_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Zhejiang_CM_RecordSetId=json.dumps(resp_Zhejiang_CM_RecordSetId.to_json_object())
    result_Zhejiang_CM_RecordSetId_json=json.loads(result_Zhejiang_CM_RecordSetId)
    Zhejiang_CM_RecordSetId=result_Zhejiang_CM_RecordSetId_json['recordsets'][0]['id']
    print(Zhejiang_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Zhejiang_CM_RecordSetId
        listRecordsbody = [
            Yidong_Zhejiang_CDN_result1,
            Yidong_Zhejiang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 浙江联通
    # 获取浙江联通调度结果
    Liantong_Zhejiang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_ZHEJIANG_CU})
    print(Liantong_Zhejiang_CDN.text)
    Liantong_Zhejiang_CDN_json = json.loads(Liantong_Zhejiang_CDN.text)
    Liantong_Zhejiang_CDN_result1 = Liantong_Zhejiang_CDN_json['Answer'][1]['data']
    Liantong_Zhejiang_CDN_result2 = Liantong_Zhejiang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Zhejiang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Zhejiang_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Zhejiang_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Zhejiang_CU_RecordSetId=json.dumps(resp_Zhejiang_CU_RecordSetId.to_json_object())
    result_Zhejiang_CU_RecordSetId_json=json.loads(result_Zhejiang_CU_RecordSetId)
    Zhejiang_CU_RecordSetId=result_Zhejiang_CU_RecordSetId_json['recordsets'][0]['id']
    print(Zhejiang_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Zhejiang_CU_RecordSetId
        listRecordsbody = [
            Liantong_Zhejiang_CDN_result1,
            Liantong_Zhejiang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 安徽
    # 安徽电信
    # 获取安徽电信调度结果
    Dianxin_Anhui_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_Anhui_CT})
    print(Dianxin_Anhui_CDN.text)
    Dianxin_Anhui_CDN_json = json.loads(Dianxin_Anhui_CDN.text)
    Dianxin_Anhui_CDN_result1 = Dianxin_Anhui_CDN_json['Answer'][1]['data']
    Dianxin_Anhui_CDN_result2 = Dianxin_Anhui_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Anhui"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Anhui_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Anhui_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Anhui_CT_RecordSetId=json.dumps(resp_Anhui_CT_RecordSetId.to_json_object())
    result_Anhui_CT_RecordSetId_json=json.loads(result_Anhui_CT_RecordSetId)
    Anhui_CT_RecordSetId=result_Anhui_CT_RecordSetId_json['recordsets'][0]['id']
    print(Anhui_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Anhui_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Anhui_CDN_result1,
            Dianxin_Anhui_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 安徽移动
    # 获取安徽移动调度结果
    Yidong_Anhui_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_Anhui_CM})
    print(Yidong_Anhui_CDN.text)
    Yidong_Anhui_CDN_json = json.loads(Yidong_Anhui_CDN.text)
    Yidong_Anhui_CDN_result1 = Yidong_Anhui_CDN_json['Answer'][1]['data']
    Yidong_Anhui_CDN_result2 = Yidong_Anhui_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Anhui"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Anhui_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Anhui_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Anhui_CM_RecordSetId=json.dumps(resp_Anhui_CM_RecordSetId.to_json_object())
    result_Anhui_CM_RecordSetId_json=json.loads(result_Anhui_CM_RecordSetId)
    Anhui_CM_RecordSetId=result_Anhui_CM_RecordSetId_json['recordsets'][0]['id']
    print(Anhui_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Anhui_CM_RecordSetId
        listRecordsbody = [
            Yidong_Anhui_CDN_result1,
            Yidong_Anhui_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 安徽联通
    # 获取安徽联通调度结果
    Liantong_Anhui_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_Anhui_CU})
    print(Liantong_Anhui_CDN.text)
    Liantong_Anhui_CDN_json = json.loads(Liantong_Anhui_CDN.text)
    Liantong_Anhui_CDN_result1 = Liantong_Anhui_CDN_json['Answer'][1]['data']
    Liantong_Anhui_CDN_result2 = Liantong_Anhui_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Anhui"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Anhui_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Anhui_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Anhui_CU_RecordSetId=json.dumps(resp_Anhui_CU_RecordSetId.to_json_object())
    result_Anhui_CU_RecordSetId_json=json.loads(result_Anhui_CU_RecordSetId)
    Anhui_CU_RecordSetId=result_Anhui_CU_RecordSetId_json['recordsets'][0]['id']
    print(Anhui_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Anhui_CU_RecordSetId
        listRecordsbody = [
            Liantong_Anhui_CDN_result1,
            Liantong_Anhui_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 福建
    # 福建电信
    # 获取福建电信调度结果
    Dianxin_Fujian_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_Fujian_CT})
    print(Dianxin_Fujian_CDN.text)
    Dianxin_Fujian_CDN_json = json.loads(Dianxin_Fujian_CDN.text)
    Dianxin_Fujian_CDN_result1 = Dianxin_Fujian_CDN_json['Answer'][1]['data']
    Dianxin_Fujian_CDN_result2 = Dianxin_Fujian_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Fujian"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Fujian_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Fujian_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Fujian_CT_RecordSetId=json.dumps(resp_Fujian_CT_RecordSetId.to_json_object())
    result_Fujian_CT_RecordSetId_json=json.loads(result_Fujian_CT_RecordSetId)
    Fujian_CT_RecordSetId=result_Fujian_CT_RecordSetId_json['recordsets'][0]['id']
    print(Fujian_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Fujian_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Fujian_CDN_result1,
            Dianxin_Fujian_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 福建移动
    # 获取福建移动调度结果
    Yidong_Fujian_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_Fujian_CM})
    print(Yidong_Fujian_CDN.text)
    Yidong_Fujian_CDN_json = json.loads(Yidong_Fujian_CDN.text)
    Yidong_Fujian_CDN_result1 = Yidong_Fujian_CDN_json['Answer'][1]['data']
    Yidong_Fujian_CDN_result2 = Yidong_Fujian_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Fujian"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Fujian_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Fujian_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Fujian_CM_RecordSetId=json.dumps(resp_Fujian_CM_RecordSetId.to_json_object())
    result_Fujian_CM_RecordSetId_json=json.loads(result_Fujian_CM_RecordSetId)
    Fujian_CM_RecordSetId=result_Fujian_CM_RecordSetId_json['recordsets'][0]['id']
    print(Fujian_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Fujian_CM_RecordSetId
        listRecordsbody = [
            Yidong_Fujian_CDN_result1,
            Yidong_Fujian_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 福建联通
    # 获取福建联通调度结果
    Liantong_Fujian_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_Fujian_CU})
    print(Liantong_Fujian_CDN.text)
    Liantong_Fujian_CDN_json = json.loads(Liantong_Fujian_CDN.text)
    Liantong_Fujian_CDN_result1 = Liantong_Fujian_CDN_json['Answer'][1]['data']
    Liantong_Fujian_CDN_result2 = Liantong_Fujian_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Fujian"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Fujian_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Fujian_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Fujian_CU_RecordSetId=json.dumps(resp_Fujian_CU_RecordSetId.to_json_object())
    result_Fujian_CU_RecordSetId_json=json.loads(result_Fujian_CU_RecordSetId)
    Fujian_CU_RecordSetId=result_Fujian_CU_RecordSetId_json['recordsets'][0]['id']
    print(Fujian_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Fujian_CU_RecordSetId
        listRecordsbody = [
            Liantong_Fujian_CDN_result1,
            Liantong_Fujian_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 江西
    # 江西电信
    # 获取江西电信调度结果
    Dianxin_Jiangxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_Jiangxi_CT})
    print(Dianxin_Jiangxi_CDN.text)
    Dianxin_Jiangxi_CDN_json = json.loads(Dianxin_Jiangxi_CDN.text)
    Dianxin_Jiangxi_CDN_result1 = Dianxin_Jiangxi_CDN_json['Answer'][1]['data']
    Dianxin_Jiangxi_CDN_result2 = Dianxin_Jiangxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Jiangxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Jiangxi_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Jiangxi_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Jiangxi_CT_RecordSetId=json.dumps(resp_Jiangxi_CT_RecordSetId.to_json_object())
    result_Jiangxi_CT_RecordSetId_json=json.loads(result_Jiangxi_CT_RecordSetId)
    Jiangxi_CT_RecordSetId=result_Jiangxi_CT_RecordSetId_json['recordsets'][0]['id']
    print(Jiangxi_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Jiangxi_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Jiangxi_CDN_result1,
            Dianxin_Jiangxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 江西移动
    # 获取江西移动调度结果
    Yidong_Jiangxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_Jiangxi_CM})
    print(Yidong_Jiangxi_CDN.text)
    Yidong_Jiangxi_CDN_json = json.loads(Yidong_Jiangxi_CDN.text)
    Yidong_Jiangxi_CDN_result1 = Yidong_Jiangxi_CDN_json['Answer'][1]['data']
    Yidong_Jiangxi_CDN_result2 = Yidong_Jiangxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Jiangxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Jiangxi_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Jiangxi_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Jiangxi_CM_RecordSetId=json.dumps(resp_Jiangxi_CM_RecordSetId.to_json_object())
    result_Jiangxi_CM_RecordSetId_json=json.loads(result_Jiangxi_CM_RecordSetId)
    Jiangxi_CM_RecordSetId=result_Jiangxi_CM_RecordSetId_json['recordsets'][0]['id']
    print(Jiangxi_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Jiangxi_CM_RecordSetId
        listRecordsbody = [
            Yidong_Jiangxi_CDN_result1,
            Yidong_Jiangxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 江西联通
    # 获取江西联通调度结果
    Liantong_Jiangxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_Jiangxi_CU})
    print(Liantong_Jiangxi_CDN.text)
    Liantong_Jiangxi_CDN_json = json.loads(Liantong_Jiangxi_CDN.text)
    Liantong_Jiangxi_CDN_result1 = Liantong_Jiangxi_CDN_json['Answer'][1]['data']
    Liantong_Jiangxi_CDN_result2 = Liantong_Jiangxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Jiangxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Jiangxi_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Jiangxi_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Jiangxi_CU_RecordSetId=json.dumps(resp_Jiangxi_CU_RecordSetId.to_json_object())
    result_Jiangxi_CU_RecordSetId_json=json.loads(result_Jiangxi_CU_RecordSetId)
    Jiangxi_CU_RecordSetId=result_Jiangxi_CU_RecordSetId_json['recordsets'][0]['id']
    print(Jiangxi_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Jiangxi_CU_RecordSetId
        listRecordsbody = [
            Liantong_Jiangxi_CDN_result1,
            Liantong_Jiangxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 山东
    # 山东电信
    # 获取山东电信调度结果
    Dianxin_Shandong_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHANDONG_CT})
    print(Dianxin_Shandong_CDN.text)
    Dianxin_Shandong_CDN_json = json.loads(Dianxin_Shandong_CDN.text)
    Dianxin_Shandong_CDN_result1 = Dianxin_Shandong_CDN_json['Answer'][1]['data']
    Dianxin_Shandong_CDN_result2 = Dianxin_Shandong_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Shandong"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shandong_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shandong_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shandong_CT_RecordSetId=json.dumps(resp_Shandong_CT_RecordSetId.to_json_object())
    result_Shandong_CT_RecordSetId_json=json.loads(result_Shandong_CT_RecordSetId)
    Shandong_CT_RecordSetId=result_Shandong_CT_RecordSetId_json['recordsets'][0]['id']
    print(Shandong_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shandong_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Shandong_CDN_result1,
            Dianxin_Shandong_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 山东移动
    # 获取山东移动调度结果
    Yidong_Shandong_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHANDONG_CM})
    print(Yidong_Shandong_CDN.text)
    Yidong_Shandong_CDN_json = json.loads(Yidong_Shandong_CDN.text)
    Yidong_Shandong_CDN_result1 = Yidong_Shandong_CDN_json['Answer'][1]['data']
    Yidong_Shandong_CDN_result2 = Yidong_Shandong_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Shandong"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shandong_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shandong_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shandong_CM_RecordSetId=json.dumps(resp_Shandong_CM_RecordSetId.to_json_object())
    result_Shandong_CM_RecordSetId_json=json.loads(result_Shandong_CM_RecordSetId)
    Shandong_CM_RecordSetId=result_Shandong_CM_RecordSetId_json['recordsets'][0]['id']
    print(Shandong_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shandong_CM_RecordSetId
        listRecordsbody = [
            Yidong_Shandong_CDN_result1,
            Yidong_Shandong_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 山东联通
    # 获取山东联通调度结果
    Liantong_Shandong_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SHANDONG_CU})
    print(Liantong_Shandong_CDN.text)
    Liantong_Shandong_CDN_json = json.loads(Liantong_Shandong_CDN.text)
    Liantong_Shandong_CDN_result1 = Liantong_Shandong_CDN_json['Answer'][1]['data']
    Liantong_Shandong_CDN_result2 = Liantong_Shandong_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Shandong"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Shandong_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Shandong_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Shandong_CU_RecordSetId=json.dumps(resp_Shandong_CU_RecordSetId.to_json_object())
    result_Shandong_CU_RecordSetId_json=json.loads(result_Shandong_CU_RecordSetId)
    Shandong_CU_RecordSetId=result_Shandong_CU_RecordSetId_json['recordsets'][0]['id']
    print(Shandong_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Shandong_CU_RecordSetId
        listRecordsbody = [
            Liantong_Shandong_CDN_result1,
            Liantong_Shandong_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 广东
    # 广东电信
    # 获取广东电信调度结果
    Dianxin_Guangdong_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GUANGDONG_CT})
    print(Dianxin_Guangdong_CDN.text)
    Dianxin_Guangdong_CDN_json = json.loads(Dianxin_Guangdong_CDN.text)
    Dianxin_Guangdong_CDN_result1 = Dianxin_Guangdong_CDN_json['Answer'][1]['data']
    Dianxin_Guangdong_CDN_result2 = Dianxin_Guangdong_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Guangdong"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Guangdong_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Guangdong_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Guangdong_CT_RecordSetId=json.dumps(resp_Guangdong_CT_RecordSetId.to_json_object())
    result_Guangdong_CT_RecordSetId_json=json.loads(result_Guangdong_CT_RecordSetId)
    Guangdong_CT_RecordSetId=result_Guangdong_CT_RecordSetId_json['recordsets'][0]['id']
    print(Guangdong_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Guangdong_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Guangdong_CDN_result1,
            Dianxin_Guangdong_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 广东移动
    # 获取广东移动调度结果
    Yidong_Guangdong_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GUANGDONG_CM})
    print(Yidong_Guangdong_CDN.text)
    Yidong_Guangdong_CDN_json = json.loads(Yidong_Guangdong_CDN.text)
    Yidong_Guangdong_CDN_result1 = Yidong_Guangdong_CDN_json['Answer'][1]['data']
    Yidong_Guangdong_CDN_result2 = Yidong_Guangdong_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Guangdong"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Guangdong_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Guangdong_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Guangdong_CM_RecordSetId=json.dumps(resp_Guangdong_CM_RecordSetId.to_json_object())
    result_Guangdong_CM_RecordSetId_json=json.loads(result_Guangdong_CM_RecordSetId)
    Guangdong_CM_RecordSetId=result_Guangdong_CM_RecordSetId_json['recordsets'][0]['id']
    print(Guangdong_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Guangdong_CM_RecordSetId
        listRecordsbody = [
            Yidong_Guangdong_CDN_result1,
            Yidong_Guangdong_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 广东联通
    # 获取广东联通调度结果
    Liantong_Guangdong_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GUANGDONG_CU})
    print(Liantong_Guangdong_CDN.text)
    Liantong_Guangdong_CDN_json = json.loads(Liantong_Guangdong_CDN.text)
    Liantong_Guangdong_CDN_result1 = Liantong_Guangdong_CDN_json['Answer'][1]['data']
    Liantong_Guangdong_CDN_result2 = Liantong_Guangdong_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Guangdong"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Guangdong_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Guangdong_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Guangdong_CU_RecordSetId=json.dumps(resp_Guangdong_CU_RecordSetId.to_json_object())
    result_Guangdong_CU_RecordSetId_json=json.loads(result_Guangdong_CU_RecordSetId)
    Guangdong_CU_RecordSetId=result_Guangdong_CU_RecordSetId_json['recordsets'][0]['id']
    print(Guangdong_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Guangdong_CU_RecordSetId
        listRecordsbody = [
            Liantong_Guangdong_CDN_result1,
            Liantong_Guangdong_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 海南
    # 海南电信
    # 获取海南电信调度结果
    Dianxin_Hainan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HAINAN_CT})
    print(Dianxin_Hainan_CDN.text)
    Dianxin_Hainan_CDN_json = json.loads(Dianxin_Hainan_CDN.text)
    Dianxin_Hainan_CDN_result1 = Dianxin_Hainan_CDN_json['Answer'][1]['data']
    Dianxin_Hainan_CDN_result2 = Dianxin_Hainan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Hainan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hainan_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hainan_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hainan_CT_RecordSetId=json.dumps(resp_Hainan_CT_RecordSetId.to_json_object())
    result_Hainan_CT_RecordSetId_json=json.loads(result_Hainan_CT_RecordSetId)
    Hainan_CT_RecordSetId=result_Hainan_CT_RecordSetId_json['recordsets'][0]['id']
    print(Hainan_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hainan_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Hainan_CDN_result1,
            Dianxin_Hainan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 海南移动
    # 获取海南移动调度结果
    Yidong_Hainan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HAINAN_CM})
    print(Yidong_Hainan_CDN.text)
    Yidong_Hainan_CDN_json = json.loads(Yidong_Hainan_CDN.text)
    Yidong_Hainan_CDN_result1 = Yidong_Hainan_CDN_json['Answer'][1]['data']
    Yidong_Hainan_CDN_result2 = Yidong_Hainan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Hainan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hainan_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hainan_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hainan_CM_RecordSetId=json.dumps(resp_Hainan_CM_RecordSetId.to_json_object())
    result_Hainan_CM_RecordSetId_json=json.loads(result_Hainan_CM_RecordSetId)
    Hainan_CM_RecordSetId=result_Hainan_CM_RecordSetId_json['recordsets'][0]['id']
    print(Hainan_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hainan_CM_RecordSetId
        listRecordsbody = [
            Yidong_Hainan_CDN_result1,
            Yidong_Hainan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 海南联通
    # 获取海南联通调度结果
    Liantong_Hainan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_HAINAN_CU})
    print(Liantong_Hainan_CDN.text)
    Liantong_Hainan_CDN_json = json.loads(Liantong_Hainan_CDN.text)
    Liantong_Hainan_CDN_result1 = Liantong_Hainan_CDN_json['Answer'][1]['data']
    Liantong_Hainan_CDN_result2 = Liantong_Hainan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Hainan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Hainan_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Hainan_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Hainan_CU_RecordSetId=json.dumps(resp_Hainan_CU_RecordSetId.to_json_object())
    result_Hainan_CU_RecordSetId_json=json.loads(result_Hainan_CU_RecordSetId)
    Hainan_CU_RecordSetId=result_Hainan_CU_RecordSetId_json['recordsets'][0]['id']
    print(Hainan_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Hainan_CU_RecordSetId
        listRecordsbody = [
            Liantong_Hainan_CDN_result1,
            Liantong_Hainan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 广西
    # 广西电信
    # 获取广西电信调度结果
    Dianxin_Guangxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GUANGXI_CT})
    print(Dianxin_Guangxi_CDN.text)
    Dianxin_Guangxi_CDN_json = json.loads(Dianxin_Guangxi_CDN.text)
    Dianxin_Guangxi_CDN_result1 = Dianxin_Guangxi_CDN_json['Answer'][1]['data']
    Dianxin_Guangxi_CDN_result2 = Dianxin_Guangxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Guangxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Guangxi_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Guangxi_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Guangxi_CT_RecordSetId=json.dumps(resp_Guangxi_CT_RecordSetId.to_json_object())
    result_Guangxi_CT_RecordSetId_json=json.loads(result_Guangxi_CT_RecordSetId)
    Guangxi_CT_RecordSetId=result_Guangxi_CT_RecordSetId_json['recordsets'][0]['id']
    print(Guangxi_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Guangxi_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Guangxi_CDN_result1,
            Dianxin_Guangxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 广西移动
    # 获取广西移动调度结果
    Yidong_Guangxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GUANGXI_CM})
    print(Yidong_Guangxi_CDN.text)
    Yidong_Guangxi_CDN_json = json.loads(Yidong_Guangxi_CDN.text)
    Yidong_Guangxi_CDN_result1 = Yidong_Guangxi_CDN_json['Answer'][1]['data']
    Yidong_Guangxi_CDN_result2 = Yidong_Guangxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Guangxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Guangxi_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Guangxi_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Guangxi_CM_RecordSetId=json.dumps(resp_Guangxi_CM_RecordSetId.to_json_object())
    result_Guangxi_CM_RecordSetId_json=json.loads(result_Guangxi_CM_RecordSetId)
    Guangxi_CM_RecordSetId=result_Guangxi_CM_RecordSetId_json['recordsets'][0]['id']
    print(Guangxi_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Guangxi_CM_RecordSetId
        listRecordsbody = [
            Yidong_Guangxi_CDN_result1,
            Yidong_Guangxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 广西联通
    # 获取广西联通调度结果
    Liantong_Guangxi_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GUANGXI_CU})
    print(Liantong_Guangxi_CDN.text)
    Liantong_Guangxi_CDN_json = json.loads(Liantong_Guangxi_CDN.text)
    Liantong_Guangxi_CDN_result1 = Liantong_Guangxi_CDN_json['Answer'][1]['data']
    Liantong_Guangxi_CDN_result2 = Liantong_Guangxi_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Guangxi"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Guangxi_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Guangxi_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Guangxi_CU_RecordSetId=json.dumps(resp_Guangxi_CU_RecordSetId.to_json_object())
    result_Guangxi_CU_RecordSetId_json=json.loads(result_Guangxi_CU_RecordSetId)
    Guangxi_CU_RecordSetId=result_Guangxi_CU_RecordSetId_json['recordsets'][0]['id']
    print(Guangxi_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Guangxi_CU_RecordSetId
        listRecordsbody = [
            Liantong_Guangxi_CDN_result1,
            Liantong_Guangxi_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 重庆
    # 重庆电信
    # 获取重庆电信调度结果
    Dianxin_Chongqing_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_CHONGQING_CT})
    print(Dianxin_Chongqing_CDN.text)
    Dianxin_Chongqing_CDN_json = json.loads(Dianxin_Chongqing_CDN.text)
    Dianxin_Chongqing_CDN_result1 = Dianxin_Chongqing_CDN_json['Answer'][1]['data']
    Dianxin_Chongqing_CDN_result2 = Dianxin_Chongqing_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Chongqing"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Chongqing_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Chongqing_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Chongqing_CT_RecordSetId=json.dumps(resp_Chongqing_CT_RecordSetId.to_json_object())
    result_Chongqing_CT_RecordSetId_json=json.loads(result_Chongqing_CT_RecordSetId)
    Chongqing_CT_RecordSetId=result_Chongqing_CT_RecordSetId_json['recordsets'][0]['id']
    print(Chongqing_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Chongqing_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Chongqing_CDN_result1,
            Dianxin_Chongqing_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 重庆移动
    # 获取重庆移动调度结果
    Yidong_Chongqing_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_CHONGQING_CM})
    print(Yidong_Chongqing_CDN.text)
    Yidong_Chongqing_CDN_json = json.loads(Yidong_Chongqing_CDN.text)
    Yidong_Chongqing_CDN_result1 = Yidong_Chongqing_CDN_json['Answer'][1]['data']
    Yidong_Chongqing_CDN_result2 = Yidong_Chongqing_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Chongqing"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Chongqing_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Chongqing_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Chongqing_CM_RecordSetId=json.dumps(resp_Chongqing_CM_RecordSetId.to_json_object())
    result_Chongqing_CM_RecordSetId_json=json.loads(result_Chongqing_CM_RecordSetId)
    Chongqing_CM_RecordSetId=result_Chongqing_CM_RecordSetId_json['recordsets'][0]['id']
    print(Chongqing_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Chongqing_CM_RecordSetId
        listRecordsbody = [
            Yidong_Chongqing_CDN_result1,
            Yidong_Chongqing_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 重庆联通
    # 获取重庆联通调度结果
    Liantong_Chongqing_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_CHONGQING_CU})
    print(Liantong_Chongqing_CDN.text)
    Liantong_Chongqing_CDN_json = json.loads(Liantong_Chongqing_CDN.text)
    Liantong_Chongqing_CDN_result1 = Liantong_Chongqing_CDN_json['Answer'][1]['data']
    Liantong_Chongqing_CDN_result2 = Liantong_Chongqing_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Chongqing"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Chongqing_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Chongqing_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Chongqing_CU_RecordSetId=json.dumps(resp_Chongqing_CU_RecordSetId.to_json_object())
    result_Chongqing_CU_RecordSetId_json=json.loads(result_Chongqing_CU_RecordSetId)
    Chongqing_CU_RecordSetId=result_Chongqing_CU_RecordSetId_json['recordsets'][0]['id']
    print(Chongqing_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Chongqing_CU_RecordSetId
        listRecordsbody = [
            Liantong_Chongqing_CDN_result1,
            Liantong_Chongqing_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 四川
    # 四川电信
    # 获取四川电信调度结果
    Dianxin_Sichuan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SICHUAN_CT})
    print(Dianxin_Sichuan_CDN.text)
    Dianxin_Sichuan_CDN_json = json.loads(Dianxin_Sichuan_CDN.text)
    Dianxin_Sichuan_CDN_result1 = Dianxin_Sichuan_CDN_json['Answer'][1]['data']
    Dianxin_Sichuan_CDN_result2 = Dianxin_Sichuan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Sichuan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Sichuan_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Sichuan_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Sichuan_CT_RecordSetId=json.dumps(resp_Sichuan_CT_RecordSetId.to_json_object())
    result_Sichuan_CT_RecordSetId_json=json.loads(result_Sichuan_CT_RecordSetId)
    Sichuan_CT_RecordSetId=result_Sichuan_CT_RecordSetId_json['recordsets'][0]['id']
    print(Sichuan_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Sichuan_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Sichuan_CDN_result1,
            Dianxin_Sichuan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 四川移动
    # 获取四川移动调度结果
    Yidong_Sichuan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SICHUAN_CM})
    print(Yidong_Sichuan_CDN.text)
    Yidong_Sichuan_CDN_json = json.loads(Yidong_Sichuan_CDN.text)
    Yidong_Sichuan_CDN_result1 = Yidong_Sichuan_CDN_json['Answer'][1]['data']
    Yidong_Sichuan_CDN_result2 = Yidong_Sichuan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Sichuan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Sichuan_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Sichuan_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Sichuan_CM_RecordSetId=json.dumps(resp_Sichuan_CM_RecordSetId.to_json_object())
    result_Sichuan_CM_RecordSetId_json=json.loads(result_Sichuan_CM_RecordSetId)
    Sichuan_CM_RecordSetId=result_Sichuan_CM_RecordSetId_json['recordsets'][0]['id']
    print(Sichuan_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Sichuan_CM_RecordSetId
        listRecordsbody = [
            Yidong_Sichuan_CDN_result1,
            Yidong_Sichuan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 四川联通
    # 获取四川联通调度结果
    Liantong_Sichuan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_SICHUAN_CU})
    print(Liantong_Sichuan_CDN.text)
    Liantong_Sichuan_CDN_json = json.loads(Liantong_Sichuan_CDN.text)
    Liantong_Sichuan_CDN_result1 = Liantong_Sichuan_CDN_json['Answer'][1]['data']
    Liantong_Sichuan_CDN_result2 = Liantong_Sichuan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Sichuan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Sichuan_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Sichuan_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Sichuan_CU_RecordSetId=json.dumps(resp_Sichuan_CU_RecordSetId.to_json_object())
    result_Sichuan_CU_RecordSetId_json=json.loads(result_Sichuan_CU_RecordSetId)
    Sichuan_CU_RecordSetId=result_Sichuan_CU_RecordSetId_json['recordsets'][0]['id']
    print(Sichuan_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Sichuan_CU_RecordSetId
        listRecordsbody = [
            Liantong_Sichuan_CDN_result1,
            Liantong_Sichuan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 贵州
    # 贵州电信
    # 获取贵州电信调度结果
    Dianxin_Guizhou_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GUIZHOU_CT})
    print(Dianxin_Guizhou_CDN.text)
    Dianxin_Guizhou_CDN_json = json.loads(Dianxin_Guizhou_CDN.text)
    Dianxin_Guizhou_CDN_result1 = Dianxin_Guizhou_CDN_json['Answer'][1]['data']
    Dianxin_Guizhou_CDN_result2 = Dianxin_Guizhou_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Guizhou"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Guizhou_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Guizhou_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Guizhou_CT_RecordSetId=json.dumps(resp_Guizhou_CT_RecordSetId.to_json_object())
    result_Guizhou_CT_RecordSetId_json=json.loads(result_Guizhou_CT_RecordSetId)
    Guizhou_CT_RecordSetId=result_Guizhou_CT_RecordSetId_json['recordsets'][0]['id']
    print(Guizhou_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Guizhou_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Guizhou_CDN_result1,
            Dianxin_Guizhou_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 贵州移动
    # 获取贵州移动调度结果
    Yidong_Guizhou_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GUIZHOU_CM})
    print(Yidong_Guizhou_CDN.text)
    Yidong_Guizhou_CDN_json = json.loads(Yidong_Guizhou_CDN.text)
    Yidong_Guizhou_CDN_result1 = Yidong_Guizhou_CDN_json['Answer'][1]['data']
    Yidong_Guizhou_CDN_result2 = Yidong_Guizhou_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Guizhou"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Guizhou_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Guizhou_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Guizhou_CM_RecordSetId=json.dumps(resp_Guizhou_CM_RecordSetId.to_json_object())
    result_Guizhou_CM_RecordSetId_json=json.loads(result_Guizhou_CM_RecordSetId)
    Guizhou_CM_RecordSetId=result_Guizhou_CM_RecordSetId_json['recordsets'][0]['id']
    print(Guizhou_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Guizhou_CM_RecordSetId
        listRecordsbody = [
            Yidong_Guizhou_CDN_result1,
            Yidong_Guizhou_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 贵州联通
    # 获取贵州联通调度结果
    Liantong_Guizhou_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_GUIZHOU_CU})
    print(Liantong_Guizhou_CDN.text)
    Liantong_Guizhou_CDN_json = json.loads(Liantong_Guizhou_CDN.text)
    Liantong_Guizhou_CDN_result1 = Liantong_Guizhou_CDN_json['Answer'][1]['data']
    Liantong_Guizhou_CDN_result2 = Liantong_Guizhou_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Guizhou"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Guizhou_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Guizhou_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Guizhou_CU_RecordSetId=json.dumps(resp_Guizhou_CU_RecordSetId.to_json_object())
    result_Guizhou_CU_RecordSetId_json=json.loads(result_Guizhou_CU_RecordSetId)
    Guizhou_CU_RecordSetId=result_Guizhou_CU_RecordSetId_json['recordsets'][0]['id']
    print(Guizhou_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Guizhou_CU_RecordSetId
        listRecordsbody = [
            Liantong_Guizhou_CDN_result1,
            Liantong_Guizhou_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 云南
    # 云南电信
    # 获取云南电信调度结果
    Dianxin_Yunnan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_YUNNAN_CT})
    print(Dianxin_Yunnan_CDN.text)
    Dianxin_Yunnan_CDN_json = json.loads(Dianxin_Yunnan_CDN.text)
    Dianxin_Yunnan_CDN_result1 = Dianxin_Yunnan_CDN_json['Answer'][1]['data']
    Dianxin_Yunnan_CDN_result2 = Dianxin_Yunnan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Yunnan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Yunnan_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Yunnan_CT_RecordSetId)   
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Yunnan_CT_RecordSetId=json.dumps(resp_Yunnan_CT_RecordSetId.to_json_object())
    result_Yunnan_CT_RecordSetId_json=json.loads(result_Yunnan_CT_RecordSetId)
    Yunnan_CT_RecordSetId=result_Yunnan_CT_RecordSetId_json['recordsets'][0]['id']
    print(Yunnan_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Yunnan_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Yunnan_CDN_result1,
            Dianxin_Yunnan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 云南移动
    # 获取云南移动调度结果
    Yidong_Yunnan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_YUNNAN_CM})
    print(Yidong_Yunnan_CDN.text)
    Yidong_Yunnan_CDN_json = json.loads(Yidong_Yunnan_CDN.text)
    Yidong_Yunnan_CDN_result1 = Yidong_Yunnan_CDN_json['Answer'][1]['data']
    Yidong_Yunnan_CDN_result2 = Yidong_Yunnan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Yunnan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Yunnan_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Yunnan_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Yunnan_CM_RecordSetId=json.dumps(resp_Yunnan_CM_RecordSetId.to_json_object())
    result_Yunnan_CM_RecordSetId_json=json.loads(result_Yunnan_CM_RecordSetId)
    Yunnan_CM_RecordSetId=result_Yunnan_CM_RecordSetId_json['recordsets'][0]['id']
    print(Yunnan_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Yunnan_CM_RecordSetId
        listRecordsbody = [
            Yidong_Yunnan_CDN_result1,
            Yidong_Yunnan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 云南联通
    # 获取云南联通调度结果
    Liantong_Yunnan_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_YUNNAN_CU})
    print(Liantong_Yunnan_CDN.text)
    Liantong_Yunnan_CDN_json = json.loads(Liantong_Yunnan_CDN.text)
    Liantong_Yunnan_CDN_result1 = Liantong_Yunnan_CDN_json['Answer'][1]['data']
    Liantong_Yunnan_CDN_result2 = Liantong_Yunnan_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Yunnan"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Yunnan_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Yunnan_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Yunnan_CU_RecordSetId=json.dumps(resp_Yunnan_CU_RecordSetId.to_json_object())
    result_Yunnan_CU_RecordSetId_json=json.loads(result_Yunnan_CU_RecordSetId)
    Yunnan_CU_RecordSetId=result_Yunnan_CU_RecordSetId_json['recordsets'][0]['id']
    print(Yunnan_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Yunnan_CU_RecordSetId
        listRecordsbody = [
            Liantong_Yunnan_CDN_result1,
            Liantong_Yunnan_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 西藏
    # 西藏电信
    # 获取西藏电信调度结果
    Dianxin_Xizang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_XIZANG_CT})
    print(Dianxin_Xizang_CDN.text)
    Dianxin_Xizang_CDN_json = json.loads(Dianxin_Xizang_CDN.text)
    Dianxin_Xizang_CDN_result1 = Dianxin_Xizang_CDN_json['Answer'][1]['data']
    Dianxin_Xizang_CDN_result2 = Dianxin_Xizang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Dianxin_Xizang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Xizang_CT_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Xizang_CT_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Xizang_CT_RecordSetId=json.dumps(resp_Xizang_CT_RecordSetId.to_json_object())
    result_Xizang_CT_RecordSetId_json=json.loads(result_Xizang_CT_RecordSetId)
    Xizang_CT_RecordSetId=result_Xizang_CT_RecordSetId_json['recordsets'][0]['id']
    print(Xizang_CT_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Xizang_CT_RecordSetId
        listRecordsbody = [
            Dianxin_Xizang_CDN_result1,
            Dianxin_Xizang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 西藏移动
    # 获取西藏移动调度结果
    Yidong_Xizang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_XIZANG_CM})
    print(Yidong_Xizang_CDN.text)
    Yidong_Xizang_CDN_json = json.loads(Yidong_Xizang_CDN.text)
    Yidong_Xizang_CDN_result1 = Yidong_Xizang_CDN_json['Answer'][1]['data']
    Yidong_Xizang_CDN_result2 = Yidong_Xizang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Yidong_Xizang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Xizang_CM_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Xizang_CM_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Xizang_CM_RecordSetId=json.dumps(resp_Xizang_CM_RecordSetId.to_json_object())
    result_Xizang_CM_RecordSetId_json=json.loads(result_Xizang_CM_RecordSetId)
    Xizang_CM_RecordSetId=result_Xizang_CM_RecordSetId_json['recordsets'][0]['id']
    print(Xizang_CM_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Xizang_CM_RecordSetId
        listRecordsbody = [
            Yidong_Xizang_CDN_result1,
            Yidong_Xizang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 西藏联通
    # 获取西藏联通调度结果
    Liantong_Xizang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_XIZANG_CU})
    print(Liantong_Xizang_CDN.text)
    Liantong_Xizang_CDN_json = json.loads(Liantong_Xizang_CDN.text)
    Liantong_Xizang_CDN_result1 = Liantong_Xizang_CDN_json['Answer'][1]['data']
    Liantong_Xizang_CDN_result2 = Liantong_Xizang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Liantong_Xizang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Xizang_CU_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Xizang_CU_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Xizang_CU_RecordSetId=json.dumps(resp_Xizang_CU_RecordSetId.to_json_object())
    result_Xizang_CU_RecordSetId_json=json.loads(result_Xizang_CU_RecordSetId)
    Xizang_CU_RecordSetId=result_Xizang_CU_RecordSetId_json['recordsets'][0]['id']
    print(Xizang_CU_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Xizang_CU_RecordSetId
        listRecordsbody = [
            Liantong_Xizang_CDN_result1,
            Liantong_Xizang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 教育网
    # 获取教育网调度结果
    Jiaoyuwang_CDN = requests.get(DoH, params={'name':CDNCNAME, 'type':record_type, 'edns_client_subnet':DNS_JIAOYU})
    print(Jiaoyuwang_CDN.text)
    Jiaoyuwang_CDN_json = json.loads(Jiaoyuwang_CDN.text)
    Jiaoyuwang_CDN_result1 = Jiaoyuwang_CDN_json['Answer'][1]['data']
    Jiaoyuwang_CDN_result2 = Jiaoyuwang_CDN_json['Answer'][2]['data']
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "Jiaoyuwang"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Jiaoyuwang_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Jiaoyuwang_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Jiaoyuwang_RecordSetId=json.dumps(resp_Jiaoyuwang_RecordSetId.to_json_object())
    result_Jiaoyuwang_RecordSetId_json=json.loads(result_Jiaoyuwang_RecordSetId)
    Jiaoyuwang_RecordSetId=result_Jiaoyuwang_RecordSetId_json['recordsets'][0]['id']
    print(Jiaoyuwang_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Jiaoyuwang_RecordSetId
        listRecordsbody = [
            Jiaoyuwang_CDN_result1,
            Jiaoyuwang_CDN_result2
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    # 默认
    # 获取记录集ID
    try:
        request = ShowRecordSetByZoneRequest()
        request.zone_id = zone_id
        request.line_id = "default_view"
        request.status = "ACTIVE"
        request.type = record_type
        request.name = FQDN
        resp_Default_RecordSetId = client.show_record_set_by_zone(request)
        print(resp_Default_RecordSetId)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)
    result_Default_RecordSetId=json.dumps(resp_Default_RecordSetId.to_json_object())
    result_Default_RecordSetId_json=json.loads(result_Default_RecordSetId)
    Default_RecordSetId=result_Default_RecordSetId_json['recordsets'][0]['id']
    print(Default_RecordSetId)
    # 更新记录集
    try:
        request = UpdateRecordSetsRequest()
        request.zone_id = zone_id
        request.recordset_id = Default_RecordSetId
        listRecordsbody = [
            Liantong_Beijing_CDN_result1,
            Liantong_Beijing_CDN_result2,
            Liantong_Guangdong_CDN_result1,
            Liantong_Guangdong_CDN_result2,
            Liantong_Shanghai_CDN_result1,
            Liantong_Shanghai_CDN_result2,
            Dianxin_Beijing_CDN_result1,
            Dianxin_Beijing_CDN_result2,
            Dianxin_Guangdong_CDN_result1,
            Dianxin_Guangdong_CDN_result2,
            Dianxin_Shanghai_CDN_result1,
            Dianxin_Shanghai_CDN_result2,
            Yidong_Beijing_CDN_result1,
            Yidong_Beijing_CDN_result2,
            Yidong_Guangdong_CDN_result1,
            Yidong_Guangdong_CDN_result2,
            Yidong_Shanghai_CDN_result1,
            Yidong_Shanghai_CDN_result2,
        ]
        request.body = UpdateRecordSetsReq(
            records=listRecordsbody,
            ttl=TTL,
            type=record_type,
            name=FQDN
        )
        response = client.update_record_sets(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code, e.request_id, e.error_code, e.error_msg)

    
