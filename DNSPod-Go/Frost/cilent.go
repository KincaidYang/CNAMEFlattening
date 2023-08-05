package main

import (
	"encoding/json"
	"fmt"
	"net"
	"net/http"

	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	dnspod "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dnspod/v20210323"
)

func main() {
	credential := common.NewCredential(
		SecretId,
		SecretKey,
	)

	cpf := profile.NewClientProfile()
	cpf.HttpProfile.Endpoint = "dnspod.tencentcloudapi.com"

	client, _ := dnspod.NewClient(credential, "", cpf)

	recordLines := []string{
		// 东北地区
		"辽宁联通", "辽宁电信", "辽宁移动", "吉林联通", "吉林电信", "吉林移动", "黑龙江联通", "黑龙江电信", "黑龙江移动",
		// 华北地区
		"北京联通", "北京电信", "北京移动", "河北联通", "河北电信", "河北移动", "山西联通", "山西电信", "山西移动", "内蒙联通", "内蒙电信", "内蒙移动", "天津联通", "天津电信", "天津移动",
		// 华东地区
		"上海联通", "上海电信", "上海移动", "江苏联通", "江苏电信", "江苏移动", "浙江联通", "浙江电信", "浙江移动", "安徽联通", "安徽电信", "安徽移动", "福建联通", "福建电信", "福建移动", "江西联通", "江西电信", "江西移动", "山东联通", "山东电信", "山东移动",
		// 华中地区
		"河南联通", "河南电信", "河南移动", "湖北联通", "湖北电信", "湖北移动", "湖南联通", "湖南电信", "湖南移动",
		// 华南地区
		"广东联通", "广东电信", "广东移动", "广西联通", "广西电信", "广西移动", "海南联通", "海南电信", "海南移动",
		// 西南地区
		"重庆联通", "重庆电信", "重庆移动", "四川联通", "四川电信", "四川移动", "贵州联通", "贵州电信", "贵州移动", "云南联通", "云南电信", "云南移动", "西藏联通", "西藏电信", "西藏移动",
		// 西北地区
		"陕西联通", "陕西电信", "陕西移动", "甘肃联通", "甘肃电信", "甘肃移动", "青海联通", "青海电信", "青海移动", "宁夏联通", "宁夏电信", "宁夏移动", "新疆联通", "新疆电信", "新疆移动",
		// 默认
		"默认",
	}

	dnsIPs := []string{
		DNS_LIAONING_CU, DNS_LIAONING_CT, DNS_LIAONING_CM, DNS_JILIN_CU, DNS_JILIN_CT, DNS_JILIN_CM, DNS_HEILONGJIANG_CU, DNS_HEILONGJIANG_CT, DNS_HEILONGJIANG_CM,
		DNS_BEIJING_CU, DNS_BEIJING_CT, DNS_BEIJING_CM, DNS_HEBEI_CU, DNS_HEBEI_CT, DNS_HEBEI_CM, DNS_SHANXI_CU, DNS_SHANXI_CT, DNS_SHANXI_CM, DNS_NEIMENGGU_CU, DNS_NEIMENGGU_CT, DNS_NEIMENGGU_CM, DNS_TIANJIN_CU, DNS_TIANJIN_CT, DNS_TIANJIN_CM,
		DNS_SHANGHAI_CU, DNS_SHANGHAI_CT, DNS_SHANGHAI_CM, DNS_JIANGSU_CU, DNS_JIANGSU_CT, DNS_JIANGSU_CM, DNS_ZHEJIANG_CU, DNS_ZHEJIANG_CT, DNS_ZHEJIANG_CM, DNS_ANHUI_CU, DNS_ANHUI_CT, DNS_ANHUI_CM, DNS_FUJIAN_CU, DNS_FUJIAN_CT, DNS_FUJIAN_CM, DNS_JIANGXI_CU, DNS_JIANGXI_CT, DNS_JIANGXI_CM, DNS_SHANDONG_CU, DNS_SHANDONG_CT, DNS_SHANDONG_CM,
		DNS_HENAN_CU, DNS_HENAN_CT, DNS_HENAN_CM, DNS_HUBEI_CU, DNS_HUBEI_CT, DNS_HUBEI_CM, DNS_HUNAN_CU, DNS_HUNAN_CT, DNS_HUNAN_CM,
		DNS_GUANGDONG_CU, DNS_GUANGDONG_CT, DNS_GUANGDONG_CM, DNS_GUANGXI_CU, DNS_GUANGXI_CT, DNS_GUANGXI_CM, DNS_HAINAN_CU, DNS_HAINAN_CT, DNS_HAINAN_CM,
		DNS_CHONGQING_CU, DNS_CHONGQING_CT, DNS_CHONGQING_CM, DNS_SICHUAN_CU, DNS_SICHUAN_CT, DNS_SICHUAN_CM, DNS_GUIZHOU_CU, DNS_GUIZHOU_CT, DNS_GUIZHOU_CM, DNS_YUNNAN_CU, DNS_YUNNAN_CT, DNS_YUNNAN_CM, DNS_XIZANG_CU, DNS_XIZANG_CT, DNS_XIZANG_CM,
		DNS_SHAANXI_CU, DNS_SHAANXI_CT, DNS_SHAANXI_CM, DNS_GANSU_CU, DNS_GANSU_CT, DNS_GANSU_CM, DNS_QINGHAI_CU, DNS_QINGHAI_CT, DNS_QINGHAI_CM, DNS_NINGXIA_CU, DNS_NINGXIA_CT, DNS_NINGXIA_CM, DNS_XINJIANG_CU, DNS_XINJIANG_CT, DNS_XINJIANG_CM,
		DNS_SHANGHAI_CT,
	}

	for i, recordLine := range recordLines {
		updateRecord(client, recordLine, dnsIPs[i])
	}
}

func updateRecord(client *dnspod.Client, recordLine, dnsIP string) {
	ip, err := fetchIP(dnsIP)
	if err != nil {
		panic(err)
	}

	request := dnspod.NewDescribeRecordListRequest()
	request.Domain = common.StringPtr(domain)
	request.Subdomain = common.StringPtr(subdomain)
	request.RecordType = common.StringPtr(recordType)
	request.RecordLine = common.StringPtr(recordLine)

	respRecordId, err := client.DescribeRecordList(request)
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	if err != nil {
		panic(err)
	}

	recordList := respRecordId.Response.RecordList
	recordID := *recordList[0].RecordId

	modifyRecordRequest := dnspod.NewModifyRecordRequest()
	modifyRecordRequest.Domain = common.StringPtr(domain)
	modifyRecordRequest.SubDomain = common.StringPtr(subdomain)
	modifyRecordRequest.RecordId = common.Uint64Ptr(uint64(recordID))
	modifyRecordRequest.RecordType = common.StringPtr(recordType)
	modifyRecordRequest.RecordLine = common.StringPtr(recordLine)
	modifyRecordRequest.Value = common.StringPtr(ip)
	modifyRecordRequest.TTL = common.Uint64Ptr(recordTTL)

	respModifyRecord, err := client.ModifyRecord(modifyRecordRequest)
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	if err != nil {
		panic(err)
	}

	fmt.Printf("%s", respModifyRecord.ToJsonString())
}

func fetchIP(dnsIP string) (string, error) {
	type Answer struct {
		Data string `json:"data"`
	}

	type DNSResponse struct {
		Answer []Answer `json:"Answer"`
	}

	resp, err := http.Get(fmt.Sprintf("%s?name=%s&type=%s&edns_client_subnet=%s", DoH, CDNCNAME, recordType, dnsIP))
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	var dnsResponse DNSResponse
	err = json.NewDecoder(resp.Body).Decode(&dnsResponse)
	if err != nil {
		return "", err
	}

	var ip string
	for _, answer := range dnsResponse.Answer {
		data := answer.Data
		if net.ParseIP(data) != nil {
			ip = data
			break
		}
	}

	return ip, nil
}
