package main

import (
	"encoding/json"
	"fmt"
	"net"
	"net/http"
	"sync"
	"time"

	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	dnspod "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/dnspod/v20210323"
)

func main() {
	startTime := time.Now()

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
		// 铁通
		"辽宁铁通", "吉林铁通", "黑龙江铁通", "北京铁通", "河北铁通", "山西铁通", "内蒙古铁通", "天津铁通", "上海铁通", "江苏铁通",
		"浙江铁通", "安徽铁通", "福建铁通", "江西铁通", "山东铁通", "河南铁通", "湖北铁通", "湖南铁通", "广东铁通", "广西铁通",
		"海南铁通", "重庆铁通", "四川铁通", "贵州铁通", "云南铁通", "西藏铁通", "陕西铁通", "甘肃铁通", "青海铁通", "宁夏铁通", "新疆铁通",
		// 教育网
		"辽宁教育网", "吉林教育网", "黑龙江教育网", "北京教育网", "河北教育网", "山西教育网", "内蒙古教育网", "天津教育网", "上海教育网", "江苏教育网",
		"浙江教育网", "安徽教育网", "福建教育网", "江西教育网", "山东教育网", "河南教育网", "湖北教育网", "湖南教育网", "广东教育网", "广西教育网",
		"海南教育网", "重庆教育网", "四川教育网", "贵州教育网", "云南教育网", "西藏教育网", "陕西教育网", "甘肃教育网", "青海教育网", "宁夏教育网", "新疆教育网",
		// 默认
		"默认",
		// 如需覆盖更多线路请在此处继续添加，并在dnsIPs中添加 LocalDNS IP 所对应的变量名称
		// 修改此处也请在控制台同步添加相应线路的解析记录，否则会出现解析失败的情况
	}

	dnsIPs := []string{
		DNS_LIAONING_CU, DNS_LIAONING_CT, DNS_LIAONING_CM, DNS_JILIN_CU, DNS_JILIN_CT, DNS_JILIN_CM, DNS_HEILONGJIANG_CU, DNS_HEILONGJIANG_CT, DNS_HEILONGJIANG_CM,
		DNS_BEIJING_CU, DNS_BEIJING_CT, DNS_BEIJING_CM, DNS_HEBEI_CU, DNS_HEBEI_CT, DNS_HEBEI_CM, DNS_SHANXI_CU, DNS_SHANXI_CT, DNS_SHANXI_CM, DNS_NEIMENGGU_CU, DNS_NEIMENGGU_CT, DNS_NEIMENGGU_CM, DNS_TIANJIN_CU, DNS_TIANJIN_CT, DNS_TIANJIN_CM,
		DNS_SHANGHAI_CU, DNS_SHANGHAI_CT, DNS_SHANGHAI_CM, DNS_JIANGSU_CU, DNS_JIANGSU_CT, DNS_JIANGSU_CM, DNS_ZHEJIANG_CU, DNS_ZHEJIANG_CT, DNS_ZHEJIANG_CM, DNS_ANHUI_CU, DNS_ANHUI_CT, DNS_ANHUI_CM, DNS_FUJIAN_CU, DNS_FUJIAN_CT, DNS_FUJIAN_CM, DNS_JIANGXI_CU, DNS_JIANGXI_CT, DNS_JIANGXI_CM, DNS_SHANDONG_CU, DNS_SHANDONG_CT, DNS_SHANDONG_CM,
		DNS_HENAN_CU, DNS_HENAN_CT, DNS_HENAN_CM, DNS_HUBEI_CU, DNS_HUBEI_CT, DNS_HUBEI_CM, DNS_HUNAN_CU, DNS_HUNAN_CT, DNS_HUNAN_CM,
		DNS_GUANGDONG_CU, DNS_GUANGDONG_CT, DNS_GUANGDONG_CM, DNS_GUANGXI_CU, DNS_GUANGXI_CT, DNS_GUANGXI_CM, DNS_HAINAN_CU, DNS_HAINAN_CT, DNS_HAINAN_CM,
		DNS_CHONGQING_CU, DNS_CHONGQING_CT, DNS_CHONGQING_CM, DNS_SICHUAN_CU, DNS_SICHUAN_CT, DNS_SICHUAN_CM, DNS_GUIZHOU_CU, DNS_GUIZHOU_CT, DNS_GUIZHOU_CM, DNS_YUNNAN_CU, DNS_YUNNAN_CT, DNS_YUNNAN_CM, DNS_XIZANG_CU, DNS_XIZANG_CT, DNS_XIZANG_CM,
		DNS_SHAANXI_CU, DNS_SHAANXI_CT, DNS_SHAANXI_CM, DNS_GANSU_CU, DNS_GANSU_CT, DNS_GANSU_CM, DNS_QINGHAI_CU, DNS_QINGHAI_CT, DNS_QINGHAI_CM, DNS_NINGXIA_CU, DNS_NINGXIA_CT, DNS_NINGXIA_CM, DNS_XINJIANG_CU, DNS_XINJIANG_CT, DNS_XINJIANG_CM,
		// 铁通
		DNS_LIAONING_CTT, DNS_JILIN_CTT, DNS_HEILONGJIANG_CTT, DNS_BEIJING_CTT, DNS_HEBEI_CTT, DNS_SHANXI_CTT, DNS_NEIMENGGU_CTT, DNS_TIANJIN_CTT, DNS_SHANGHAI_CTT, DNS_JIANGSU_CTT,
		DNS_ZHEJIANG_CTT, DNS_ANHUI_CTT, DNS_FUJIAN_CTT, DNS_JIANGXI_CTT, DNS_SHANDONG_CTT, DNS_HENAN_CTT, DNS_HUBEI_CTT, DNS_HUNAN_CTT, DNS_GUANGDONG_CTT, DNS_GUANGXI_CTT,
		DNS_HAINAN_CTT, DNS_CHONGQING_CTT, DNS_SICHUAN_CTT, DNS_GUIZHOU_CTT, DNS_YUNNAN_CTT, DNS_XIZANG_CTT, DNS_SHAANXI_CTT, DNS_GANSU_CTT, DNS_QINGHAI_CTT, DNS_NINGXIA_CTT, DNS_XINJIANG_CTT,
		// 教育网
		DNS_LIAONING_EDU, DNS_JILIN_EDU, DNS_HEILONGJIANG_EDU, DNS_BEIJING_EDU, DNS_HEBEI_EDU, DNS_SHANXI_EDU, DNS_NEIMENGGU_EDU, DNS_TIANJIN_EDU, DNS_SHANGHAI_EDU, DNS_JIANGSU_EDU,
		DNS_ZHEJIANG_EDU, DNS_ANHUI_EDU, DNS_FUJIAN_EDU, DNS_JIANGXI_EDU, DNS_SHANDONG_EDU, DNS_HENAN_EDU, DNS_HUBEI_EDU, DNS_HUNAN_EDU, DNS_GUANGDONG_EDU, DNS_GUANGXI_EDU,
		DNS_HAINAN_EDU, DNS_CHONGQING_EDU, DNS_SICHUAN_EDU, DNS_GUIZHOU_EDU, DNS_YUNNAN_EDU, DNS_XIZANG_EDU, DNS_SHAANXI_EDU, DNS_GANSU_EDU, DNS_QINGHAI_EDU, DNS_NINGXIA_EDU, DNS_XINJIANG_EDU,
		// 默认
		DNS_SHANGHAI_CT,
		// 添加前请前往localdns.go中添加对应的变量
	}

	// 创建信号量来限制并发数量，避免超过DNSPod API的QPS限制
	// DNSPod修改记录接口QPS限制为20，这里设置为15保持安全边际
	semaphore := make(chan struct{}, 15)

	var wg sync.WaitGroup

	// 处理每个域名配置
	for _, config := range domainConfigs {
		fmt.Printf("Processing domain: %s, subdomain: %s, record type: %s\n", config.Domain, config.Subdomain, config.RecordType)

		recordList, err := fetchRecordList(client, config.Domain, config.Subdomain)
		if err != nil {
			fmt.Printf("Error fetching record list for %s: %v\n", config.Domain, err)
			continue
		}

		for i, recordLine := range recordLines {
			wg.Add(1)
			go func(recordLine string, dnsIP string, cfg DomainConfig) {
				defer wg.Done()

				// 获取信号量
				semaphore <- struct{}{}
				defer func() {
					// 释放信号量
					<-semaphore
				}()

				err := updateRecord(client, recordList, recordLine, dnsIP, cfg)
				if err != nil {
					fmt.Printf("Error updating record: %v\n", err)
				}
			}(recordLine, dnsIPs[i], config)
		}
	}

	// 等待所有任务完成
	wg.Wait()

	endTime := time.Now()
	duration := endTime.Sub(startTime)

	fmt.Printf("Finished updating all record sets at %s. Total time: %s\n", endTime.Format("2006-01-02 15:04:05"), duration)
}

func fetchRecordList(client *dnspod.Client, domain, subdomain string) ([]*dnspod.RecordListItem, error) {
	describeRecordListRequest := dnspod.NewDescribeRecordListRequest()
	describeRecordListRequest.Domain = common.StringPtr(domain)
	describeRecordListRequest.Subdomain = common.StringPtr(subdomain)
	describeRecordListRequest.Limit = common.Uint64Ptr(3000)
	respRecordId, err := client.DescribeRecordList(describeRecordListRequest)
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return nil, err
	}
	if err != nil {
		return nil, err
	}
	return respRecordId.Response.RecordList, nil
}

func updateRecord(client *dnspod.Client, recordList []*dnspod.RecordListItem, recordLine, dnsIP string, cfg DomainConfig) error {
	ip, err := fetchIP(dnsIP, cfg.CDNCNAME, cfg.RecordType)
	if err != nil {
		return err
	}

	var recordID uint64
	var currentValue string
	var currentTTL uint64
	for _, record := range recordList {
		if *record.Line == recordLine && *record.Type == cfg.RecordType {
			recordID = uint64(*record.RecordId)
			currentValue = *record.Value
			currentTTL = uint64(*record.TTL)
			break
		}
	}

	if recordID == 0 {
		return fmt.Errorf("no matching record found for RecordLine: %s, RecordType: %s", recordLine, cfg.RecordType)
	}

	if ip == currentValue && cfg.RecordTTL == currentTTL {
		fmt.Printf("Record values are the same, no update needed. Domain: %s, Subdomain: %s, RecordID: %d, RecordLine: %s, IP: %s\n", cfg.Domain, cfg.Subdomain, recordID, recordLine, ip)
		return nil
	}

	modifyRecordRequest := dnspod.NewModifyRecordRequest()
	modifyRecordRequest.Domain = common.StringPtr(cfg.Domain)
	modifyRecordRequest.SubDomain = common.StringPtr(cfg.Subdomain)
	modifyRecordRequest.RecordId = common.Uint64Ptr(recordID)
	modifyRecordRequest.RecordType = common.StringPtr(cfg.RecordType)
	modifyRecordRequest.RecordLine = common.StringPtr(recordLine)
	modifyRecordRequest.Value = common.StringPtr(ip)
	modifyRecordRequest.TTL = common.Uint64Ptr(cfg.RecordTTL)

	respModifyRecord, err := client.ModifyRecord(modifyRecordRequest)
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		return fmt.Errorf("an API error has returned: %v , %s", err, respModifyRecord.ToJsonString())
	}
	if err != nil {
		return err
	}

	fmt.Printf("Upadate Record. Domain: %s, Subdomain: %s, RecordID: %d, RecordLine: %s, IP: %s\n", cfg.Domain, cfg.Subdomain, recordID, recordLine, ip)
	return nil
}

func fetchIP(dnsIP, cdnCNAME, recordType string) (string, error) {
	type Answer struct {
		Data string `json:"data"`
	}

	type DNSResponse struct {
		Answer []Answer `json:"Answer"`
	}

	resp, err := http.Get(fmt.Sprintf("%s?name=%s&type=%s&edns_client_subnet=%s", DoH, cdnCNAME, recordType, dnsIP))
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
