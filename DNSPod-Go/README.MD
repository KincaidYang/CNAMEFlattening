## 版本说明
Frost 版本使用 DoH 服务获取 CDN 调度 IP 结果

Storm 版本使用 HTTPDNS 服务获取 CDN 调度 IP 结果，可能会产生额外费用

## 使用说明
### 环境准备
使用前前自行安装 Golang，并将其配置到环境变量

安装说明可参考 https://go.dev，或自行搜索

### 导入记录
使用前请参考[导入记录-Frost版本](https://r2wind.cn/articles/20230108.html)完成记录的导入,请注意，当前模板有三条默认记录，请删掉最后两条默认记录，保留第一条即可

### 安装说明
#### 克隆仓库到本地
```bash
git clone https://github.com/KincaidYang/CNAMEFlattening.git
cd CNAMEFlattening
cd DNSPod-Go
# 请根据需要自行选择使用 Frost 版本或者 Storm 版本
```

### 配置基本信息
使用前请自行修改完善 config.go 文件中的相关信息


