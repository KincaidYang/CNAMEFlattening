# DNSPod 拉平脚本，用于拉平根域名的CDN CNAME地址
# 本脚本基于腾讯云API，使用前请先安装SDK，pip install --upgrade tencentcloud-sdk-python
# 使用脚本前请参照说明导入记录，以及修改配置参数
# 本脚本为 HTTPDNS 版本
# 本脚本依赖于腾讯云HTTPDNS服务，使用可能会产生额外的费用
import sys
import requests
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models
if __name__ == '__main__':
    # 配置参数
    # domanin替换为自己的域名
    domain='r2wind.cn'
    # sub_domain替换为自己的子域名
    subdomain='@'
    # CDNCNAME请替换为CDN提供的CNAME地址
    # 使用前请前往https://console.cloud.tencent.com/httpdns/domain 添加CNAME域名
    # 添加域名时仅需要添加主域名，如您的CNAME地址是r2wind.cn.eo.dnse3.com，仅需要添加dnse3.com即可
    CDNCNAME='r2wind.cn.eo.dnse3.com'
    # Token 腾讯云HTTPDNS Token，可前往https://console.cloud.tencent.com/httpdns/configure 获取
    # 如您下方HTTPDNS地址修改成了http://119.29.29.29/d，请留空
    Token=''
    # SecretId请替换为自己的腾讯云SecretId
    SecretId=''
    # SecretKey请替换为自己的腾讯云SecretKey
    SecretKey=''
    # HTTPDNS地址，该地址固定，无需修改；
    # 如您不希望额外产生使用费用，请将地址修改成http://119.29.29.29/d，并将上方Token留空
    # 请注意，使用http://119.29.29.29/d将无法保证脚本可用性
    DoH='https://119.29.29.99/d'
    # 记录类型("A"为IPv4，"AAAA"为IPv6)
    record_type='AAAA'
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
    DNS_FUJIAN_CU='218.104.128.106'
    DNS_FUJIAN_CT='218.85.152.99'
    DNS_FUJIAN_CM='211.138.151.161'
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
    DNS_JIANGXI_CU='220.248.192.12'
    DNS_JIANGXI_CT='202.101.224.69'
    DNS_JIANGXI_CM='211.141.90.68'
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
    DNS_ANHUI_CU='218.104.78.2'
    DNS_ANHUI_CT='61.132.163.68'
    DNS_ANHUI_CM='211.138.180.2'
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
    # 获取 CDN 调度结果并将调度结果推送到 DNSPod
    # 东北地区
    # 辽宁
    # 辽宁联通
    # 获取辽宁联通 CDN 调度结果
    LIAONING_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_LIAONING_CU, 'token':Token})
    print(LIAONING_CU_CDN.text)
    # 解析返回结果
    ip1_LIAONING_CU= LIAONING_CU_CDN.text.split(";")[0]
    # 获取辽宁联通记录ID
    try:
        cred = credential.Credential(SecretId, SecretKey)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "dnspod.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = dnspod_client.DnspodClient(cred, "", clientProfile)
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "辽宁联通"
        }
        req.from_json_string(json.dumps(params))
        resp_LIAONING_CU_RecordId = client.DescribeRecordList(req)
        print(resp_LIAONING_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_LIAONING_CU_RecordId = json.loads(resp_LIAONING_CU_RecordId.to_json_string())
        RecordId_LIAONING_CU1 = result_LIAONING_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新辽宁联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_LIAONING_CU1,
            "RecordType": record_type,
            "RecordLine": "辽宁联通",
            "Value": ip1_LIAONING_CU
        }
        req.from_json_string(json.dumps(params))
        resp_DONGBEI_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_DONGBEI_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 辽宁电信
    # 获取辽宁电信 CDN 调度结果
    LIAONING_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_LIAONING_CT, 'token':Token})
    print(LIAONING_CT_CDN.text)
    # 解析返回结果
    ip1_LIAONING_CT= LIAONING_CT_CDN.text.split(";")[0]
    # 获取辽宁电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "辽宁电信"
        }
        req.from_json_string(json.dumps(params))
        resp_LIAONING_CT_RecordId = client.DescribeRecordList(req)
        print(resp_LIAONING_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_LIAONING_CT_RecordId = json.loads(resp_LIAONING_CT_RecordId.to_json_string())
        RecordId_LIAONING_CT1 = result_LIAONING_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新辽宁电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_LIAONING_CT1,
            "RecordType": record_type,
            "RecordLine": "辽宁电信",
            "Value": ip1_LIAONING_CT
        }
        req.from_json_string(json.dumps(params))
        resp_LIAONING_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_LIAONING_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 辽宁移动
    # 获取辽宁移动 CDN 调度结果
    LIAONING_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_LIAONING_CM, 'token':Token})
    print(LIAONING_CM_CDN.text)
    # 解析返回结果
    ip1_LIAONING_CM= LIAONING_CM_CDN.text.split(";")[0]
    # 获取辽宁移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "辽宁移动"
        }
        req.from_json_string(json.dumps(params))
        resp_LIAONING_CM_RecordId = client.DescribeRecordList(req)
        print(resp_LIAONING_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_LIAONING_CM_RecordId = json.loads(resp_LIAONING_CM_RecordId.to_json_string())
        RecordId_LIAONING_CM1 = result_LIAONING_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新辽宁移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_LIAONING_CM1,
            "RecordType": record_type,
            "RecordLine": "辽宁移动",
            "Value": ip1_LIAONING_CM
        }
        req.from_json_string(json.dumps(params))
        resp_LIAONING_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_LIAONING_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 吉林
    # 吉林联通
    # 获取吉林联通 CDN 调度结果
    JILIN_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_JILIN_CU, 'token':Token})
    print(JILIN_CU_CDN.text)
    # 解析返回结果
    ip1_JILIN_CU= JILIN_CU_CDN.text.split(";")[0]
    # 获取吉林联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "吉林联通"
        }
        req.from_json_string(json.dumps(params))
        resp_JILIN_CU_RecordId = client.DescribeRecordList(req)
        print(resp_JILIN_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_JILIN_CU_RecordId = json.loads(resp_JILIN_CU_RecordId.to_json_string())
        RecordId_JILIN_CU1 = result_JILIN_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新吉林联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_JILIN_CU1,
            "RecordType": record_type,
            "RecordLine": "吉林联通",
            "Value": ip1_JILIN_CU
        }
        req.from_json_string(json.dumps(params))
        resp_JILIN_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_JILIN_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 吉林电信
    # 获取吉林电信 CDN 调度结果
    JILIN_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_JILIN_CT, 'token':Token})
    print(JILIN_CT_CDN.text)
    # 解析返回结果
    ip1_JILIN_CT= JILIN_CT_CDN.text.split(";")[0]
    # 获取吉林电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "吉林电信"
        }
        req.from_json_string(json.dumps(params))
        resp_JILIN_CT_RecordId = client.DescribeRecordList(req)
        print(resp_JILIN_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_JILIN_CT_RecordId = json.loads(resp_JILIN_CT_RecordId.to_json_string())
        RecordId_JILIN_CT1 = result_JILIN_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新吉林电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_JILIN_CT1,
            "RecordType": record_type,
            "RecordLine": "吉林电信",
            "Value": ip1_JILIN_CT
        }
        req.from_json_string(json.dumps(params))
        resp_JILIN_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_JILIN_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 吉林移动
    # 获取吉林移动 CDN 调度结果
    JILIN_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_JILIN_CM, 'token':Token})
    print(JILIN_CM_CDN.text)
    # 解析返回结果
    ip1_JILIN_CM= JILIN_CM_CDN.text.split(";")[0]
    # 获取吉林移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "吉林移动"
        }
        req.from_json_string(json.dumps(params))
        resp_JILIN_CM_RecordId = client.DescribeRecordList(req)
        print(resp_JILIN_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_JILIN_CM_RecordId = json.loads(resp_JILIN_CM_RecordId.to_json_string())
        RecordId_JILIN_CM1 = result_JILIN_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新吉林移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_JILIN_CM1,
            "RecordType": record_type,
            "RecordLine": "吉林移动",
            "Value": ip1_JILIN_CM
        }
        req.from_json_string(json.dumps(params))
        resp_JILIN_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_JILIN_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 黑龙江
    # 黑龙江联通
    # 获取黑龙江联通 CDN 调度结果
    HEILONGJIANG_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HEILONGJIANG_CU, 'token':Token})
    print(HEILONGJIANG_CU_CDN.text)
    # 解析返回结果
    ip1_HEILONGJIANG_CU= HEILONGJIANG_CU_CDN.text.split(";")[0]
    # 获取黑龙江联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "黑龙江联通"
        }
        req.from_json_string(json.dumps(params))
        resp_HEILONGJIANG_CU_RecordId = client.DescribeRecordList(req)
        print(resp_HEILONGJIANG_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HEILONGJIANG_CU_RecordId = json.loads(resp_HEILONGJIANG_CU_RecordId.to_json_string())
        RecordId_HEILONGJIANG_CU1 = result_HEILONGJIANG_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新黑龙江联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_HEILONGJIANG_CU1,
            "RecordType": record_type,
            "RecordLine": "黑龙江联通",
            "Value": ip1_HEILONGJIANG_CU
        }
        req.from_json_string(json.dumps(params))
        resp_HEILONGJIANG_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_HEILONGJIANG_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 黑龙江电信
    # 获取黑龙江电信 CDN 调度结果
    HEILONGJIANG_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HEILONGJIANG_CT, 'token':Token})
    print(HEILONGJIANG_CT_CDN.text)
    # 解析返回结果
    ip1_HEILONGJIANG_CT= HEILONGJIANG_CT_CDN.text.split(";")[0]
    # 获取黑龙江电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "黑龙江电信"
        }
        req.from_json_string(json.dumps(params))
        resp_HEILONGJIANG_CT_RecordId = client.DescribeRecordList(req)
        print(resp_HEILONGJIANG_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HEILONGJIANG_CT_RecordId = json.loads(resp_HEILONGJIANG_CT_RecordId.to_json_string())
        RecordId_HEILONGJIANG_CT1 = result_HEILONGJIANG_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新黑龙江电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_HEILONGJIANG_CT1,
            "RecordType": record_type,
            "RecordLine": "黑龙江电信",
            "Value": ip1_HEILONGJIANG_CT
        }
        req.from_json_string(json.dumps(params))
        resp_HEILONGJIANG_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_HEILONGJIANG_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 黑龙江移动
    # 获取黑龙江移动 CDN 调度结果
    HEILONGJIANG_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HEILONGJIANG_CM, 'token':Token})
    print(HEILONGJIANG_CM_CDN.text)
    # 解析返回结果
    ip1_HEILONGJIANG_CM= HEILONGJIANG_CM_CDN.text.split(";")[0]
    # 获取黑龙江移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "黑龙江移动"
        }
        req.from_json_string(json.dumps(params))
        resp_HEILONGJIANG_CM_RecordId = client.DescribeRecordList(req)
        print(resp_HEILONGJIANG_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HEILONGJIANG_CM_RecordId = json.loads(resp_HEILONGJIANG_CM_RecordId.to_json_string())
        RecordId_HEILONGJIANG_CM1 = result_HEILONGJIANG_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新黑龙江移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_HEILONGJIANG_CM1,
            "RecordType": record_type,
            "RecordLine": "黑龙江移动",
            "Value": ip1_HEILONGJIANG_CM
        }
        req.from_json_string(json.dumps(params))
        resp_HEILONGJIANG_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_HEILONGJIANG_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 华北地区
    # 北京
    # 北京联通
    # 获取北京联通 CDN 调度结果
    BEIJING_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_BEIJING_CU, 'token':Token})
    print(BEIJING_CU_CDN.text)
    # 解析返回结果
    ip1_BEIJING_CU= BEIJING_CU_CDN.text.split(";")[0]
    # 获取北京联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "北京联通"
        }
        req.from_json_string(json.dumps(params))
        resp_BEIJING_CU_RecordId = client.DescribeRecordList(req)
        print(resp_BEIJING_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_BEIJING_CU_RecordId = json.loads(resp_BEIJING_CU_RecordId.to_json_string())
        RecordId_BEIJING_CU1 = result_BEIJING_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新北京联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_BEIJING_CU1,
            "RecordType": record_type,
            "RecordLine": "北京联通",
            "Value": ip1_BEIJING_CU
        }
        req.from_json_string(json.dumps(params))
        resp_BEIJING_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_BEIJING_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 北京电信
    # 获取北京电信 CDN 调度结果
    BEIJING_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_BEIJING_CT, 'token':Token})
    print(BEIJING_CT_CDN.text)
    # 解析返回结果
    ip1_BEIJING_CT= BEIJING_CT_CDN.text.split(";")[0]
    # 获取北京电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "北京电信"
        }
        req.from_json_string(json.dumps(params))
        resp_BEIJING_CT_RecordId = client.DescribeRecordList(req)
        print(resp_BEIJING_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_BEIJING_CT_RecordId = json.loads(resp_BEIJING_CT_RecordId.to_json_string())
        RecordId_BEIJING_CT1 = result_BEIJING_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新北京电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_BEIJING_CT1,
            "RecordType": record_type,
            "RecordLine": "北京电信",
            "Value": ip1_BEIJING_CT
        }
        req.from_json_string(json.dumps(params))
        resp_BEIJING_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_BEIJING_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 北京移动
    # 获取北京移动 CDN 调度结果
    BEIJING_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_BEIJING_CM, 'token':Token})
    print(BEIJING_CM_CDN.text)
    # 解析返回结果
    ip1_BEIJING_CM= BEIJING_CM_CDN.text.split(";")[0]
    # 获取北京移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "北京移动"
        }
        req.from_json_string(json.dumps(params))
        resp_BEIJING_CM_RecordId = client.DescribeRecordList(req)
        print(resp_BEIJING_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_BEIJING_CM_RecordId = json.loads(resp_BEIJING_CM_RecordId.to_json_string())
        RecordId_BEIJING_CM1 = result_BEIJING_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新北京移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_BEIJING_CM1,
            "RecordType": record_type,
            "RecordLine": "北京移动",
            "Value": ip1_BEIJING_CM
        }
        req.from_json_string(json.dumps(params))
        resp_BEIJING_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_BEIJING_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 河北
    # 河北联通
    # 获取河北联通 CDN 调度结果
    HEBEI_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HEBEI_CU, 'token':Token})
    print(HEBEI_CU_CDN.text)
    # 解析返回结果
    ip1_HEBEI_CU= HEBEI_CU_CDN.text.split(";")[0]
    # 获取河北联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "河北联通"
        }
        req.from_json_string(json.dumps(params))
        resp_HEBEI_CU_RecordId = client.DescribeRecordList(req)
        print(resp_HEBEI_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HEBEI_CU_RecordId = json.loads(resp_HEBEI_CU_RecordId.to_json_string())
        RecordId_HEBEI_CU1 = result_HEBEI_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新河北联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_HEBEI_CU1,
            "RecordType": record_type,
            "RecordLine": "河北联通",
            "Value": ip1_HEBEI_CU
        }
        req.from_json_string(json.dumps(params))
        resp_HEBEI_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_HEBEI_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 河北电信
    # 获取河北电信 CDN 调度结果
    HEBEI_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HEBEI_CT, 'token':Token})
    print(HEBEI_CT_CDN.text)
    # 解析返回结果
    ip1_HEBEI_CT= HEBEI_CT_CDN.text.split(";")[0]
    # 获取河北电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "河北电信"
        }
        req.from_json_string(json.dumps(params))
        resp_HEBEI_CT_RecordId = client.DescribeRecordList(req)
        print(resp_HEBEI_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HEBEI_CT_RecordId = json.loads(resp_HEBEI_CT_RecordId.to_json_string())
        RecordId_HEBEI_CT1 = result_HEBEI_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新河北电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_HEBEI_CT1,
            "RecordType": record_type,
            "RecordLine": "河北电信",
            "Value": ip1_HEBEI_CT
        }
        req.from_json_string(json.dumps(params))
        resp_HEBEI_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_HEBEI_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 河北移动
    # 获取河北移动 CDN 调度结果
    HEBEI_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HEBEI_CM, 'token':Token})
    print(HEBEI_CM_CDN.text)
    # 解析返回结果
    ip1_HEBEI_CM= HEBEI_CM_CDN.text.split(";")[0]
    # 获取河北移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "河北移动"
        }
        req.from_json_string(json.dumps(params))
        resp_HEBEI_CM_RecordId = client.DescribeRecordList(req)
        print(resp_HEBEI_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HEBEI_CM_RecordId = json.loads(resp_HEBEI_CM_RecordId.to_json_string())
        RecordId_HEBEI_CM1 = result_HEBEI_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新河北移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_HEBEI_CM1,
            "RecordType": record_type,
            "RecordLine": "河北移动",
            "Value": ip1_HEBEI_CM
        }
        req.from_json_string(json.dumps(params))
        resp_HEBEI_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_HEBEI_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 天津
    # 天津联通
    # 获取天津联通 CDN 调度结果
    TIANJIN_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_TIANJIN_CU, 'token':Token})
    print(TIANJIN_CU_CDN.text)
    # 解析返回结果
    ip1_TIANJIN_CU= TIANJIN_CU_CDN.text.split(";")[0]
    # 获取天津联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "天津联通"
        }
        req.from_json_string(json.dumps(params))
        resp_TIANJIN_CU_RecordId = client.DescribeRecordList(req)
        print(resp_TIANJIN_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_TIANJIN_CU_RecordId = json.loads(resp_TIANJIN_CU_RecordId.to_json_string())
        RecordId_TIANJIN_CU1 = result_TIANJIN_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新天津联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_TIANJIN_CU1,
            "RecordType": record_type,
            "RecordLine": "天津联通",
            "Value": ip1_TIANJIN_CU
        }
        req.from_json_string(json.dumps(params))
        resp_TIANJIN_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_TIANJIN_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 天津电信
    # 获取天津电信 CDN 调度结果
    TIANJIN_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_TIANJIN_CT, 'token':Token})
    print(TIANJIN_CT_CDN.text)
    # 解析返回结果
    ip1_TIANJIN_CT= TIANJIN_CT_CDN.text.split(";")[0]
    # 获取天津电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "天津电信"
        }
        req.from_json_string(json.dumps(params))
        resp_TIANJIN_CT_RecordId = client.DescribeRecordList(req)
        print(resp_TIANJIN_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_TIANJIN_CT_RecordId = json.loads(resp_TIANJIN_CT_RecordId.to_json_string())
        RecordId_TIANJIN_CT1 = result_TIANJIN_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新天津电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_TIANJIN_CT1,
            "RecordType": record_type,
            "RecordLine": "天津电信",
            "Value": ip1_TIANJIN_CT
        }
        req.from_json_string(json.dumps(params))
        resp_TIANJIN_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_TIANJIN_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 天津移动
    # 获取天津移动 CDN 调度结果
    TIANJIN_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_TIANJIN_CM, 'token':Token})
    print(TIANJIN_CM_CDN.text)
    # 解析返回结果
    ip1_TIANJIN_CM= TIANJIN_CM_CDN.text.split(";")[0]
    # 获取天津移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "天津移动"
        }
        req.from_json_string(json.dumps(params))
        resp_TIANJIN_CM_RecordId = client.DescribeRecordList(req)
        print(resp_TIANJIN_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_TIANJIN_CM_RecordId = json.loads(resp_TIANJIN_CM_RecordId.to_json_string())
        RecordId_TIANJIN_CM1 = result_TIANJIN_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新天津移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_TIANJIN_CM1,
            "RecordType": record_type,
            "RecordLine": "天津移动",
            "Value": ip1_TIANJIN_CM
        }
        req.from_json_string(json.dumps(params))
        resp_TIANJIN_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_TIANJIN_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 山西
    # 山西联通
    # 获取山西联通 CDN 调度结果
    SHANXI_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHANXI_CU, 'token':Token})
    print(SHANXI_CU_CDN.text)
    # 解析返回结果
    ip1_SHANXI_CU= SHANXI_CU_CDN.text.split(";")[0]
    # 获取山西联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "山西联通"
        }
        req.from_json_string(json.dumps(params))
        resp_SHANXI_CU_RecordId = client.DescribeRecordList(req)
        print(resp_SHANXI_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHANXI_CU_RecordId = json.loads(resp_SHANXI_CU_RecordId.to_json_string())
        RecordId_SHANXI_CU1 = result_SHANXI_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新山西联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_SHANXI_CU1,
            "RecordType": record_type,
            "RecordLine": "山西联通",
            "Value": ip1_SHANXI_CU
        }
        req.from_json_string(json.dumps(params))
        resp_SHANXI_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHANXI_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 山西电信
    # 获取山西电信 CDN 调度结果
    SHANXI_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHANXI_CT, 'token':Token})
    print(SHANXI_CT_CDN.text)
    # 解析返回结果
    ip1_SHANXI_CT= SHANXI_CT_CDN.text.split(";")[0]
    # 获取山西电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "山西电信"
        }
        req.from_json_string(json.dumps(params))
        resp_SHANXI_CT_RecordId = client.DescribeRecordList(req)
        print(resp_SHANXI_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHANXI_CT_RecordId = json.loads(resp_SHANXI_CT_RecordId.to_json_string())
        RecordId_SHANXI_CT1 = result_SHANXI_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新山西电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_SHANXI_CT1,
            "RecordType": record_type,
            "RecordLine": "山西电信",
            "Value": ip1_SHANXI_CT
        }
        req.from_json_string(json.dumps(params))
        resp_SHANXI_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHANXI_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 山西移动
    # 获取山西移动 CDN 调度结果
    SHANXI_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHANXI_CM, 'token':Token})
    print(SHANXI_CM_CDN.text)
    # 解析返回结果
    ip1_SHANXI_CM= SHANXI_CM_CDN.text.split(";")[0]
    # 获取山西移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "山西移动"
        }
        req.from_json_string(json.dumps(params))
        resp_SHANXI_CM_RecordId = client.DescribeRecordList(req)
        print(resp_SHANXI_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHANXI_CM_RecordId = json.loads(resp_SHANXI_CM_RecordId.to_json_string())
        RecordId_SHANXI_CM1 = result_SHANXI_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新山西移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_SHANXI_CM1,
            "RecordType": record_type,
            "RecordLine": "山西移动",
            "Value": ip1_SHANXI_CM
        }
        req.from_json_string(json.dumps(params))
        resp_SHANXI_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHANXI_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 内蒙古
    # 内蒙古联通
    # 获取内蒙古联通 CDN 调度结果
    NEIMENGGU_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_NEIMENGGU_CU, 'token':Token})
    print(NEIMENGGU_CU_CDN.text)
    # 解析返回结果
    ip1_NEIMENGGU_CU= NEIMENGGU_CU_CDN.text.split(";")[0]
    # 获取内蒙古联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "内蒙联通"
        }
        req.from_json_string(json.dumps(params))
        resp_NEIMENGGU_CU_RecordId = client.DescribeRecordList(req)
        print(resp_NEIMENGGU_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_NEIMENGGU_CU_RecordId = json.loads(resp_NEIMENGGU_CU_RecordId.to_json_string())
        RecordId_NEIMENGGU_CU1 = result_NEIMENGGU_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新内蒙古联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_NEIMENGGU_CU1,
            "RecordType": record_type,
            "RecordLine": "内蒙联通",
            "Value": ip1_NEIMENGGU_CU
        }
        req.from_json_string(json.dumps(params))
        resp_NEIMENGGU_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_NEIMENGGU_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 内蒙古电信
    # 获取内蒙古电信 CDN 调度结果
    NEIMENGGU_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_NEIMENGGU_CT, 'token':Token})
    print(NEIMENGGU_CT_CDN.text)
    # 解析返回结果
    ip1_NEIMENGGU_CT= NEIMENGGU_CT_CDN.text.split(";")[0]
    # 获取内蒙古电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "内蒙电信"
        }
        req.from_json_string(json.dumps(params))
        resp_NEIMENGGU_CT_RecordId = client.DescribeRecordList(req)
        print(resp_NEIMENGGU_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_NEIMENGGU_CT_RecordId = json.loads(resp_NEIMENGGU_CT_RecordId.to_json_string())
        RecordId_NEIMENGGU_CT1 = result_NEIMENGGU_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新内蒙古电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_NEIMENGGU_CT1,
            "RecordType": record_type,
            "RecordLine": "内蒙电信",
            "Value": ip1_NEIMENGGU_CT
        }
        req.from_json_string(json.dumps(params))
        resp_NEIMENGGU_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_NEIMENGGU_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 内蒙古移动
    # 获取内蒙古移动 CDN 调度结果
    NEIMENGGU_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_NEIMENGGU_CM, 'token':Token})
    print(NEIMENGGU_CM_CDN.text)
    # 解析返回结果
    ip1_NEIMENGGU_CM= NEIMENGGU_CM_CDN.text.split(";")[0]
    # 获取内蒙古移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "内蒙移动"
        }
        req.from_json_string(json.dumps(params))
        resp_NEIMENGGU_CM_RecordId = client.DescribeRecordList(req)
        print(resp_NEIMENGGU_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_NEIMENGGU_CM_RecordId = json.loads(resp_NEIMENGGU_CM_RecordId.to_json_string())
        RecordId_NEIMENGGU_CM1 = result_NEIMENGGU_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新内蒙古移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_NEIMENGGU_CM1,
            "RecordType": record_type,
            "RecordLine": "内蒙移动",
            "Value": ip1_NEIMENGGU_CM
        }
        req.from_json_string(json.dumps(params))
        resp_NEIMENGGU_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_NEIMENGGU_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 华东地区
    # 江苏
    # 江苏联通
    # 获取江苏联通 CDN 调度结果
    JIANGSU_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_JIANGSU_CU, 'token':Token})
    print(JIANGSU_CU_CDN.text)
    # 解析返回结果
    ip1_JIANGSU_CU= JIANGSU_CU_CDN.text.split(";")[0]
    # 获取江苏联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "江苏联通"
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGSU_CU_RecordId = client.DescribeRecordList(req)
        print(resp_JIANGSU_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_JIANGSU_CU_RecordId = json.loads(resp_JIANGSU_CU_RecordId.to_json_string())
        RecordId_JIANGSU_CU1 = result_JIANGSU_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新江苏联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_JIANGSU_CU1,
            "RecordType": record_type,
            "RecordLine": "江苏联通",
            "Value": ip1_JIANGSU_CU
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGSU_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_JIANGSU_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 江苏电信
    # 获取江苏电信 CDN 调度结果
    JIANGSU_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_JIANGSU_CT, 'token':Token})
    print(JIANGSU_CT_CDN.text)
    # 解析返回结果
    ip1_JIANGSU_CT= JIANGSU_CT_CDN.text.split(";")[0]
    # 获取江苏电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "江苏电信"
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGSU_CT_RecordId = client.DescribeRecordList(req)
        print(resp_JIANGSU_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_JIANGSU_CT_RecordId = json.loads(resp_JIANGSU_CT_RecordId.to_json_string())
        RecordId_JIANGSU_CT1 = result_JIANGSU_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新江苏电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_JIANGSU_CT1,
            "RecordType": record_type,
            "RecordLine": "江苏电信",
            "Value": ip1_JIANGSU_CT
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGSU_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_JIANGSU_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 江苏移动
    # 获取江苏移动 CDN 调度结果
    JIANGSU_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_JIANGSU_CM, 'token':Token})
    print(JIANGSU_CM_CDN.text)
    # 解析返回结果
    ip1_JIANGSU_CM= JIANGSU_CM_CDN.text.split(";")[0]
    # 获取江苏移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "江苏移动"
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGSU_CM_RecordId = client.DescribeRecordList(req)
        print(resp_JIANGSU_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_JIANGSU_CM_RecordId = json.loads(resp_JIANGSU_CM_RecordId.to_json_string())
        RecordId_JIANGSU_CM1 = result_JIANGSU_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新江苏移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_JIANGSU_CM1,
            "RecordType": record_type,
            "RecordLine": "江苏移动",
            "Value": ip1_JIANGSU_CM
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGSU_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_JIANGSU_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 上海
    # 上海联通
    # 获取上海联通 CDN 调度结果
    SHANGHAI_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHANGHAI_CU, 'token':Token})
    print(SHANGHAI_CU_CDN.text)
    # 解析返回结果
    ip1_SHANGHAI_CU= SHANGHAI_CU_CDN.text.split(";")[0]
    # 获取上海联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "上海联通"
        }
        req.from_json_string(json.dumps(params))
        resp_SHANGHAI_CU_RecordId = client.DescribeRecordList(req)
        print(resp_SHANGHAI_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHANGHAI_CU_RecordId = json.loads(resp_SHANGHAI_CU_RecordId.to_json_string())
        RecordId_SHANGHAI_CU1 = result_SHANGHAI_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新上海联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_SHANGHAI_CU1,
            "RecordType": record_type,
            "RecordLine": "上海联通",
            "Value": ip1_SHANGHAI_CU
        }
        req.from_json_string(json.dumps(params))
        resp_SHANGHAI_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHANGHAI_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 上海电信
    # 获取上海电信 CDN 调度结果
    SHANGHAI_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHANGHAI_CT, 'token':Token})
    print(SHANGHAI_CT_CDN.text)
    # 解析返回结果
    ip1_SHANGHAI_CT= SHANGHAI_CT_CDN.text.split(";")[0]
    # 获取上海电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "上海电信"
        }
        req.from_json_string(json.dumps(params))
        resp_SHANGHAI_CT_RecordId = client.DescribeRecordList(req)
        print(resp_SHANGHAI_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHANGHAI_CT_RecordId = json.loads(resp_SHANGHAI_CT_RecordId.to_json_string())
        RecordId_SHANGHAI_CT1 = result_SHANGHAI_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新上海电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_SHANGHAI_CT1,
            "RecordType": record_type,
            "RecordLine": "上海电信",
            "Value": ip1_SHANGHAI_CT
        }
        req.from_json_string(json.dumps(params))
        resp_SHANGHAI_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHANGHAI_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 上海移动
    # 获取上海移动 CDN 调度结果
    SHANGHAI_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHANGHAI_CM, 'token':Token})
    print(SHANGHAI_CM_CDN.text)
    # 解析返回结果
    ip1_SHANGHAI_CM= SHANGHAI_CM_CDN.text.split(";")[0]
    # 获取上海移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "上海移动"
        }
        req.from_json_string(json.dumps(params))
        resp_SHANGHAI_CM_RecordId = client.DescribeRecordList(req)
        print(resp_SHANGHAI_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHANGHAI_CM_RecordId = json.loads(resp_SHANGHAI_CM_RecordId.to_json_string())
        RecordId_SHANGHAI_CM1 = result_SHANGHAI_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新上海移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_SHANGHAI_CM1,
            "RecordType": record_type,
            "RecordLine": "上海移动",
            "Value": ip1_SHANGHAI_CM
        }
        req.from_json_string(json.dumps(params))
        resp_SHANGHAI_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHANGHAI_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 浙江
    # 浙江联通
    # 获取浙江联通 CDN 调度结果
    ZHEJIANG_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_ZHEJIANG_CU, 'token':Token})
    print(ZHEJIANG_CU_CDN.text)
    # 解析返回结果
    ip1_ZHEJIANG_CU= ZHEJIANG_CU_CDN.text.split(";")[0]
    # 获取浙江联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "浙江联通"
        }
        req.from_json_string(json.dumps(params))
        resp_ZHEJIANG_CU_RecordId = client.DescribeRecordList(req)
        print(resp_ZHEJIANG_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_ZHEJIANG_CU_RecordId = json.loads(resp_ZHEJIANG_CU_RecordId.to_json_string())
        RecordId_ZHEJIANG_CU1 = result_ZHEJIANG_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新浙江联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_ZHEJIANG_CU1,
            "RecordType": record_type,
            "RecordLine": "浙江联通",
            "Value": ip1_ZHEJIANG_CU
        }
        req.from_json_string(json.dumps(params))
        resp_ZHEJIANG_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_ZHEJIANG_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 浙江电信
    # 获取浙江电信 CDN 调度结果
    ZHEJIANG_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_ZHEJIANG_CT, 'token':Token})
    print(ZHEJIANG_CT_CDN.text)
    # 解析返回结果
    ip1_ZHEJIANG_CT= ZHEJIANG_CT_CDN.text.split(";")[0]
    # 获取浙江电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "浙江电信"
        }
        req.from_json_string(json.dumps(params))
        resp_ZHEJIANG_CT_RecordId = client.DescribeRecordList(req)
        print(resp_ZHEJIANG_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_ZHEJIANG_CT_RecordId = json.loads(resp_ZHEJIANG_CT_RecordId.to_json_string())
        RecordId_ZHEJIANG_CT1 = result_ZHEJIANG_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新浙江电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_ZHEJIANG_CT1,
            "RecordType": record_type,
            "RecordLine": "浙江电信",
            "Value": ip1_ZHEJIANG_CT
        }
        req.from_json_string(json.dumps(params))
        resp_ZHEJIANG_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_ZHEJIANG_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 浙江移动
    # 获取浙江移动 CDN 调度结果
    ZHEJIANG_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_ZHEJIANG_CM, 'token':Token})
    print(ZHEJIANG_CM_CDN.text)
    # 解析返回结果
    ip1_ZHEJIANG_CM= ZHEJIANG_CM_CDN.text.split(";")[0]
    # 获取浙江移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "浙江移动"
        }
        req.from_json_string(json.dumps(params))
        resp_ZHEJIANG_CM_RecordId = client.DescribeRecordList(req)
        print(resp_ZHEJIANG_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_ZHEJIANG_CM_RecordId = json.loads(resp_ZHEJIANG_CM_RecordId.to_json_string())
        RecordId_ZHEJIANG_CM1 = result_ZHEJIANG_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新浙江移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_ZHEJIANG_CM1,
            "RecordType": record_type,
            "RecordLine": "浙江移动",
            "Value": ip1_ZHEJIANG_CM
        }
        req.from_json_string(json.dumps(params))
        resp_ZHEJIANG_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_ZHEJIANG_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 安徽
    # 安徽联通
    # 获取安徽联通 CDN 调度结果
    ANHUI_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_ANHUI_CU, 'token':Token})
    print(ANHUI_CU_CDN.text)
    # 解析返回结果
    ip1_ANHUI_CU= ANHUI_CU_CDN.text.split(";")[0]
    # 获取安徽联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "安徽联通"
        }
        req.from_json_string(json.dumps(params))
        resp_ANHUI_CU_RecordId = client.DescribeRecordList(req)
        print(resp_ANHUI_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_ANHUI_CU_RecordId = json.loads(resp_ANHUI_CU_RecordId.to_json_string())
        RecordId_ANHUI_CU1 = result_ANHUI_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新安徽联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_ANHUI_CU1,
            "RecordType": record_type,
            "RecordLine": "安徽联通",
            "Value": ip1_ANHUI_CU
        }
        req.from_json_string(json.dumps(params))
        resp_ANHUI_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_ANHUI_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 安徽电信
    # 获取安徽电信 CDN 调度结果
    ANHUI_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_ANHUI_CT, 'token':Token})
    print(ANHUI_CT_CDN.text)
    # 解析返回结果
    ip1_ANHUI_CT= ANHUI_CT_CDN.text.split(";")[0]
    # 获取安徽电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "安徽电信"
        }
        req.from_json_string(json.dumps(params))
        resp_ANHUI_CT_RecordId = client.DescribeRecordList(req)
        print(resp_ANHUI_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_ANHUI_CT_RecordId = json.loads(resp_ANHUI_CT_RecordId.to_json_string())
        RecordId_ANHUI_CT1 = result_ANHUI_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新安徽电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_ANHUI_CT1,
            "RecordType": record_type,
            "RecordLine": "安徽电信",
            "Value": ip1_ANHUI_CT
        }
        req.from_json_string(json.dumps(params))
        resp_ANHUI_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_ANHUI_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 安徽移动
    # 获取安徽移动 CDN 调度结果
    ANHUI_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_ANHUI_CM, 'token':Token})
    print(ANHUI_CM_CDN.text)
    # 解析返回结果
    ip1_ANHUI_CM= ANHUI_CM_CDN.text.split(";")[0]
    # 获取安徽移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "安徽移动"
        }
        req.from_json_string(json.dumps(params))
        resp_ANHUI_CM_RecordId = client.DescribeRecordList(req)
        print(resp_ANHUI_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_ANHUI_CM_RecordId = json.loads(resp_ANHUI_CM_RecordId.to_json_string())
        RecordId_ANHUI_CM1 = result_ANHUI_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新安徽移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_ANHUI_CM1,
            "RecordType": record_type,
            "RecordLine": "安徽移动",
            "Value": ip1_ANHUI_CM
        }
        req.from_json_string(json.dumps(params))
        resp_ANHUI_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_ANHUI_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 福建
    # 福建联通
    # 获取福建联通 CDN 调度结果
    FUJIAN_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_FUJIAN_CU, 'token':Token})
    print(FUJIAN_CU_CDN.text)
    # 解析返回结果
    ip1_FUJIAN_CU= FUJIAN_CU_CDN.text.split(";")[0]
    # 获取福建联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "福建联通"
        }
        req.from_json_string(json.dumps(params))
        resp_FUJIAN_CU_RecordId = client.DescribeRecordList(req)
        print(resp_FUJIAN_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_FUJIAN_CU_RecordId = json.loads(resp_FUJIAN_CU_RecordId.to_json_string())
        RecordId_FUJIAN_CU1 = result_FUJIAN_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新福建联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_FUJIAN_CU1,
            "RecordType": record_type,
            "RecordLine": "福建联通",
            "Value": ip1_FUJIAN_CU
        }
        req.from_json_string(json.dumps(params))
        resp_FUJIAN_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_FUJIAN_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 福建电信
    # 获取福建电信 CDN 调度结果
    FUJIAN_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_FUJIAN_CT, 'token':Token})
    print(FUJIAN_CT_CDN.text)
    # 解析返回结果
    ip1_FUJIAN_CT= FUJIAN_CT_CDN.text.split(";")[0]
    # 获取福建电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "福建电信"
        }
        req.from_json_string(json.dumps(params))
        resp_FUJIAN_CT_RecordId = client.DescribeRecordList(req)
        print(resp_FUJIAN_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_FUJIAN_CT_RecordId = json.loads(resp_FUJIAN_CT_RecordId.to_json_string())
        RecordId_FUJIAN_CT1 = result_FUJIAN_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新福建电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_FUJIAN_CT1,
            "RecordType": record_type,
            "RecordLine": "福建电信",
            "Value": ip1_FUJIAN_CT
        }
        req.from_json_string(json.dumps(params))
        resp_FUJIAN_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_FUJIAN_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 福建移动
    # 获取福建移动 CDN 调度结果
    FUJIAN_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_FUJIAN_CM, 'token':Token})
    print(FUJIAN_CM_CDN.text)
    # 解析返回结果
    ip1_FUJIAN_CM= FUJIAN_CM_CDN.text.split(";")[0]
    # 获取福建移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "福建移动"
        }
        req.from_json_string(json.dumps(params))
        resp_FUJIAN_CM_RecordId = client.DescribeRecordList(req)
        print(resp_FUJIAN_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_FUJIAN_CM_RecordId = json.loads(resp_FUJIAN_CM_RecordId.to_json_string())
        RecordId_FUJIAN_CM1 = result_FUJIAN_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新福建移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_FUJIAN_CM1,
            "RecordType": record_type,
            "RecordLine": "福建移动",
            "Value": ip1_FUJIAN_CM
        }
        req.from_json_string(json.dumps(params))
        resp_FUJIAN_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_FUJIAN_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 江西
    # 江西联通
    # 获取江西联通 CDN 调度结果
    JIANGXI_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_JIANGXI_CU, 'token':Token})
    print(JIANGXI_CU_CDN.text)
    # 解析返回结果
    ip1_JIANGXI_CU= JIANGXI_CU_CDN.text.split(";")[0]
    # 获取江西联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "江西联通"
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGXI_CU_RecordId = client.DescribeRecordList(req)
        print(resp_JIANGXI_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_JIANGXI_CU_RecordId = json.loads(resp_JIANGXI_CU_RecordId.to_json_string())
        RecordId_JIANGXI_CU1 = result_JIANGXI_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新江西联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_JIANGXI_CU1,
            "RecordType": record_type,
            "RecordLine": "江西联通",
            "Value": ip1_JIANGXI_CU
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGXI_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_JIANGXI_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 江西电信
    # 获取江西电信 CDN 调度结果
    JIANGXI_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_JIANGXI_CT, 'token':Token})
    print(JIANGXI_CT_CDN.text)
    # 解析返回结果
    ip1_JIANGXI_CT= JIANGXI_CT_CDN.text.split(";")[0]
    # 获取江西电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "江西电信"
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGXI_CT_RecordId = client.DescribeRecordList(req)
        print(resp_JIANGXI_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_JIANGXI_CT_RecordId = json.loads(resp_JIANGXI_CT_RecordId.to_json_string())
        RecordId_JIANGXI_CT1 = result_JIANGXI_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新江西电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_JIANGXI_CT1,
            "RecordType": record_type,
            "RecordLine": "江西电信",
            "Value": ip1_JIANGXI_CT
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGXI_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_JIANGXI_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 江西移动
    # 获取江西移动 CDN 调度结果
    JIANGXI_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_JIANGXI_CM, 'token':Token})
    print(JIANGXI_CM_CDN.text)
    # 解析返回结果
    ip1_JIANGXI_CM= JIANGXI_CM_CDN.text.split(";")[0]
    # 获取江西移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "江西移动"
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGXI_CM_RecordId = client.DescribeRecordList(req)
        print(resp_JIANGXI_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_JIANGXI_CM_RecordId = json.loads(resp_JIANGXI_CM_RecordId.to_json_string())
        RecordId_JIANGXI_CM1 = result_JIANGXI_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新江西移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_JIANGXI_CM1,
            "RecordType": record_type,
            "RecordLine": "江西移动",
            "Value": ip1_JIANGXI_CM
        }
        req.from_json_string(json.dumps(params))
        resp_JIANGXI_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_JIANGXI_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 山东
    # 山东联通
    # 获取山东联通 CDN 调度结果
    SHANDONG_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHANDONG_CU, 'token':Token})
    print(SHANDONG_CU_CDN.text)
    # 解析返回结果
    ip1_SHANDONG_CU= SHANDONG_CU_CDN.text.split(";")[0]
    # 获取山东联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "山东联通"
        }
        req.from_json_string(json.dumps(params))
        resp_SHANDONG_CU_RecordId = client.DescribeRecordList(req)
        print(resp_SHANDONG_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHANDONG_CU_RecordId = json.loads(resp_SHANDONG_CU_RecordId.to_json_string())
        RecordId_SHANDONG_CU1 = result_SHANDONG_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新山东联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_SHANDONG_CU1,
            "RecordType": record_type,
            "RecordLine": "山东联通",
            "Value": ip1_SHANDONG_CU
        }
        req.from_json_string(json.dumps(params))
        resp_SHANDONG_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHANDONG_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 山东电信
    # 获取山东电信 CDN 调度结果
    SHANDONG_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHANDONG_CT, 'token':Token})
    print(SHANDONG_CT_CDN.text)
    # 解析返回结果
    ip1_SHANDONG_CT= SHANDONG_CT_CDN.text.split(";")[0]
    # 获取山东电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "山东电信"
        }
        req.from_json_string(json.dumps(params))
        resp_SHANDONG_CT_RecordId = client.DescribeRecordList(req)
        print(resp_SHANDONG_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHANDONG_CT_RecordId = json.loads(resp_SHANDONG_CT_RecordId.to_json_string())
        RecordId_SHANDONG_CT1 = result_SHANDONG_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新山东电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_SHANDONG_CT1,
            "RecordType": record_type,
            "RecordLine": "山东电信",
            "Value": ip1_SHANDONG_CT
        }
        req.from_json_string(json.dumps(params))
        resp_SHANDONG_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHANDONG_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 山东移动
    # 获取山东移动 CDN 调度结果
    SHANDONG_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHANDONG_CM, 'token':Token})
    print(SHANDONG_CM_CDN.text)
    # 解析返回结果
    ip1_SHANDONG_CM= SHANDONG_CM_CDN.text.split(";")[0]
    # 获取山东移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "山东移动"
        }
        req.from_json_string(json.dumps(params))
        resp_SHANDONG_CM_RecordId = client.DescribeRecordList(req)
        print(resp_SHANDONG_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHANDONG_CM_RecordId = json.loads(resp_SHANDONG_CM_RecordId.to_json_string())
        RecordId_SHANDONG_CM1 = result_SHANDONG_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新山东移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_SHANDONG_CM1,
            "RecordType": record_type,
            "RecordLine": "山东移动",
            "Value": ip1_SHANDONG_CM
        }
        req.from_json_string(json.dumps(params))
        resp_SHANDONG_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHANDONG_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 华中地区
    # 河南
    # 河南联通
    # 获取河南联通 CDN 调度结果
    HENAN_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HENAN_CU, 'token':Token})
    print(HENAN_CU_CDN.text)
    # 解析返回结果
    ip1_HENAN_CU= HENAN_CU_CDN.text.split(";")[0]
    # 获取河南联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "河南联通"
        }
        req.from_json_string(json.dumps(params))
        resp_HENAN_CU_RecordId = client.DescribeRecordList(req)
        print(resp_HENAN_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HENAN_CU_RecordId = json.loads(resp_HENAN_CU_RecordId.to_json_string())
        RecordId_HENAN_CU1 = result_HENAN_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新河南联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_HENAN_CU1,
            "RecordType": record_type,
            "RecordLine": "河南联通",
            "Value": ip1_HENAN_CU
        }
        req.from_json_string(json.dumps(params))
        resp_HENAN_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_HENAN_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 河南电信
    # 获取河南电信 CDN 调度结果
    HENAN_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HENAN_CT, 'token':Token})
    print(HENAN_CT_CDN.text)
    # 解析返回结果
    ip1_HENAN_CT= HENAN_CT_CDN.text.split(";")[0]
    # 获取河南电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "河南电信"
        }
        req.from_json_string(json.dumps(params))
        resp_HENAN_CT_RecordId = client.DescribeRecordList(req)
        print(resp_HENAN_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HENAN_CT_RecordId = json.loads(resp_HENAN_CT_RecordId.to_json_string())
        RecordId_HENAN_CT1 = result_HENAN_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新河南电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_HENAN_CT1,
            "RecordType": record_type,
            "RecordLine": "河南电信",
            "Value": ip1_HENAN_CT
        }
        req.from_json_string(json.dumps(params))
        resp_HENAN_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_HENAN_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 河南移动
    # 获取河南移动 CDN 调度结果
    HENAN_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HENAN_CM, 'token':Token})
    print(HENAN_CM_CDN.text)
    # 解析返回结果
    ip1_HENAN_CM= HENAN_CM_CDN.text.split(";")[0]
    # 获取河南移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "河南移动"
        }
        req.from_json_string(json.dumps(params))
        resp_HENAN_CM_RecordId = client.DescribeRecordList(req)
        print(resp_HENAN_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HENAN_CM_RecordId = json.loads(resp_HENAN_CM_RecordId.to_json_string())
        RecordId_HENAN_CM1 = result_HENAN_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新河南移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_HENAN_CM1,
            "RecordType": record_type,
            "RecordLine": "河南移动",
            "Value": ip1_HENAN_CM
        }
        req.from_json_string(json.dumps(params))
        resp_HENAN_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_HENAN_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 湖北
    # 湖北联通
    # 获取湖北联通 CDN 调度结果
    HUBEI_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HUBEI_CU, 'token':Token})
    print(HUBEI_CU_CDN.text)
    # 解析返回结果
    ip1_HUBEI_CU= HUBEI_CU_CDN.text.split(";")[0]
    # 获取湖北联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "湖北联通"
        }
        req.from_json_string(json.dumps(params))
        resp_HUBEI_CU_RecordId = client.DescribeRecordList(req)
        print(resp_HUBEI_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HUBEI_CU_RecordId = json.loads(resp_HUBEI_CU_RecordId.to_json_string())
        RecordId_HUBEI_CU1 = result_HUBEI_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新湖北联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_HUBEI_CU1,
            "RecordType": record_type,
            "RecordLine": "湖北联通",
            "Value": ip1_HUBEI_CU
        }
        req.from_json_string(json.dumps(params))
        resp_HUBEI_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_HUBEI_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 湖北电信
    # 获取湖北电信 CDN 调度结果
    HUBEI_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HUBEI_CT, 'token':Token})
    print(HUBEI_CT_CDN.text)
    # 解析返回结果
    ip1_HUBEI_CT= HUBEI_CT_CDN.text.split(";")[0]
    # 获取湖北电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "湖北电信"
        }
        req.from_json_string(json.dumps(params))
        resp_HUBEI_CT_RecordId = client.DescribeRecordList(req)
        print(resp_HUBEI_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HUBEI_CT_RecordId = json.loads(resp_HUBEI_CT_RecordId.to_json_string())
        RecordId_HUBEI_CT1 = result_HUBEI_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新湖北电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_HUBEI_CT1,
            "RecordType": record_type,
            "RecordLine": "湖北电信",
            "Value": ip1_HUBEI_CT
        }
        req.from_json_string(json.dumps(params))
        resp_HUBEI_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_HUBEI_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 湖北移动
    # 获取湖北移动 CDN 调度结果
    HUBEI_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HUBEI_CM, 'token':Token})
    print(HUBEI_CM_CDN.text)
    # 解析返回结果
    ip1_HUBEI_CM= HUBEI_CM_CDN.text.split(";")[0]
    # 获取湖北移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "湖北移动"
        }
        req.from_json_string(json.dumps(params))
        resp_HUBEI_CM_RecordId = client.DescribeRecordList(req)
        print(resp_HUBEI_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HUBEI_CM_RecordId = json.loads(resp_HUBEI_CM_RecordId.to_json_string())
        RecordId_HUBEI_CM1 = result_HUBEI_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新湖北移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_HUBEI_CM1,
            "RecordType": record_type,
            "RecordLine": "湖北移动",
            "Value": ip1_HUBEI_CM
        }
        req.from_json_string(json.dumps(params))
        resp_HUBEI_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_HUBEI_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 湖南
    # 湖南联通
    # 获取湖南联通 CDN 调度结果
    HUNAN_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HUNAN_CU, 'token':Token})
    print(HUNAN_CU_CDN.text)
    # 解析返回结果
    ip1_HUNAN_CU= HUNAN_CU_CDN.text.split(";")[0]
    # 获取湖南联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "湖南联通"
        }
        req.from_json_string(json.dumps(params))
        resp_HUNAN_CU_RecordId = client.DescribeRecordList(req)
        print(resp_HUNAN_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HUNAN_CU_RecordId = json.loads(resp_HUNAN_CU_RecordId.to_json_string())
        RecordId_HUNAN_CU1 = result_HUNAN_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新湖南联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_HUNAN_CU1,
            "RecordType": record_type,
            "RecordLine": "湖南联通",
            "Value": ip1_HUNAN_CU
        }
        req.from_json_string(json.dumps(params))
        resp_HUNAN_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_HUNAN_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 湖南电信
    # 获取湖南电信 CDN 调度结果
    HUNAN_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HUNAN_CT, 'token':Token})
    print(HUNAN_CT_CDN.text)
    # 解析返回结果
    ip1_HUNAN_CT= HUNAN_CT_CDN.text.split(";")[0]
    # 获取湖南电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "湖南电信"
        }
        req.from_json_string(json.dumps(params))
        resp_HUNAN_CT_RecordId = client.DescribeRecordList(req)
        print(resp_HUNAN_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HUNAN_CT_RecordId = json.loads(resp_HUNAN_CT_RecordId.to_json_string())
        RecordId_HUNAN_CT1 = result_HUNAN_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新湖南电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_HUNAN_CT1,
            "RecordType": record_type,
            "RecordLine": "湖南电信",
            "Value": ip1_HUNAN_CT
        }
        req.from_json_string(json.dumps(params))
        resp_HUNAN_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_HUNAN_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 湖南移动
    # 获取湖南移动 CDN 调度结果
    HUNAN_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HUNAN_CM, 'token':Token})
    print(HUNAN_CM_CDN.text)
    # 解析返回结果
    ip1_HUNAN_CM= HUNAN_CM_CDN.text.split(";")[0]
    # 获取湖南移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "湖南移动"
        }
        req.from_json_string(json.dumps(params))
        resp_HUNAN_CM_RecordId = client.DescribeRecordList(req)
        print(resp_HUNAN_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HUNAN_CM_RecordId = json.loads(resp_HUNAN_CM_RecordId.to_json_string())
        RecordId_HUNAN_CM1 = result_HUNAN_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新湖南移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_HUNAN_CM1,
            "RecordType": record_type,
            "RecordLine": "湖南移动",
            "Value": ip1_HUNAN_CM
        }
        req.from_json_string(json.dumps(params))
        resp_HUNAN_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_HUNAN_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 华南地区
    # 广东
    # 广东联通
    # 获取广东联通 CDN 调度结果
    GUANGDONG_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GUANGDONG_CU, 'token':Token})
    print(GUANGDONG_CU_CDN.text)
    # 解析返回结果
    ip1_GUANGDONG_CU= GUANGDONG_CU_CDN.text.split(";")[0]
    # 获取广东联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "广东联通"
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGDONG_CU_RecordId = client.DescribeRecordList(req)
        print(resp_GUANGDONG_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GUANGDONG_CU_RecordId = json.loads(resp_GUANGDONG_CU_RecordId.to_json_string())
        RecordId_GUANGDONG_CU1 = result_GUANGDONG_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新广东联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_GUANGDONG_CU1,
            "RecordType": record_type,
            "RecordLine": "广东联通",
            "Value": ip1_GUANGDONG_CU
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGDONG_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_GUANGDONG_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 广东电信
    # 获取广东电信 CDN 调度结果
    GUANGDONG_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GUANGDONG_CT, 'token':Token})
    print(GUANGDONG_CT_CDN.text)
    # 解析返回结果
    ip1_GUANGDONG_CT= GUANGDONG_CT_CDN.text.split(";")[0]
    # 获取广东电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "广东电信"
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGDONG_CT_RecordId = client.DescribeRecordList(req)
        print(resp_GUANGDONG_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GUANGDONG_CT_RecordId = json.loads(resp_GUANGDONG_CT_RecordId.to_json_string())
        RecordId_GUANGDONG_CT1 = result_GUANGDONG_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新广东电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_GUANGDONG_CT1,
            "RecordType": record_type,
            "RecordLine": "广东电信",
            "Value": ip1_GUANGDONG_CT
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGDONG_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_GUANGDONG_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 广东移动
    # 获取广东移动 CDN 调度结果
    GUANGDONG_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GUANGDONG_CM, 'token':Token})
    print(GUANGDONG_CM_CDN.text)
    # 解析返回结果
    ip1_GUANGDONG_CM= GUANGDONG_CM_CDN.text.split(";")[0]
    # 获取广东移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "广东移动"
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGDONG_CM_RecordId = client.DescribeRecordList(req)
        print(resp_GUANGDONG_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GUANGDONG_CM_RecordId = json.loads(resp_GUANGDONG_CM_RecordId.to_json_string())
        RecordId_GUANGDONG_CM1 = result_GUANGDONG_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新广东移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_GUANGDONG_CM1,
            "RecordType": record_type,
            "RecordLine": "广东移动",
            "Value": ip1_GUANGDONG_CM
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGDONG_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_GUANGDONG_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 广西
    # 广西联通
    # 获取广西联通 CDN 调度结果
    GUANGXI_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GUANGXI_CU, 'token':Token})
    print(GUANGXI_CU_CDN.text)
    # 解析返回结果
    ip1_GUANGXI_CU= GUANGXI_CU_CDN.text.split(";")[0]
    # 获取广西联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "广西联通"
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGXI_CU_RecordId = client.DescribeRecordList(req)
        print(resp_GUANGXI_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GUANGXI_CU_RecordId = json.loads(resp_GUANGXI_CU_RecordId.to_json_string())
        RecordId_GUANGXI_CU1 = result_GUANGXI_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新广西联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId": RecordId_GUANGXI_CU1,
            "RecordType": record_type,
            "RecordLine": "广西联通",
            "Value": ip1_GUANGXI_CU
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGXI_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_GUANGXI_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 广西电信
    # 获取广西电信 CDN 调度结果
    GUANGXI_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GUANGXI_CT, 'token':Token})
    print(GUANGXI_CT_CDN.text)
    # 解析返回结果
    ip1_GUANGXI_CT= GUANGXI_CT_CDN.text.split(";")[0]
    # 获取广西电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "广西电信"
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGXI_CT_RecordId = client.DescribeRecordList(req)
        print(resp_GUANGXI_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GUANGXI_CT_RecordId = json.loads(resp_GUANGXI_CT_RecordId.to_json_string())
        RecordId_GUANGXI_CT1 = result_GUANGXI_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新广西电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_GUANGXI_CT1,
            "RecordType": record_type,
            "RecordLine": "广西电信",
            "Value": ip1_GUANGXI_CT
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGXI_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_GUANGXI_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 广西移动
    # 获取广西移动 CDN 调度结果
    GUANGXI_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GUANGXI_CM, 'token':Token})
    print(GUANGXI_CM_CDN.text)
    # 解析返回结果
    ip1_GUANGXI_CM= GUANGXI_CM_CDN.text.split(";")[0]
    # 获取广西移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "广西移动"
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGXI_CM_RecordId = client.DescribeRecordList(req)
        print(resp_GUANGXI_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GUANGXI_CM_RecordId = json.loads(resp_GUANGXI_CM_RecordId.to_json_string())
        RecordId_GUANGXI_CM1 = result_GUANGXI_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新广西移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_GUANGXI_CM1,
            "RecordType": record_type,
            "RecordLine": "广西移动",
            "Value": ip1_GUANGXI_CM
        }
        req.from_json_string(json.dumps(params))
        resp_GUANGXI_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_GUANGXI_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 海南
    # 海南联通
    # 获取海南联通 CDN 调度结果
    HAINAN_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HAINAN_CU, 'token':Token})
    print(HAINAN_CU_CDN.text)
    # 解析返回结果
    ip1_HAINAN_CU= HAINAN_CU_CDN.text.split(";")[0]
    # 获取海南联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "海南联通"
        }
        req.from_json_string(json.dumps(params))
        resp_HAINAN_CU_RecordId = client.DescribeRecordList(req)
        print(resp_HAINAN_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HAINAN_CU_RecordId = json.loads(resp_HAINAN_CU_RecordId.to_json_string())
        RecordId_HAINAN_CU1 = result_HAINAN_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新海南联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_HAINAN_CU1,
            "RecordType": record_type,
            "RecordLine": "海南联通",
            "Value": ip1_HAINAN_CU
        }
        req.from_json_string(json.dumps(params))
        resp_HAINAN_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_HAINAN_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 海南电信
    # 获取海南电信 CDN 调度结果
    HAINAN_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HAINAN_CT, 'token':Token})
    print(HAINAN_CT_CDN.text)
    # 解析返回结果
    ip1_HAINAN_CT= HAINAN_CT_CDN.text.split(";")[0]
    # 获取海南电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "海南电信"
        }
        req.from_json_string(json.dumps(params))
        resp_HAINAN_CT_RecordId = client.DescribeRecordList(req)
        print(resp_HAINAN_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HAINAN_CT_RecordId = json.loads(resp_HAINAN_CT_RecordId.to_json_string())
        RecordId_HAINAN_CT1 = result_HAINAN_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新海南电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_HAINAN_CT1,
            "RecordType": record_type,
            "RecordLine": "海南电信",
            "Value": ip1_HAINAN_CT
        }
        req.from_json_string(json.dumps(params))
        resp_HAINAN_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_HAINAN_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 海南移动
    # 获取海南移动 CDN 调度结果
    HAINAN_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_HAINAN_CM, 'token':Token})
    print(HAINAN_CM_CDN.text)
    # 解析返回结果
    ip1_HAINAN_CM= HAINAN_CM_CDN.text.split(";")[0]
    # 获取海南移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "海南移动"
        }
        req.from_json_string(json.dumps(params))
        resp_HAINAN_CM_RecordId = client.DescribeRecordList(req)
        print(resp_HAINAN_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_HAINAN_CM_RecordId = json.loads(resp_HAINAN_CM_RecordId.to_json_string())
        RecordId_HAINAN_CM1 = result_HAINAN_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新海南移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_HAINAN_CM1,
            "RecordType": record_type,
            "RecordLine": "海南移动",
            "Value": ip1_HAINAN_CM
        }
        req.from_json_string(json.dumps(params))
        resp_HAINAN_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_HAINAN_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 西南地区
    # 四川
    # 四川联通
    # 获取四川联通 CDN 调度结果
    SICHUAN_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SICHUAN_CU, 'token':Token})
    print(SICHUAN_CU_CDN.text)
    # 解析返回结果
    ip1_SICHUAN_CU= SICHUAN_CU_CDN.text.split(";")[0]
    # 获取四川联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "四川联通"
        }
        req.from_json_string(json.dumps(params))
        resp_SICHUAN_CU_RecordId = client.DescribeRecordList(req)
        print(resp_SICHUAN_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SICHUAN_CU_RecordId = json.loads(resp_SICHUAN_CU_RecordId.to_json_string())
        RecordId_SICHUAN_CU1 = result_SICHUAN_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新四川联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain ,
            "RecordId": RecordId_SICHUAN_CU1,
            "RecordType": record_type,
            "RecordLine": "四川联通",
            "Value": ip1_SICHUAN_CU
        }
        req.from_json_string(json.dumps(params))
        resp_SICHUAN_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_SICHUAN_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 四川电信
    # 获取四川电信 CDN 调度结果
    SICHUAN_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SICHUAN_CT, 'token':Token})
    print(SICHUAN_CT_CDN.text)
    # 解析返回结果
    ip1_SICHUAN_CT= SICHUAN_CT_CDN.text.split(";")[0]
    # 获取四川电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "四川电信"
        }
        req.from_json_string(json.dumps(params))
        resp_SICHUAN_CT_RecordId = client.DescribeRecordList(req)
        print(resp_SICHUAN_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SICHUAN_CT_RecordId = json.loads(resp_SICHUAN_CT_RecordId.to_json_string())
        RecordId_SICHUAN_CT1 = result_SICHUAN_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新四川电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_SICHUAN_CT1,
            "RecordType": record_type,
            "RecordLine": "四川电信",
            "Value": ip1_SICHUAN_CT
        }
        req.from_json_string(json.dumps(params))
        resp_SICHUAN_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_SICHUAN_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 四川移动
    # 获取四川移动 CDN 调度结果
    SICHUAN_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SICHUAN_CM, 'token':Token})
    print(SICHUAN_CM_CDN.text)
    # 解析返回结果
    ip1_SICHUAN_CM= SICHUAN_CM_CDN.text.split(";")[0]
    # 获取四川移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "四川移动"
        }
        req.from_json_string(json.dumps(params))
        resp_SICHUAN_CM_RecordId = client.DescribeRecordList(req)
        print(resp_SICHUAN_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SICHUAN_CM_RecordId = json.loads(resp_SICHUAN_CM_RecordId.to_json_string())
        RecordId_SICHUAN_CM1 = result_SICHUAN_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新四川移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_SICHUAN_CM1,
            "RecordType": record_type,
            "RecordLine": "四川移动",
            "Value": ip1_SICHUAN_CM
        }
        req.from_json_string(json.dumps(params))
        resp_SICHUAN_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_SICHUAN_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 西藏
    # 西藏联通
    # 获取西藏联通 CDN 调度结果
    XIZANG_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_XIZANG_CU, 'token':Token})
    print(XIZANG_CU_CDN.text)
    # 解析返回结果
    ip1_XIZANG_CU= XIZANG_CU_CDN.text.split(";")[0]
    # 获取西藏联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "西藏联通"
        }
        req.from_json_string(json.dumps(params))
        resp_XIZANG_CU_RecordId = client.DescribeRecordList(req)
        print(resp_XIZANG_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_XIZANG_CU_RecordId = json.loads(resp_XIZANG_CU_RecordId.to_json_string())
        RecordId_XIZANG_CU1 = result_XIZANG_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新西藏联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId": RecordId_XIZANG_CU1,
            "RecordType": record_type,
            "RecordLine": "西藏联通",
            "Value": ip1_XIZANG_CU
        }
        req.from_json_string(json.dumps(params))
        resp_XIZANG_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_XIZANG_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 西藏电信
    # 获取西藏电信 CDN 调度结果
    XIZANG_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_XIZANG_CT, 'token':Token})
    print(XIZANG_CT_CDN.text)
    # 解析返回结果
    ip1_XIZANG_CT= XIZANG_CT_CDN.text.split(";")[0]
    # 获取西藏电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "西藏电信"
        }
        req.from_json_string(json.dumps(params))
        resp_XIZANG_CT_RecordId = client.DescribeRecordList(req)
        print(resp_XIZANG_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_XIZANG_CT_RecordId = json.loads(resp_XIZANG_CT_RecordId.to_json_string())
        RecordId_XIZANG_CT1 = result_XIZANG_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新西藏电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_XIZANG_CT1,
            "RecordType": record_type,
            "RecordLine": "西藏电信",
            "Value": ip1_XIZANG_CT
        }
        req.from_json_string(json.dumps(params))
        resp_XIZANG_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_XIZANG_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 西藏移动
    # 获取西藏移动 CDN 调度结果
    XIZANG_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_XIZANG_CM, 'token':Token})
    print(XIZANG_CM_CDN.text)
    # 解析返回结果
    ip1_XIZANG_CM= XIZANG_CM_CDN.text.split(";")[0]
    # 获取西藏移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "西藏移动"
        }
        req.from_json_string(json.dumps(params))
        resp_XIZANG_CM_RecordId = client.DescribeRecordList(req)
        print(resp_XIZANG_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_XIZANG_CM_RecordId = json.loads(resp_XIZANG_CM_RecordId.to_json_string())
        RecordId_XIZANG_CM1 = result_XIZANG_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新西藏移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_XIZANG_CM1,
            "RecordType": record_type,
            "RecordLine": "西藏移动",
            "Value": ip1_XIZANG_CM
        }
        req.from_json_string(json.dumps(params))
        resp_XIZANG_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_XIZANG_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 重庆
    # 重庆联通
    # 获取重庆联通 CDN 调度结果
    CHONGQING_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_CHONGQING_CU, 'token':Token})
    print(CHONGQING_CU_CDN.text)
    # 解析返回结果
    ip1_CHONGQING_CU= CHONGQING_CU_CDN.text.split(";")[0]
    # 获取重庆联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "重庆联通"
        }
        req.from_json_string(json.dumps(params))
        resp_CHONGQING_CU_RecordId = client.DescribeRecordList(req)
        print(resp_CHONGQING_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_CHONGQING_CU_RecordId = json.loads(resp_CHONGQING_CU_RecordId.to_json_string())
        RecordId_CHONGQING_CU1 = result_CHONGQING_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新重庆联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_CHONGQING_CU1,
            "RecordType": record_type,
            "RecordLine": "重庆联通",
            "Value": ip1_CHONGQING_CU
        }
        req.from_json_string(json.dumps(params))
        resp_CHONGQING_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_CHONGQING_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 重庆电信
    # 获取重庆电信 CDN 调度结果
    CHONGQING_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_CHONGQING_CT, 'token':Token})
    print(CHONGQING_CT_CDN.text)
    # 解析返回结果
    ip1_CHONGQING_CT= CHONGQING_CT_CDN.text.split(";")[0]
    # 获取重庆电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "重庆电信"
        }
        req.from_json_string(json.dumps(params))
        resp_CHONGQING_CT_RecordId = client.DescribeRecordList(req)
        print(resp_CHONGQING_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_CHONGQING_CT_RecordId = json.loads(resp_CHONGQING_CT_RecordId.to_json_string())
        RecordId_CHONGQING_CT1 = result_CHONGQING_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新重庆电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_CHONGQING_CT1,
            "RecordType": record_type,
            "RecordLine": "重庆电信",
            "Value": ip1_CHONGQING_CT
        }
        req.from_json_string(json.dumps(params))
        resp_CHONGQING_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_CHONGQING_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 重庆移动
    # 获取重庆移动 CDN 调度结果
    CHONGQING_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_CHONGQING_CM, 'token':Token})
    print(CHONGQING_CM_CDN.text)
    # 解析返回结果
    ip1_CHONGQING_CM= CHONGQING_CM_CDN.text.split(";")[0]
    # 获取重庆移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "重庆移动"
        }
        req.from_json_string(json.dumps(params))
        resp_CHONGQING_CM_RecordId = client.DescribeRecordList(req)
        print(resp_CHONGQING_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_CHONGQING_CM_RecordId = json.loads(resp_CHONGQING_CM_RecordId.to_json_string())
        RecordId_CHONGQING_CM1 = result_CHONGQING_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新重庆移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_CHONGQING_CM1,
            "RecordType": record_type,
            "RecordLine": "重庆移动",
            "Value": ip1_CHONGQING_CM
        }
        req.from_json_string(json.dumps(params))
        resp_CHONGQING_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_CHONGQING_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 云南
    # 云南联通
    # 获取云南联通 CDN 调度结果
    YUNNAN_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_YUNNAN_CU, 'token':Token})
    print(YUNNAN_CU_CDN.text)
    # 解析返回结果
    ip1_YUNNAN_CU= YUNNAN_CU_CDN.text.split(";")[0]
    # 获取云南联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "云南联通"
        }
        req.from_json_string(json.dumps(params))
        resp_YUNNAN_CU_RecordId = client.DescribeRecordList(req)
        print(resp_YUNNAN_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_YUNNAN_CU_RecordId = json.loads(resp_YUNNAN_CU_RecordId.to_json_string())
        RecordId_YUNNAN_CU1 = result_YUNNAN_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新云南联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_YUNNAN_CU1,
            "RecordType": record_type,
            "RecordLine": "云南联通",
            "Value": ip1_YUNNAN_CU
        }
        req.from_json_string(json.dumps(params))
        resp_YUNNAN_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_YUNNAN_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 云南电信
    # 获取云南电信 CDN 调度结果
    YUNNAN_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_YUNNAN_CT, 'token':Token})
    print(YUNNAN_CT_CDN.text)
    # 解析返回结果
    ip1_YUNNAN_CT= YUNNAN_CT_CDN.text.split(";")[0]
    # 获取云南电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "云南电信"
        }
        req.from_json_string(json.dumps(params))
        resp_YUNNAN_CT_RecordId = client.DescribeRecordList(req)
        print(resp_YUNNAN_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_YUNNAN_CT_RecordId = json.loads(resp_YUNNAN_CT_RecordId.to_json_string())
        RecordId_YUNNAN_CT1 = result_YUNNAN_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新云南电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_YUNNAN_CT1,
            "RecordType": record_type,
            "RecordLine": "云南电信",
            "Value": ip1_YUNNAN_CT
        }
        req.from_json_string(json.dumps(params))
        resp_YUNNAN_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_YUNNAN_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 云南移动
    # 获取云南移动 CDN 调度结果
    YUNNAN_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_YUNNAN_CM, 'token':Token})
    print(YUNNAN_CM_CDN.text)
    # 解析返回结果
    ip1_YUNNAN_CM= YUNNAN_CM_CDN.text.split(";")[0]
    # 获取云南移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "云南移动"
        }
        req.from_json_string(json.dumps(params))
        resp_YUNNAN_CM_RecordId = client.DescribeRecordList(req)
        print(resp_YUNNAN_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_YUNNAN_CM_RecordId = json.loads(resp_YUNNAN_CM_RecordId.to_json_string())
        RecordId_YUNNAN_CM1 = result_YUNNAN_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新云南移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId": RecordId_YUNNAN_CM1,
            "RecordType": record_type,
            "RecordLine": "云南移动",
            "Value": ip1_YUNNAN_CM
        }
        req.from_json_string(json.dumps(params))
        resp_YUNNAN_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_YUNNAN_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 贵州
    # 贵州联通
    # 获取贵州联通 CDN 调度结果
    GUIZHOU_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GUIZHOU_CU, 'token':Token})
    print(GUIZHOU_CU_CDN.text)
    # 解析返回结果
    ip1_GUIZHOU_CU= GUIZHOU_CU_CDN.text.split(";")[0]
    # 获取贵州联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "贵州联通"
        }
        req.from_json_string(json.dumps(params))
        resp_GUIZHOU_CU_RecordId = client.DescribeRecordList(req)
        print(resp_GUIZHOU_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GUIZHOU_CU_RecordId = json.loads(resp_GUIZHOU_CU_RecordId.to_json_string())
        RecordId_GUIZHOU_CU1 = result_GUIZHOU_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新贵州联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId": RecordId_GUIZHOU_CU1,
            "RecordType": record_type,
            "RecordLine": "贵州联通",
            "Value": ip1_GUIZHOU_CU
        }
        req.from_json_string(json.dumps(params))
        resp_GUIZHOU_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_GUIZHOU_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 贵州电信
    # 获取贵州电信 CDN 调度结果
    GUIZHOU_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GUIZHOU_CT, 'token':Token})
    print(GUIZHOU_CT_CDN.text)
    # 解析返回结果
    ip1_GUIZHOU_CT= GUIZHOU_CT_CDN.text.split(";")[0]
    # 获取贵州电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "贵州电信"
        }
        req.from_json_string(json.dumps(params))
        resp_GUIZHOU_CT_RecordId = client.DescribeRecordList(req)
        print(resp_GUIZHOU_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GUIZHOU_CT_RecordId = json.loads(resp_GUIZHOU_CT_RecordId.to_json_string())
        RecordId_GUIZHOU_CT1 = result_GUIZHOU_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新贵州电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_GUIZHOU_CT1,
            "RecordType": record_type,
            "RecordLine": "贵州电信",
            "Value": ip1_GUIZHOU_CT
        }
        req.from_json_string(json.dumps(params))
        resp_GUIZHOU_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_GUIZHOU_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 贵州移动
    # 获取贵州移动 CDN 调度结果
    GUIZHOU_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GUIZHOU_CM, 'token':Token})
    print(GUIZHOU_CM_CDN.text)
    # 解析返回结果
    ip1_GUIZHOU_CM= GUIZHOU_CM_CDN.text.split(";")[0]
    # 获取贵州移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "贵州移动"
        }
        req.from_json_string(json.dumps(params))
        resp_GUIZHOU_CM_RecordId = client.DescribeRecordList(req)
        print(resp_GUIZHOU_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GUIZHOU_CM_RecordId = json.loads(resp_GUIZHOU_CM_RecordId.to_json_string())
        RecordId_GUIZHOU_CM1 = result_GUIZHOU_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新贵州移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_GUIZHOU_CM1,
            "RecordType": record_type,
            "RecordLine": "贵州移动",
            "Value": ip1_GUIZHOU_CM
        }
        req.from_json_string(json.dumps(params))
        resp_GUIZHOU_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_GUIZHOU_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 西北地区
    # 陕西
    # 陕西联通
    # 获取陕西联通 CDN 调度结果
    SHAANXI_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHAANXI_CU, 'token':Token})
    print(SHAANXI_CU_CDN.text)
    # 解析返回结果
    ip1_SHAANXI_CU= SHAANXI_CU_CDN.text.split(";")[0]
    # 获取陕西联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "陕西联通"
        }
        req.from_json_string(json.dumps(params))
        resp_SHAANXI_CU_RecordId = client.DescribeRecordList(req)
        print(resp_SHAANXI_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHAANXI_CU_RecordId = json.loads(resp_SHAANXI_CU_RecordId.to_json_string())
        RecordId_SHAANXI_CU1 = result_SHAANXI_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新陕西联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_SHAANXI_CU1,
            "RecordType": record_type,
            "RecordLine": "陕西联通",
            "Value": ip1_SHAANXI_CU
        }
        req.from_json_string(json.dumps(params))
        resp_SHAANXI_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHAANXI_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 陕西电信
    # 获取陕西电信 CDN 调度结果
    SHAANXI_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHAANXI_CT, 'token':Token})
    print(SHAANXI_CT_CDN.text)
    # 解析返回结果
    ip1_SHAANXI_CT= SHAANXI_CT_CDN.text.split(";")[0]
    # 获取陕西电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "陕西电信"
        }
        req.from_json_string(json.dumps(params))
        resp_SHAANXI_CT_RecordId = client.DescribeRecordList(req)
        print(resp_SHAANXI_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHAANXI_CT_RecordId = json.loads(resp_SHAANXI_CT_RecordId.to_json_string())
        RecordId_SHAANXI_CT1 = result_SHAANXI_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新陕西电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_SHAANXI_CT1,
            "RecordType": record_type,
            "RecordLine": "陕西电信",
            "Value": ip1_SHAANXI_CT
        }
        req.from_json_string(json.dumps(params))
        resp_SHAANXI_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHAANXI_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 陕西移动
    # 获取陕西移动 CDN 调度结果
    SHAANXI_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_SHAANXI_CM, 'token':Token})
    print(SHAANXI_CM_CDN.text)
    # 解析返回结果
    ip1_SHAANXI_CM= SHAANXI_CM_CDN.text.split(";")[0]
    # 获取陕西移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "陕西移动"
        }
        req.from_json_string(json.dumps(params))
        resp_SHAANXI_CM_RecordId = client.DescribeRecordList(req)
        print(resp_SHAANXI_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_SHAANXI_CM_RecordId = json.loads(resp_SHAANXI_CM_RecordId.to_json_string())
        RecordId_SHAANXI_CM1 = result_SHAANXI_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新陕西移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_SHAANXI_CM1,
            "RecordType": record_type,
            "RecordLine": "陕西移动",
            "Value": ip1_SHAANXI_CM
        }
        req.from_json_string(json.dumps(params))
        resp_SHAANXI_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_SHAANXI_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 甘肃
    # 甘肃联通
    # 获取甘肃联通 CDN 调度结果
    GANSU_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GANSU_CU, 'token':Token})
    print(GANSU_CU_CDN.text)
    # 解析返回结果
    ip1_GANSU_CU= GANSU_CU_CDN.text.split(";")[0]
    # 获取甘肃联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "甘肃联通"
        }
        req.from_json_string(json.dumps(params))
        resp_GANSU_CU_RecordId = client.DescribeRecordList(req)
        print(resp_GANSU_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GANSU_CU_RecordId = json.loads(resp_GANSU_CU_RecordId.to_json_string())
        RecordId_GANSU_CU1 = result_GANSU_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新甘肃联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_GANSU_CU1,
            "RecordType": record_type,
            "RecordLine": "甘肃联通",
            "Value": ip1_GANSU_CU
        }
        req.from_json_string(json.dumps(params))
        resp_GANSU_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_GANSU_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 甘肃电信
    # 获取甘肃电信 CDN 调度结果
    GANSU_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GANSU_CT, 'token':Token})
    print(GANSU_CT_CDN.text)
    # 解析返回结果
    ip1_GANSU_CT= GANSU_CT_CDN.text.split(";")[0]
    # 获取甘肃电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "甘肃电信"
        }
        req.from_json_string(json.dumps(params))
        resp_GANSU_CT_RecordId = client.DescribeRecordList(req)
        print(resp_GANSU_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GANSU_CT_RecordId = json.loads(resp_GANSU_CT_RecordId.to_json_string())
        RecordId_GANSU_CT1 = result_GANSU_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新甘肃电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_GANSU_CT1,
            "RecordType": record_type,
            "RecordLine": "甘肃电信",
            "Value": ip1_GANSU_CT
        }
        req.from_json_string(json.dumps(params))
        resp_GANSU_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_GANSU_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 甘肃移动
    # 获取甘肃移动 CDN 调度结果
    GANSU_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_GANSU_CM, 'token':Token})
    print(GANSU_CM_CDN.text)
    # 解析返回结果
    ip1_GANSU_CM= GANSU_CM_CDN.text.split(";")[0]
    # 获取甘肃移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain ,
            "RecordType": record_type,
            "RecordLine": "甘肃移动"
        }
        req.from_json_string(json.dumps(params))
        resp_GANSU_CM_RecordId = client.DescribeRecordList(req)
        print(resp_GANSU_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_GANSU_CM_RecordId = json.loads(resp_GANSU_CM_RecordId.to_json_string())
        RecordId_GANSU_CM1 = result_GANSU_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新甘肃移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_GANSU_CM1,
            "RecordType": record_type,
            "RecordLine": "甘肃移动",
            "Value": ip1_GANSU_CM
        }
        req.from_json_string(json.dumps(params))
        resp_GANSU_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_GANSU_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 新疆
    # 新疆联通
    # 获取新疆联通 CDN 调度结果
    XINJIANG_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_XINJIANG_CU, 'token':Token})
    print(XINJIANG_CU_CDN.text)
    # 解析返回结果
    ip1_XINJIANG_CU= XINJIANG_CU_CDN.text.split(";")[0]
    # 获取新疆联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "新疆联通"
        }
        req.from_json_string(json.dumps(params))
        resp_XINJIANG_CU_RecordId = client.DescribeRecordList(req)
        print(resp_XINJIANG_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_XINJIANG_CU_RecordId = json.loads(resp_XINJIANG_CU_RecordId.to_json_string())
        RecordId_XINJIANG_CU1 = result_XINJIANG_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新新疆联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_XINJIANG_CU1,
            "RecordType": record_type,
            "RecordLine": "新疆联通",
            "Value": ip1_XINJIANG_CU
        }
        req.from_json_string(json.dumps(params))
        resp_XINJIANG_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_XINJIANG_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 新疆电信
    # 获取新疆电信 CDN 调度结果
    XINJIANG_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_XINJIANG_CT, 'token':Token})
    print(XINJIANG_CT_CDN.text)
    # 解析返回结果
    ip1_XINJIANG_CT= XINJIANG_CT_CDN.text.split(";")[0]
    # 获取新疆电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "新疆电信"
        }
        req.from_json_string(json.dumps(params))
        resp_XINJIANG_CT_RecordId = client.DescribeRecordList(req)
        print(resp_XINJIANG_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_XINJIANG_CT_RecordId = json.loads(resp_XINJIANG_CT_RecordId.to_json_string())
        RecordId_XINJIANG_CT1 = result_XINJIANG_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新新疆电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_XINJIANG_CT1,
            "RecordType": record_type,
            "RecordLine": "新疆电信",
            "Value": ip1_XINJIANG_CT
        }
        req.from_json_string(json.dumps(params))
        resp_XINJIANG_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_XINJIANG_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 新疆移动
    # 获取新疆移动 CDN 调度结果
    XINJIANG_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_XINJIANG_CM, 'token':Token})
    print(XINJIANG_CM_CDN.text)
    # 解析返回结果
    ip1_XINJIANG_CM= XINJIANG_CM_CDN.text.split(";")[0]
    # 获取新疆移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "新疆移动"
        }
        req.from_json_string(json.dumps(params))
        resp_XINJIANG_CM_RecordId = client.DescribeRecordList(req)
        print(resp_XINJIANG_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_XINJIANG_CM_RecordId = json.loads(resp_XINJIANG_CM_RecordId.to_json_string())
        RecordId_XINJIANG_CM1 = result_XINJIANG_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新新疆移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_XINJIANG_CM1,
            "RecordType": record_type,
            "RecordLine": "新疆移动",
            "Value": ip1_XINJIANG_CM
        }
        req.from_json_string(json.dumps(params))
        resp_XINJIANG_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_XINJIANG_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 青海
    # 青海联通
    # 获取青海联通 CDN 调度结果
    QINGHAI_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_QINGHAI_CU, 'token':Token})
    print(QINGHAI_CU_CDN.text)
    # 解析返回结果
    ip1_QINGHAI_CU= QINGHAI_CU_CDN.text.split(";")[0]
    # 获取青海联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "青海联通"
        }
        req.from_json_string(json.dumps(params))
        resp_QINGHAI_CU_RecordId = client.DescribeRecordList(req)
        print(resp_QINGHAI_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_QINGHAI_CU_RecordId = json.loads(resp_QINGHAI_CU_RecordId.to_json_string())
        RecordId_QINGHAI_CU1 = result_QINGHAI_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新青海联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_QINGHAI_CU1,
            "RecordType": record_type,
            "RecordLine": "青海联通",
            "Value": ip1_QINGHAI_CU
        }
        req.from_json_string(json.dumps(params))
        resp_QINGHAI_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_QINGHAI_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 青海电信
    # 获取青海电信 CDN 调度结果
    QINGHAI_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_QINGHAI_CT, 'token':Token})
    print(QINGHAI_CT_CDN.text)
    # 解析返回结果
    ip1_QINGHAI_CT= QINGHAI_CT_CDN.text.split(";")[0]
    # 获取青海电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain":subdomain,
            "RecordType": record_type,
            "RecordLine": "青海电信"
        }
        req.from_json_string(json.dumps(params))
        resp_QINGHAI_CT_RecordId = client.DescribeRecordList(req)
        print(resp_QINGHAI_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_QINGHAI_CT_RecordId = json.loads(resp_QINGHAI_CT_RecordId.to_json_string())
        RecordId_QINGHAI_CT1 = result_QINGHAI_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新青海电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain,
            "RecordId":RecordId_QINGHAI_CT1,
            "RecordType": record_type,
            "RecordLine": "青海电信",
            "Value": ip1_QINGHAI_CT
        }
        req.from_json_string(json.dumps(params))
        resp_QINGHAI_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_QINGHAI_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 青海移动
    # 获取青海移动 CDN 调度结果
    QINGHAI_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_QINGHAI_CM, 'token':Token})
    print(QINGHAI_CM_CDN.text)
    # 解析返回结果
    ip1_QINGHAI_CM= QINGHAI_CM_CDN.text.split(";")[0]
    # 获取青海移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "青海移动"
        }
        req.from_json_string(json.dumps(params))
        resp_QINGHAI_CM_RecordId = client.DescribeRecordList(req)
        print(resp_QINGHAI_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_QINGHAI_CM_RecordId = json.loads(resp_QINGHAI_CM_RecordId.to_json_string())
        RecordId_QINGHAI_CM1 = result_QINGHAI_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新青海移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain":subdomain ,
            "RecordId":RecordId_QINGHAI_CM1,
            "RecordType": record_type,
            "RecordLine": "青海移动",
            "Value": ip1_QINGHAI_CM
        }
        req.from_json_string(json.dumps(params))
        resp_QINGHAI_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_QINGHAI_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 宁夏
    # 宁夏联通
    # 获取宁夏联通 CDN 调度结果
    NINGXIA_CU_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_NINGXIA_CU, 'token':Token})
    print(NINGXIA_CU_CDN.text)
    # 解析返回结果
    ip1_NINGXIA_CU= NINGXIA_CU_CDN.text.split(";")[0]
    # 获取宁夏联通记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "宁夏联通"
        }
        req.from_json_string(json.dumps(params))
        resp_NINGXIA_CU_RecordId = client.DescribeRecordList(req)
        print(resp_NINGXIA_CU_RecordId.to_json_string())
        # 将返回数据写入变量
        result_NINGXIA_CU_RecordId = json.loads(resp_NINGXIA_CU_RecordId.to_json_string())
        RecordId_NINGXIA_CU1 = result_NINGXIA_CU_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新宁夏联通记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_NINGXIA_CU1,
            "RecordType": record_type,
            "RecordLine": "宁夏联通",
            "Value": ip1_NINGXIA_CU
        }
        req.from_json_string(json.dumps(params))
        resp_NINGXIA_CU1_Modify_Record = client.ModifyRecord(req)
        print(resp_NINGXIA_CU1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 宁夏电信
    # 获取宁夏电信 CDN 调度结果
    NINGXIA_CT_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_NINGXIA_CT, 'token':Token})
    print(NINGXIA_CT_CDN.text)
    # 解析返回结果
    ip1_NINGXIA_CT= NINGXIA_CT_CDN.text.split(";")[0]
    # 获取宁夏电信记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "宁夏电信"
        }
        req.from_json_string(json.dumps(params))
        resp_NINGXIA_CT_RecordId = client.DescribeRecordList(req)
        print(resp_NINGXIA_CT_RecordId.to_json_string())
        # 将返回数据写入变量
        result_NINGXIA_CT_RecordId = json.loads(resp_NINGXIA_CT_RecordId.to_json_string())
        RecordId_NINGXIA_CT1 = result_NINGXIA_CT_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新宁夏电信记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain ,
            "RecordId": RecordId_NINGXIA_CT1,
            "RecordType": record_type,
            "RecordLine": "宁夏电信",
            "Value": ip1_NINGXIA_CT
        }
        req.from_json_string(json.dumps(params))
        resp_NINGXIA_CT1_Modify_Record = client.ModifyRecord(req)
        print(resp_NINGXIA_CT1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 宁夏移动
    # 获取宁夏移动 CDN 调度结果
    NINGXIA_CM_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_NINGXIA_CM, 'token':Token})
    print(NINGXIA_CM_CDN.text)
    # 解析返回结果
    ip1_NINGXIA_CM= NINGXIA_CM_CDN.text.split(";")[0]
    # 获取宁夏移动记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "宁夏移动"
        }
        req.from_json_string(json.dumps(params))
        resp_NINGXIA_CM_RecordId = client.DescribeRecordList(req)
        print(resp_NINGXIA_CM_RecordId.to_json_string())
        # 将返回数据写入变量
        result_NINGXIA_CM_RecordId = json.loads(resp_NINGXIA_CM_RecordId.to_json_string())
        RecordId_NINGXIA_CM1 = result_NINGXIA_CM_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新宁夏移动记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_NINGXIA_CM1,
            "RecordType": record_type,
            "RecordLine": "宁夏移动",
            "Value": ip1_NINGXIA_CM
        }
        req.from_json_string(json.dumps(params))
        resp_NINGXIA_CM1_Modify_Record = client.ModifyRecord(req)
        print(resp_NINGXIA_CM1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 教育网
    # 获取教育网 CDN 调度结果
    CERNET_CDN = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNS_JIAOYU, 'token':Token})
    print(CERNET_CDN.text)
    # 解析返回结果
    ip1_CERNET= CERNET_CDN.text.split(";")[0]
    # 获取教育网记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "教育网"
        }
        req.from_json_string(json.dumps(params))
        resp_CERNET_RecordId = client.DescribeRecordList(req)
        print(resp_CERNET_RecordId.to_json_string())
        # 将返回数据写入变量
        result_CERNET_RecordId = json.loads(resp_CERNET_RecordId.to_json_string())
        RecordId_CERNET1 = result_CERNET_RecordId['RecordList'][0]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新教育网记录
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId":RecordId_CERNET1,
            "RecordType": record_type,
            "RecordLine": "教育网",
            "Value": ip1_CERNET
        }
        req.from_json_string(json.dumps(params))
        resp_CERNET1_Modify_Record = client.ModifyRecord(req)
        print(resp_CERNET1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 默认
    # 默认线路用于覆盖其他二级运营商等上面运营商线路未覆盖的线路，选取上海电信、北京联通、广东移动的IP作为默认线路
    # 将调度结果推送到DNSPod
    # 获取默认记录ID
    try:
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain,
            "Subdomain": subdomain,
            "RecordType": record_type,
            "RecordLine": "默认"
        }
        req.from_json_string(json.dumps(params))
        resp_Default_RecordId = client.DescribeRecordList(req)
        print(resp_Default_RecordId.to_json_string())
        result_Default_RecordId = json.loads(resp_Default_RecordId.to_json_string())
        # 将返回数据写入变量
        RecordId_Default1 = result_Default_RecordId['RecordList'][0]['RecordId']
        RecordId_Default2 = result_Default_RecordId['RecordList'][1]['RecordId']
        RecordId_Default3 = result_Default_RecordId['RecordList'][2]['RecordId']
    except TencentCloudSDKException as err:
        print(err)
    # 更新默认记录
    # 更新默认记录1
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_Default1,
            "RecordType": record_type,
            "RecordLine": "默认",
            "Value": ip1_SHANGHAI_CT
        }
        req.from_json_string(json.dumps(params))
        resp_Default1_Modify_Record = client.ModifyRecord(req)
        print(resp_Default1_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 更新默认记录2
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_Default2,
            "RecordType": record_type,
            "RecordLine": "默认",
            "Value": ip1_BEIJING_CU
        }
        req.from_json_string(json.dumps(params))
        resp_Default2_Modify_Record = client.ModifyRecord(req)
        print(resp_Default2_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
    # 更新默认记录3
    try:
        req = models.ModifyRecordRequest()
        params = {
            "Domain": domain,
            "SubDomain": subdomain,
            "RecordId": RecordId_Default3,
            "RecordType": record_type,
            "RecordLine": "默认",
            "Value": ip1_GUANGDONG_CM
        }
        req.from_json_string(json.dumps(params))
        resp_Default3_Modify_Record = client.ModifyRecord(req)
        print(resp_Default3_Modify_Record.to_json_string())
    except TencentCloudSDKException as err:
        print(err)