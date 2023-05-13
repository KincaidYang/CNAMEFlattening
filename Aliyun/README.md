## 说明
Frost版本仅适用于腾讯云 EdgeOne、阿里云 CDN/DCDN、天翼云 CDN

alidns_record_ipv4.xlsx 和 alidns_record_ipv6.xlsx为导入模板，使用请参照下方说明

## 准备条件
### 安装阿里云 CLI 工具
使用前请自行参照[安装指南](https://help.aliyun.com/document_detail/121988.html)安装 CLI 工具，并完成[初始配置](https://help.aliyun.com/document_detail/121258.html)

### 导入记录
使用前请使用模板将记录阿里云，导入前请根据实际情况自行修改模板

### 替换脚本变量
请注意替换脚本内域名、CNAME域名、子域名等信息

## 使用方法
```bash
chmod u+x AliyunDNS-Frost-IPv6.sh
./AliyunDNS-Frost-IPv$.sh
```
