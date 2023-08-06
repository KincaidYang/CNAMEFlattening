package main

const (
	// 请替换成您自己的域名
	domain = "r2wind.cn"
	// 请替换成您自己的子域名前缀，如www，如果不使用子域名请写 @
	subdomain = "www"
	// 请替换成您的 CDN或其他服务的 CNAME 服务地址
	CDNCNAME = "xxx.cn.cdn.dnsv1.com.cn"
	// 请替换成您的腾讯云账号的 SecretId 和 SecretKey，请前往 https://console.cloud.tencent.com/cam/capi 获取
	SecretId  = "12345678"
	SecretKey = "12345678"
	// 注意，该地址为DNSPod DoH服务地址，可自行替换为其他DoH服务地址
	DoH = "https://1.12.12.12/resolve"
	// 记录类型，AAAA为IPv6记录，A为IPv4记录，请根据实际需要自行修改
	recordType = "AAAA"
	// 记录TTL，单位秒，建议不低于60秒
	recordTTL = 60
)
