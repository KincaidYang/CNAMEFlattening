// 本脚本调用了腾讯云HTTPDNS服务，可能会产生额外费用，如不想付费请使用Frost版本https://github.com/KincaidYang/CNAMEFlattening/tree/main/DNSPod/Frost
package main

// DNS配置结构
type DomainConfig struct {
	Domain     string // 域名
	Subdomain  string // 子域名前缀，如果不使用子域名请写 @
	CDNCNAME   string // CDN或其他服务的 CNAME 服务地址
	RecordType string // 记录类型，AAAA为IPv6记录，A为IPv4记录
	RecordTTL  uint64 // 记录TTL，单位秒，建议不低于60秒
}

// 硬编码的域名配置列表，可以配置多个域名或同一域名的不同记录类型
var domainConfigs = []DomainConfig{
	{
		Domain:     "r2wind.cn",
		Subdomain:  "ipv4",
		CDNCNAME:   "r2wind.cn.eo.dnse3.com",
		RecordType: "A",
		RecordTTL:  60,
	},
	{
		Domain:     "r2wind.cn",
		Subdomain:  "ipv6",
		CDNCNAME:   "r2wind.cn.eo.dnse3.com",
		RecordType: "AAAA",
		RecordTTL:  60,
	},
	// 可以添加更多域名配置，例如：
	// {
	//     Domain:     "example.com",
	//     Subdomain:  "www",
	//     CDNCNAME:   "www.example.com.cdn.example.com",
	//     RecordType: "A",
	//     RecordTTL:  300,
	// },
}

const (
	// 您的腾讯云HTTPDNS服务的密钥，可前往 https://console.cloud.tencent.com/httpdns/configure 获取
	Token = "1********0"
	// 您的腾讯云账号的 SecretId 和 SecretKey，可前往 https://console.cloud.tencent.com/cam/capi 获取
	SecretId  = "AKIDc5Ui**********cFfuz4GUX"
	SecretKey = "teMvJS**************8bppa8U"
	// 注意，该地址为DNSPod HTTPDNS服务地址，无需更换
	DoH = "https://119.29.29.99/d"
)
