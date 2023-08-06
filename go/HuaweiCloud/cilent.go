package main

import (
	"encoding/json"
	"fmt"
	"net"
	"net/http"
	"time"

	"github.com/huaweicloud/huaweicloud-sdk-go-v3/core/auth/basic"
	dns "github.com/huaweicloud/huaweicloud-sdk-go-v3/services/dns/v2"
	"github.com/huaweicloud/huaweicloud-sdk-go-v3/services/dns/v2/model"
	region "github.com/huaweicloud/huaweicloud-sdk-go-v3/services/dns/v2/region"
)

func main() {
	startTime := time.Now()

	if subdomain == "@" {
		subdomain = ""
	}
	subdomains := subdomain
	if subdomain != "" {
		subdomains = subdomain + "."
	}
	FQDN := subdomains + domain + "."

	auth := basic.NewCredentialsBuilder().
		WithAk(ak).
		WithSk(sk).
		Build()

	client := dns.NewDnsClient(
		dns.DnsClientBuilder().
			WithRegion(region.ValueOf(regionName)).
			WithCredential(auth).
			Build())

	zoneID, err := getZoneID(client, domain)
	if err != nil {
		fmt.Println("Error getting zone ID:", err)
		return
	}

	for lineID, dnsServer := range DNS_SERVERS {
		cdnResult, err := fetchIP(DoH, CDNCNAME, recordType, dnsServer)
		if err != nil {
			fmt.Println("Error querying DOH CDN result:", err)
			continue
		}

		recordSetID, err := getRecordSetID(client, zoneID, lineID, recordType, FQDN)
		if err != nil {
			fmt.Println("Error getting record set ID:", err)
			continue
		}

		err = updateRecordSets(client, zoneID, recordSetID, cdnResult, TTL, recordType, FQDN)
		if err != nil {
			fmt.Println("Error updating record sets:", err)
		}
	}

	endTime := time.Now()
	duration := endTime.Sub(startTime)

	fmt.Printf("Finished updating record sets at %s. Total time: %s\n", endTime.Format("2006-01-02 15:04:05"), duration)
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

	return nil
}
