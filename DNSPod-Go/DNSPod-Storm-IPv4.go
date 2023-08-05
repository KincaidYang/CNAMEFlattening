package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"

	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	dnspod "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dnspod/v20210323"
)

const (
	domain          = "r2wind.cn"
	subdomain       = "@"
	CDNCNAME        = "r2wind.cn.eo.dnse3.com"
	Token           = ""
	SecretId        = ""
	SecretKey       = ""
	DoH             = "https://119.29.29.99/d"
	recordType      = "A"
	DNS_LIAONING_CU = "202.96.64.68"
	DNS_LIAONING_CT = "219.148.204.66"
	DNS_LIAONING_CM = "211.137.32.178"
)

func main() {
	credential := common.NewCredential(
		SecretId,
		SecretKey,
	)

	cpf := profile.NewClientProfile()
	cpf.HttpProfile.Endpoint = "dnspod.tencentcloudapi.com"

	client, _ := dnspod.NewClient(credential, "", cpf)

	// 辽宁联通
	resp, err := http.Get(fmt.Sprintf("%s?dn=%s&type=%s&ip=%s&token=%s", DoH, CDNCNAME, recordType, DNS_LIAONING_CU, Token))
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	ip1_LIAONING_CU := strings.Split(string(body), ";")[0]

	request := dnspod.NewDescribeRecordListRequest()
	request.Domain = common.StringPtr(domain)
	request.SubDomain = common.StringPtr(subdomain)
	request.RecordType = common.StringPtr(recordType)
	request.RecordLine = common.StringPtr("辽宁联通")

	resp_LIAONING_CU_RecordId, err := client.DescribeRecordList(request)
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	if err != nil {
		panic(err)
	}

	recordList := resp_LIAONING_CU_RecordId.Response.RecordList
	RecordId_LIAONING_CU1 := *recordList[0].RecordId

	modifyRecordRequest := dnspod.NewModifyRecordRequest()
	modifyRecordRequest.Domain = common.StringPtr(domain)
	modifyRecordRequest.SubDomain = common.StringPtr(subdomain)
	modifyRecordRequest.RecordId = common.Uint64Ptr(uint64(RecordId_LIAONING_CU1))
	modifyRecordRequest.RecordType = common.StringPtr(recordType)
	modifyRecordRequest.RecordLine = common.StringPtr("辽宁联通")
	modifyRecordRequest.Value = common.StringPtr(ip1_LIAONING_CU)

	resp_DONGBEI_CU1_Modify_Record, err := client.ModifyRecord(modifyRecordRequest)
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	if err != nil {
		panic(err)
	}

	fmt.Printf("%s", resp_DONGBEI_CU1_Modify_Record.ToJsonString())

	// 更多的地区和运营商可以按照上面的代码模式继续添加
}
