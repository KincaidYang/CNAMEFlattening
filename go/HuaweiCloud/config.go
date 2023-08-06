package main

const (
	domain     = "r2wind.cn"                             // 请替换为您的域名
	CDNCNAME   = "r2wind.cn.cdn.dnsv1.com.cn"            // 请替换为您的服务商提供的 CNAME 地址
	ak         = "ZF5U********GO6LDNRLS"                 // 请替换为您的 AK，可前往华为云控制台“我的凭证”获取
	sk         = "PGDpq7zW7************jVwDwg7yfQBVTeLZ" // 请替换为您的 SK，可前往华为云控制台“我的凭证”获取
	DoH        = "https://1.12.12.12/resolve"            // DoH 地址，可自行替换，或使用默认值
	recordType = "AAAA"                                  // 请替换为您的记录类型，可选值为 A、AAAA，A 为 IPv4，AAAA 为 IPv6
)

var (
	subdomain = "ipv6"     // 请替换为您的子域名，若为根域名请留空或填写 @
	TTL       = int32(120) //TTL 值，可自行替换，或使用默认值
	// Region ID, 可以从 https://developer.huaweicloud.com/endpoint 获取, 例如cn-north-4
	// 请注意请前往 https://console.huaweicloud.com/iam/ > 项目 中查看自己是否开通了对应的区域，否则会报错
	regionName = "cn-north-4"
)
