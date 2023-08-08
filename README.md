# CNAMEFlattening
## 版本说明
本脚本支持 Python 和 Go 两种版本，其中Python版本支持华为云 DNS、阿里云 DNS 和DNSPod，Go 版本支持 DNSPod、华为云。
## 相关说明
本脚本用以拉平 CNAME 记录，当前仅支持 DNSPod、华为云DNS、阿里云 DNS。

DNSPod DNSPod DNS

HuaweiCloud 华为云 DNS

Aliyun 阿里云 DNS

请根据实际需要选择对应的脚本使用。

注意：本脚本仅测试了与腾讯云 CDN、腾讯云 EdgeOne、华为云 CDN、天翼云 CDN、阿里云 CDN 的兼容性，其他 CDN 厂商未测试兼容性，若有其他厂商需求请自行测试或提交Issue。
## 使用教程
该教程为 Python 版本，此处未列厂商说明可查看对于厂商文件夹下的 README.MD

DNSPod：[使用 DNSPod 拉平 CNAME 记录（CDN 场景）](https://r2wind.cn/articles/20230108.html)

华为云DNS：[使用华为云 DNS 拉平 CNAME 记录（CDN 场景）](https://r2wind.cn/articles/20230109.html)
## 脚本示意
该示意为 DNSPod Python版本，其他厂商和版本流程类似。

![流程图](https://github.com/KincaidYang/CNAMEFlattening/blob/main/static/DNSPodFlattening.png)
