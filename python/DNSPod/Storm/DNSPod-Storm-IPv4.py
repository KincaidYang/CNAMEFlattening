# DNSPod 拉平脚本，用于拉平根域名的CDN CNAME地址
# 本脚本基于腾讯云API，使用前请先安装SDK，pip install --upgrade tencentcloud-sdk-python
# 使用脚本前请参照说明导入记录，以及修改配置参数
# 本脚本为 HTTPDNS 版本
# 本脚本依赖于腾讯云HTTPDNS服务，使用可能会产生额外的费用
import sys
import requests,json,time
from multiprocessing.dummy import Pool
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models
if __name__ == '__main__':
    # 配置参数
    # domanin替换为自己的域名
    domain='9kr.cc'
    # sub_domain替换为自己的子域名
    subdomain='@'
    # CDNCNAME请替换为CDN提供的CNAME地址
    # 使用前请前往https://console.cloud.tencent.com/httpdns/domain 添加CNAME域名
    # 添加域名时仅需要添加主域名，如您的CNAME地址是r2wind.cn.eo.dnse3.com，仅需要添加dnse3.com即可
    CDNCNAME='9kr.cc.cdn.dnsv1.com.cn'
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
    record_type='A'
    # 使用各省运营商 DNSIP，以确保可以正常使用 ECS 协议调度
    DNSIP_List = {
        # 东北,
        "DNS_LIAONING_CU":{"ip":"202.96.64.68","name":"辽宁联通"},
        "DNS_LIAONING_CT":{"ip":"219.148.204.66","name":"辽宁电信"},
        "DNS_LIAONING_CM":{"ip":"211.137.32.178","name":"辽宁移动"},
        "DNS_JILIN_CU":{"ip":"202.98.0.68","name":"吉林联通"},
        "DNS_JILIN_CT":{"ip":"219.149.194.55","name":"吉林电信"},
        "DNS_JILIN_CM":{"ip":"211.141.16.99","name":"吉林移动"},
        "DNS_HEILONGJIANG_CU":{"ip":"202.97.224.68","name":"黑龙江联通"},
        "DNS_HEILONGJIANG_CT":{"ip":"112.100.100.100","name":"黑龙江电信"},
        "DNS_HEILONGJIANG_CM":{"ip":"211.137.241.34","name":"黑龙江移动"},
        # 华北,
        "DNS_BEIJING_CU":{"ip":"202.106.196.115","name":"北京联通"},
        "DNS_BEIJING_CT":{"ip":"219.141.136.10","name":"北京电信"},
        "DNS_BEIJING_CM":{"ip":"221.130.33.52","name":"北京移动"},
        "DNS_TIANJIN_CU":{"ip":"202.99.96.68","name":"天津联通"},
        "DNS_TIANJIN_CT":{"ip":"219.150.32.132","name":"天津电信"},
        "DNS_TIANJIN_CM":{"ip":"211.137.160.5","name":"天津移动"},
        "DNS_HEBEI_CU":{"ip":"202.99.160.68","name":"河北联通"},
        "DNS_HEBEI_CT":{"ip":"222.222.222.222","name":"河北电信"},
        "DNS_HEBEI_CM":{"ip":"211.138.13.66","name":"河北移动"},
        "DNS_SHANXI_CU":{"ip":"202.99.216.113","name":"山西联通"},
        "DNS_SHANXI_CT":{"ip":"219.149.135.188","name":"山西电信"},
        "DNS_SHANXI_CM":{"ip":"211.138.106.3","name":"山西移动"},
        "DNS_NEIMENGGU_CU":{"ip":"202.99.224.68","name":"内蒙联通"},
        "DNS_NEIMENGGU_CT":{"ip":"219.148.162.31","name":"内蒙电信"},
        "DNS_NEIMENGGU_CM":{"ip":"211.138.91.1","name":"内蒙移动"},
        # 华南,
        "DNS_HAINAN_CU":{"ip":"221.11.132.2","name":"海南联通"},
        "DNS_HAINAN_CT":{"ip":"202.100.192.68","name":"海南电信"},
        "DNS_HAINAN_CM":{"ip":"221.176.88.95","name":"海南移动"},
        "DNS_GUANGDONG_CU":{"ip":"210.21.196.6","name":"广东联通"},
        "DNS_GUANGDONG_CT":{"ip":"202.96.134.133","name":"广东电信"},
        "DNS_GUANGDONG_CM":{"ip":"211.139.163.6","name":"广东移动"},
        "DNS_GUANGXI_CU":{"ip":"221.7.128.68","name":"广西联通"},
        "DNS_GUANGXI_CT":{"ip":"202.103.225.68","name":"广西电信"},
        "DNS_GUANGXI_CM":{"ip":"211.138.245.180","name":"广西移动"},
        "DNS_FUJIAN_CU":{"ip":"218.104.128.106","name":"福建联通"},
        "DNS_FUJIAN_CT":{"ip":"218.85.152.99","name":"福建电信"},
        "DNS_FUJIAN_CM":{"ip":"211.138.151.161","name":"福建移动"},
        # 华中,
        "DNS_HUNAN_CU":{"ip":"58.20.127.238","name":"湖南联通"},
        "DNS_HUNAN_CT":{"ip":"222.246.129.80","name":"湖南电信"},
        "DNS_HUNAN_CM":{"ip":"211.142.210.98","name":"湖南移动"},
        "DNS_HUBEI_CU":{"ip":"218.104.111.114","name":"湖北联通"},
        "DNS_HUBEI_CT":{"ip":"202.103.24.68","name":"湖北电信"},
        "DNS_HUBEI_CM":{"ip":"211.137.58.20","name":"湖北移动"},
        "DNS_HENAN_CU":{"ip":"202.102.224.68","name":"河南联通"},
        "DNS_HENAN_CT":{"ip":"222.85.85.85","name":"河南电信"},
        "DNS_HENAN_CM":{"ip":"211.138.24.71","name":"河南移动"},
        "DNS_JIANGXI_CU":{"ip":"220.248.192.12","name":"江西联通"},
        "DNS_JIANGXI_CT":{"ip":"202.101.224.69","name":"江西电信"},
        "DNS_JIANGXI_CM":{"ip":"211.141.90.68","name":"江西移动"},
        # 华东,
        "DNS_SHANGHAI_CU":{"ip":"210.22.70.3","name":"上海联通"},
        "DNS_SHANGHAI_CT":{"ip":"202.96.209.133","name":"上海电信"},
        "DNS_SHANGHAI_CM":{"ip":"211.136.112.50","name":"上海移动"},
        "DNS_JIANGSU_CU":{"ip":"221.6.4.66","name":"江苏联通"},
        "DNS_JIANGSU_CT":{"ip":"218.2.2.2","name":"江苏电信"},
        "DNS_JIANGSU_CM":{"ip":"221.131.143.69","name":"江苏移动"},
        "DNS_ZHEJIANG_CU":{"ip":"221.12.1.227","name":"浙江联通"},
        "DNS_ZHEJIANG_CT":{"ip":"202.101.172.35","name":"浙江电信"},
        "DNS_ZHEJIANG_CM":{"ip":"211.140.13.188","name":"浙江移动"},
        "DNS_ANHUI_CU":{"ip":"218.104.78.2","name":"安徽联通"},
        "DNS_ANHUI_CT":{"ip":"61.132.163.68","name":"安徽电信"},
        "DNS_ANHUI_CM":{"ip":"211.138.180.2","name":"安徽移动"},
        "DNS_SHANDONG_CU":{"ip":"202.102.128.68","name":"山东联通"},
        "DNS_SHANDONG_CT":{"ip":"219.146.1.66","name":"山东电信"},
        "DNS_SHANDONG_CM":{"ip":"218.201.96.130","name":"山东移动"},
        # 西南,
        "DNS_CHONGQING_CU":{"ip":"221.5.203.98","name":"重庆联通"},
        "DNS_CHONGQING_CT":{"ip":"61.128.192.68","name":"重庆电信"},
        "DNS_CHONGQING_CM":{"ip":"218.201.4.3","name":"重庆移动"},
        "DNS_SICHUAN_CU":{"ip":"119.6.6.6","name":"四川联通"},
        "DNS_SICHUAN_CT":{"ip":"61.139.2.69","name":"四川电信"},
        "DNS_SICHUAN_CM":{"ip":"211.137.82.4","name":"四川移动"},
        "DNS_GUIZHOU_CU":{"ip":"221.13.28.234","name":"贵州联通"},
        "DNS_GUIZHOU_CT":{"ip":"202.98.192.67","name":"贵州电信"},
        "DNS_GUIZHOU_CM":{"ip":"211.139.5.29","name":"贵州移动"},
        "DNS_YUNNAN_CU":{"ip":"221.3.131.11","name":"云南联通"},
        "DNS_YUNNAN_CT":{"ip":"222.172.200.68","name":"云南电信"},
        "DNS_YUNNAN_CM":{"ip":"211.139.29.68","name":"云南移动"},
        "DNS_XIZANG_CU":{"ip":"221.13.65.34","name":"西藏联通"},
        "DNS_XIZANG_CT":{"ip":"202.98.224.68","name":"西藏电信"},
        "DNS_XIZANG_CM":{"ip":"211.139.73.34","name":"西藏移动"},
        # 西北,
        "DNS_SHAANXI_CU":{"ip":"221.11.1.67","name":"陕西联通"},
        "DNS_SHAANXI_CT":{"ip":"218.30.19.40","name":"陕西电信"},
        "DNS_SHAANXI_CM":{"ip":"211.137.130.3","name":"陕西移动"},
        "DNS_GANSU_CU":{"ip":"221.7.34.10","name":"甘肃联通"},
        "DNS_GANSU_CT":{"ip":"202.100.64.68","name":"甘肃电信"},
        "DNS_GANSU_CM":{"ip":"218.203.160.194","name":"甘肃移动"},
        "DNS_QINGHAI_CU":{"ip":"221.207.58.58","name":"青海联通"},
        "DNS_QINGHAI_CT":{"ip":"202.100.128.68","name":"青海电信"},
        "DNS_QINGHAI_CM":{"ip":"211.138.75.123","name":"青海移动"},
        "DNS_NINGXIA_CU":{"ip":"211.93.0.81","name":"宁夏联通"},
        "DNS_NINGXIA_CT":{"ip":"222.75.152.129","name":"宁夏电信"},
        "DNS_NINGXIA_CM":{"ip":"218.203.123.116","name":"宁夏移动"},
        "DNS_XINJIANG_CU":{"ip":"221.7.1.21","name":"新疆联通"},
        "DNS_XINJIANG_CT":{"ip":"61.128.114.166","name":"新疆电信"},
        "DNS_XINJIANG_CM":{"ip":"218.202.152.130","name":"新疆移动"},
        # 教育网（全国各地域都覆盖不太现实，选取北京交通大学 DNS 获取调度IP）,
        "DNS_JIAOYU":{"ip":"202.112.144.30","name":"教育网"}
    }
    # 获取 CDN 调度结果并将调度结果推送到 DNSPod

    DNSIP_NAME_List = list(DNSIP_List.keys())

    # 所有现有记录
    # 内容演示
    # {"广州移动":{"RecordId": 123456,"Value": "1.2.3.4","Status": "ENABLE"}}
    AllRecordInfoDict = {}

    # 更新后的解析记录列表
    new_AllRecordInfoList = []
    # 更新后的解析记录字典
    new_AllRecordInfoDict = {}

    # 待删除的解析记录ID
    remove_RecordID_List = []

    # 开始时间戳
    start_time = int(time.time())

    # 获取所有对应记录类型解析
    # 记录ID、分区名、记录值
    # 限制：只可获取3000条以下
    def get_AllRecordInfo():
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
                "Limit": 3000
                # "RecordLine": DNSIP_List[LocationAndNetName]["name"]
            }
            req.from_json_string(json.dumps(params))
            resp = client.DescribeRecordList(req)
            # print(resp.to_json_string())
            # 将返回数据写入变量
            result_All_Info_JSON = json.loads(resp.to_json_string())
            for oneRecord in result_All_Info_JSON['RecordList']:
                if oneRecord["Line"] in AllRecordInfoDict:
                    remove_RecordID_List.append(oneRecord["RecordId"])
                else:
                    AllRecordInfoDict[oneRecord["Line"]] = {"RecordId": oneRecord["RecordId"],"Value": oneRecord["Value"],"Status": oneRecord["Status"]}
            print("获取结束")
        except TencentCloudSDKException as err:
            print("获取报错:"+str(err))

    # 获取调度结果
    def get_AllocationResult(LocationAndNetName):
        CDN_Result = requests.get(DoH, params={'dn':CDNCNAME, 'type':record_type, 'ip':DNSIP_List[LocationAndNetName]["ip"], 'token':Token})
        print(CDN_Result.text)
        # 解析返回结果
        return CDN_Result.text.split(";")[0]
    
    # 更新记录
    def update_Record(RecordId,RecordValue,RecordLine):
        try:
            cred = credential.Credential(SecretId, SecretKey)
            httpProfile = HttpProfile()
            httpProfile.endpoint = "dnspod.tencentcloudapi.com"
            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = dnspod_client.DnspodClient(cred, "", clientProfile)
            req = models.ModifyRecordRequest()
            params = {
                "Domain": domain,
                "SubDomain": subdomain,
                "RecordId": RecordId,
                "RecordType": record_type,
                "RecordLine": RecordLine,
                "Value": RecordValue
            }
            req.from_json_string(json.dumps(params))
            resp = client.ModifyRecord(req)
            print(resp.to_json_string())
        except TencentCloudSDKException as err:
            print("更新报错:"+str(err))
            print(RecordId,RecordValue,RecordLine)
    
    # 添加记录
    def add_Record(RecordValue,RecordLine):
        try:
            cred = credential.Credential(SecretId, SecretKey)
            httpProfile = HttpProfile()
            httpProfile.endpoint = "dnspod.tencentcloudapi.com"
            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = dnspod_client.DnspodClient(cred, "", clientProfile)
            req = models.CreateRecordRequest()
            params = {
                "Domain": domain,
                "SubDomain": subdomain,
                "RecordType": record_type,
                "RecordLine": RecordLine,
                "Value": RecordValue
            }
            req.from_json_string(json.dumps(params))
            # 返回的resp是一个CreateRecordResponse的实例，与请求对象对应
            resp = client.CreateRecord(req)
            print(resp.to_json_string())
        except TencentCloudSDKException as err:
            print("添加报错:"+str(err))
            print(RecordValue,RecordLine)
    
    # 删除记录
    def remove_Record(RecordId):
        try:
            # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
            cred = credential.Credential(SecretId, SecretKey)
            # 实例化一个http选项，可选的，没有特殊需求可以跳过
            httpProfile = HttpProfile()
            httpProfile.endpoint = "dnspod.tencentcloudapi.com"

            # 实例化一个client选项，可选的，没有特殊需求可以跳过
            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            # 实例化要请求产品的client对象,clientProfile是可选的
            client = dnspod_client.DnspodClient(cred, "", clientProfile)

            # 实例化一个请求对象,每个接口都会对应一个request对象
            req = models.DeleteRecordRequest()
            params = {
                "Domain": domain,
                "RecordId": RecordId
            }
            req.from_json_string(json.dumps(params))

            # 返回的resp是一个DeleteRecordResponse的实例，与请求对象对应
            resp = client.DeleteRecord(req)
            # 输出json格式的字符串回包
            print(resp.to_json_string())
        except TencentCloudSDKException as err:
            print("删除报错:"+str(err))
    
    # 获取所有调度信息
    def get_new_AllRecordInfoList(LocationAndNetName):
        # 获取调度记录
        ip_Result = get_AllocationResult(LocationAndNetName)
        # 插入现有记录进列表
        new_AllRecordInfoList.append((DNSIP_List[LocationAndNetName]["name"],ip_Result))

    # 拉平的主函数
    def dns_Flattening(LocationAndNetName):
        # 获取当前地域调度ip
        ip_Result = new_AllRecordInfoDict[DNSIP_List[LocationAndNetName]["name"]]

        # 看看现有记录中有没有
        if DNSIP_List[LocationAndNetName]["name"] in AllRecordInfoDict:
            # 看看是否相同，相同则跳过
            if AllRecordInfoDict[DNSIP_List[LocationAndNetName]["name"]]["Value"] == ip_Result:
                print("记录值相同，无需更新")
                return
            else:
                # 更新记录
                update_Record(AllRecordInfoDict[DNSIP_List[LocationAndNetName]["name"]]["RecordId"],ip_Result,DNSIP_List[LocationAndNetName]["name"])
                # print(AllRecordInfoDict[DNSIP_List[LocationAndNetName]["name"]]["Value"],ip_Result)
        else:
            add_Record(ip_Result,DNSIP_List[LocationAndNetName]["name"])
        

    # 获取所有记录
    get_AllRecordInfo()

    # input(AllRecordInfoDict)
    # input(DNSIP_NAME_List)

    # 开始处理
    pool = Pool(20)
    # 获取调度记录
    pool.map(get_new_AllRecordInfoList,DNSIP_NAME_List)

    # 列表转字典
    for new_AllRecordInfoOne in new_AllRecordInfoList:
        new_AllRecordInfoDict[new_AllRecordInfoOne[0]] = new_AllRecordInfoOne[1]

    # f = open("doh.json","w+",encoding="utf-8")
    # f.write(json.dumps(new_AllRecordInfoDict,ensure_ascii=False))
    # f.close()

    # f = open("doh.json","r",encoding="utf-8")
    # new_AllRecordInfoDict = json.loads(f.read())
    # f.close()

    # input("ok")

    # 开始拉平
    pool.map(dns_Flattening,DNSIP_NAME_List)

    print("非默认线路处理结束")

    # 删除多余的记录
    pool.map(remove_Record,remove_RecordID_List)
    
    # print(new_AllRecordInfoDict)
    # 默认
    # 默认线路用于覆盖其他二级运营商等上面运营商线路未覆盖的线路，选取上海电信、北京联通、广东移动的IP作为默认线路
    add_Record(new_AllRecordInfoDict["上海电信"],"默认")
    add_Record(new_AllRecordInfoDict["北京联通"],"默认")
    if "默认" in AllRecordInfoDict:
        update_Record(AllRecordInfoDict["默认"]["RecordId"],new_AllRecordInfoDict["广东移动"],"默认")
    else:
        add_Record(new_AllRecordInfoDict["广东移动"],"默认")
    

    # 结束时间戳
    end_time = int(time.time())

    print("耗时: "+str(end_time - start_time))
