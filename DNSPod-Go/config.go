package main

const (
	// 请替换成您自己的域名
	domain = "r2wind.cn"
	// 请替换成您自己的子域名前缀，如果不使用子域名请写 @
	subdomain = "ipv6"
	// 请替换成您的 CDN或其他服务的 CNAME 服务地址
	// 使用前请前往 https://console.cloud.tencent.com/httpdns/domain 将 CDN 服务域名添加到 HTTPDNS
	// 仅需添加主域名，如您的 CDN 服务域名为 cdn.r2wind.cn，仅需填写 r2wind.cn 完成添加即可
	CDNCNAME = "r2wind.cn.eo.dnse3.com"
	// 请替换成您的腾讯云HTTPDNS服务的密钥，可前往 https://console.cloud.tencent.com/httpdns/configure 获取
	Token     = ""
	SecretId  = ""
	SecretKey = ""
	// 注意，该地址为DNSPod HTTPDNS服务地址，无需更换
	DoH = "https://119.29.29.99/d"
	// 记录类型，AAAA为IPv6记录，A为IPv4记录
	recordType = "AAAA"
	// 记录TTL，单位秒，建议不低于60秒
	recordTTL = 60
)
