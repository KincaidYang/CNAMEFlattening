package main

import (
	"encoding/json"
	"fmt"
	"net"
	"net/http"
	"sync"
	"time"

	"github.com/huaweicloud/huaweicloud-sdk-go-v3/core/auth/basic"
	dns "github.com/huaweicloud/huaweicloud-sdk-go-v3/services/dns/v2"
	"github.com/huaweicloud/huaweicloud-sdk-go-v3/services/dns/v2/model"
	region "github.com/huaweicloud/huaweicloud-sdk-go-v3/services/dns/v2/region"
)

func main() {
	startTime := time.Now()

	auth := basic.NewCredentialsBuilder().
		WithAk(ak).
		WithSk(sk).
		Build()

	client := dns.NewDnsClient(
		dns.DnsClientBuilder().
			WithRegion(region.ValueOf(regionName)).
			WithCredential(auth).
			Build())

	// 创建信号量来限制并发数量，避免超过华为云API的QPS限制
	// 设置为10保持安全边际，如果华为云限制更低可以调整这个值
	semaphore := make(chan struct{}, 10)

	var wg sync.WaitGroup

	// 处理每个域名配置
	for _, config := range domainConfigs {
		fmt.Printf("Processing domain: %s, subdomain: %s, record type: %s\n", config.Domain, config.Subdomain, config.RecordType)

		// 处理子域名格式
		subdomain := config.Subdomain
		if subdomain == "@" {
			subdomain = ""
		}
		subdomains := subdomain
		if subdomain != "" {
			subdomains = subdomain + "."
		}
		FQDN := subdomains + config.Domain + "."

		zoneID, err := getZoneID(client, config.Domain)
		if err != nil {
			fmt.Printf("Error getting zone ID for %s: %v\n", config.Domain, err)
			continue
		}

		for lineID, dnsServer := range DNS_SERVERS {
			wg.Add(1)
			go func(lineID string, dnsServer string, cfg DomainConfig, fqdn string, zoneId string) {
				defer wg.Done()

				// 获取信号量
				semaphore <- struct{}{}
				defer func() {
					// 释放信号量
					<-semaphore
				}()

				cdnResult, err := fetchIP(DoH, cfg.CDNCNAME, cfg.RecordType, dnsServer)
				if err != nil {
					fmt.Printf("Error querying DOH CDN result for %s: %v\n", cfg.Domain, err)
					return
				}

				recordSetID, err := getRecordSetID(client, zoneId, lineID, cfg.RecordType, fqdn)
				if err != nil {
					fmt.Printf("Error getting record set ID for %s: %v\n", cfg.Domain, err)
					return
				}

				err = updateRecordSets(client, zoneId, recordSetID, cdnResult, cfg.TTL, cfg.RecordType, fqdn)
				if err != nil {
					fmt.Printf("Error updating record sets for %s: %v\n", cfg.Domain, err)
				}
			}(lineID, dnsServer, config, FQDN, zoneID)
		}
	}

	// 等待所有任务完成
	wg.Wait()

	endTime := time.Now()
	duration := endTime.Sub(startTime)

	fmt.Printf("Finished updating all record sets at %s. Total time: %s\n", endTime.Format("2006-01-02 15:04:05"), duration)
}

func getZoneID(client *dns.DnsClient, domain string) (string, error) {
	request := &model.ListPublicZonesRequest{}
	typeRequest := "public"
	request.Type = &typeRequest
	nameRequest := domain
	request.Name = &nameRequest
	response, err := client.ListPublicZones(request)
	if err != nil {
		return "", err
	}

	if len(*response.Zones) == 0 {
		return "", fmt.Errorf("no zones found for domain %s", domain)
	}

	return *(*response.Zones)[0].Id, nil
}

func fetchIP(doh, cdnCNAME, recordType, dnsServer string) (string, error) {
	type Answer struct {
		Data string `json:"data"`
	}

	type DNSResponse struct {
		Answer []Answer `json:"Answer"`
	}

	url := fmt.Sprintf("%s?name=%s&type=%s&edns_client_subnet=%s", doh, cdnCNAME, recordType, dnsServer)
	resp, err := http.Get(url)
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

func getRecordSetID(client *dns.DnsClient, zoneID, lineID, recordType, FQDN string) (string, error) {
	request := &model.ShowRecordSetByZoneRequest{}
	request.ZoneId = zoneID
	request.LineId = &lineID
	statusRequest := "ACTIVE"
	request.Status = &statusRequest
	request.Type = &recordType
	request.Name = &FQDN
	response, err := client.ShowRecordSetByZone(request)
	if err != nil {
		return "", err
	}

	if len(*response.Recordsets) == 0 {
		return "", fmt.Errorf("no record sets found for FQDN %s", FQDN)
	}

	return *(*response.Recordsets)[0].Id, nil
}

func updateRecordSets(client *dns.DnsClient, zoneID, recordSetID, cdnResult string, ttl int32, recordType, FQDN string) error {
	request := &model.UpdateRecordSetsRequest{}
	request.ZoneId = zoneID
	request.RecordsetId = recordSetID
	listRecordsBody := []string{cdnResult}
	request.Body = &model.UpdateRecordSetsReq{
		Records: &listRecordsBody,
		Ttl:     &ttl,
		Type:    recordType,
		Name:    FQDN,
	}
	response, err := client.UpdateRecordSets(request)
	if err != nil {
		fmt.Printf("%+v\n", response)
	} else {
		fmt.Printf("Updated record set %s (RecordSetID: %s) with CDN result %s\n", FQDN, recordSetID, cdnResult)
	}

	return err
}
