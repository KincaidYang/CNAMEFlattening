package main

// DNS配置结构
type DomainConfig struct {
	Domain     string // 域名
	Subdomain  string // 子域名，若为根域名请留空或填写 @
	CDNCNAME   string // CDN或其他服务的 CNAME 服务地址
	RecordType string // 记录类型，可选值为 A、AAAA，A 为 IPv4，AAAA 为 IPv6
	TTL        int32  // TTL 值
}

// 硬编码的域名配置列表，可以配置多个域名或同一域名的不同记录类型
var domainConfigs = []DomainConfig{
	{
		Domain:     "r2wind.cn",
		Subdomain:  "ipv6",
		CDNCNAME:   "ipv6.ddnsip.cn.cdn.dnsv1.com.cn",
		RecordType: "AAAA",
		TTL:        120,
	},
	{
		Domain:     "r2wind.cn",
		Subdomain:  "ipv4",
		CDNCNAME:   "ipv4.ddnsip.cn.cdn.dnsv1.com.cn",
		RecordType: "A",
		TTL:        120,
	},
	// 可以添加更多域名配置，例如：
	// {
	//     Domain:     "example.com",
	//     Subdomain:  "www",
	//     CDNCNAME:   "www.example.com.cdn.example.com",
	//     RecordType: "A",
	//     TTL:        300,
	// },
}

const (
	ak  = "ZF5UM*******O6LDNRLS"           // 请替换为您的 AK，可前往华为云控制台"我的凭证"获取
	sk  = "PGDpq7***********fQBrMKX6VTeLZ" // 请替换为您的 SK，可前往华为云控制台"我的凭证"获取
	DoH = "https://1.12.12.12/resolve"     // DoH 地址，可自行替换，或使用默认值
	// Region ID, 可以从 https://developer.huaweicloud.com/endpoint 获取, 例如cn-north-4
	// 请注意请前往 https://console.huaweicloud.com/iam/ > 项目 中查看自己是否开通了对应的区域，否则会报错
	regionName = "cn-north-4"
)
