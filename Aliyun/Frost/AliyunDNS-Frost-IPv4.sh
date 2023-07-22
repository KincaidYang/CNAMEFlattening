#!/bin/bash
# 写入变量
domain="r2wind.cn"
sub_domain="@"
CDNCNAME="r2wind.cn.eo.dnse3.com"
record_type_v4="A"
# 电信
# 安徽电信
# 获取安徽电信 CDN 调度结果
ANHUI_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=61.132.163.68")
# 获取安徽电信 CDN 调度结果的 IP 地址
ANHUI_CT_IP=$(echo $ANHUI_CT_CDN | jq -r '.Answer[0].data')
echo $ANHUI_CT_IP
# 获取安徽电信记录详情
result_ANHUI_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_anhui --Status Enable --SearchMode ADVANCED)
# 获取安徽电信记录详情的 RecordID
ANHUI_CT_RecordID=$(echo $result_ANHUI_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $ANHUI_CT_RecordID
# 修改安徽电信记录
ANHUI_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $ANHUI_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $ANHUI_CT_IP --Line cn_telecom_anhui --TTL 60)
echo $ANHUI_CT_UpdateDomainRecord_Result
# 北京电信
# 获取北京电信 CDN 调度结果
BEIJING_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=219.141.136.10")
# 获取北京电信 CDN 调度结果的 IP 地址
BEIJING_CT_IP=$(echo $BEIJING_CT_CDN | jq -r '.Answer[0].data')
echo $BEIJING_CT_IP
# 获取北京电信记录详情
result_BEIJING_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_beijing --Status Enable --SearchMode ADVANCED)
# 获取北京电信记录详情的 RecordID
BEIJING_CT_RecordID=$(echo $result_BEIJING_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $BEIJING_CT_RecordID
# 修改北京电信记录
BEIJING_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $BEIJING_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $BEIJING_CT_IP --Line cn_telecom_beijing --TTL 60)
echo $BEIJING_CT_UpdateDomainRecord_Result
# 福建电信
# 获取福建电信 CDN 调度结果
FUJIAN_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.85.152.99")
# 获取福建电信 CDN 调度结果的 IP 地址
FUJIAN_CT_IP=$(echo $FUJIAN_CT_CDN | jq -r '.Answer[0].data')
echo $FUJIAN_CT_IP
# 获取福建电信记录详情
result_FUJIAN_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_fujian --Status Enable --SearchMode ADVANCED)
# 获取福建电信记录详情的 RecordID
FUJIAN_CT_RecordID=$(echo $result_FUJIAN_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $FUJIAN_CT_RecordID
# 修改福建电信记录
FUJIAN_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $FUJIAN_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $FUJIAN_CT_IP --Line cn_telecom_fujian --TTL 60)
echo $FUJIAN_CT_UpdateDomainRecord_Result
# 甘肃电信
# 获取甘肃电信 CDN 调度结果
GANSU_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.100.64.68")
# 获取甘肃电信 CDN 调度结果的 IP 地址
GANSU_CT_IP=$(echo $GANSU_CT_CDN | jq -r '.Answer[0].data')
echo $GANSU_CT_IP
# 获取甘肃电信记录详情
result_GANSU_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_gansu --Status Enable --SearchMode ADVANCED)
# 获取甘肃电信记录详情的 RecordID
GANSU_CT_RecordID=$(echo $result_GANSU_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GANSU_CT_RecordID
# 修改甘肃电信记录
GANSU_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GANSU_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GANSU_CT_IP --Line cn_telecom_gansu --TTL 60)
echo $GANSU_CT_UpdateDomainRecord_Result
# 广东电信
# 获取广东电信 CDN 调度结果
GUANGDONG_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.96.134.133")
# 获取广东电信 CDN 调度结果的 IP 地址
GUANGDONG_CT_IP=$(echo $GUANGDONG_CT_CDN | jq -r '.Answer[0].data')
echo $GUANGDONG_CT_IP
# 获取广东电信记录详情
result_GUANGDONG_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_guangdong --Status Enable --SearchMode ADVANCED)
# 获取广东电信记录详情的 RecordID
GUANGDONG_CT_RecordID=$(echo $result_GUANGDONG_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GUANGDONG_CT_RecordID
# 修改广东电信记录
GUANGDONG_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GUANGDONG_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GUANGDONG_CT_IP --Line cn_telecom_guangdong --TTL 60)
echo $GUANGDONG_CT_UpdateDomainRecord_Result
# 广西电信
# 获取广西电信 CDN 调度结果
GUANGXI_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.103.225.68")
# 获取广西电信 CDN 调度结果的 IP 地址
GUANGXI_CT_IP=$(echo $GUANGXI_CT_CDN | jq -r '.Answer[0].data')
echo $GUANGXI_CT_IP
# 获取广西电信记录详情
result_GUANGXI_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_guangxi --Status Enable --SearchMode ADVANCED)
# 获取广西电信记录详情的 RecordID
GUANGXI_CT_RecordID=$(echo $result_GUANGXI_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GUANGXI_CT_RecordID
# 修改广西电信记录
GUANGXI_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GUANGXI_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GUANGXI_CT_IP --Line cn_telecom_guangxi --TTL 60)
echo $GUANGXI_CT_UpdateDomainRecord_Result
# 贵州电信
# 获取贵州电信 CDN 调度结果
GUIZHOU_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.98.192.67")
# 获取贵州电信 CDN 调度结果的 IP 地址
GUIZHOU_CT_IP=$(echo $GUIZHOU_CT_CDN | jq -r '.Answer[0].data')
echo $GUIZHOU_CT_IP
# 获取贵州电信记录详情
result_GUIZHOU_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_guizhou --Status Enable --SearchMode ADVANCED)
# 获取贵州电信记录详情的 RecordID
GUIZHOU_CT_RecordID=$(echo $result_GUIZHOU_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GUIZHOU_CT_RecordID
# 修改贵州电信记录
GUIZHOU_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GUIZHOU_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GUIZHOU_CT_IP --Line cn_telecom_guizhou --TTL 60)
echo $GUIZHOU_CT_UpdateDomainRecord_Result
# 海南电信
# 获取海南电信 CDN 调度结果
HAINAN_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.100.192.68")
# 获取海南电信 CDN 调度结果的 IP 地址
HAINAN_CT_IP=$(echo $HAINAN_CT_CDN | jq -r '.Answer[0].data')
echo $HAINAN_CT_IP
# 获取海南电信记录详情
result_HAINAN_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_hainan --Status Enable --SearchMode ADVANCED)
# 获取海南电信记录详情的 RecordID
HAINAN_CT_RecordID=$(echo $result_HAINAN_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HAINAN_CT_RecordID
# 修改海南电信记录
HAINAN_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HAINAN_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HAINAN_CT_IP --Line cn_telecom_hainan --TTL 60)
echo $HAINAN_CT_UpdateDomainRecord_Result
# 河北电信
# 获取河北电信 CDN 调度结果
HEBEI_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=222.222.222.222")
# 获取河北电信 CDN 调度结果的 IP 地址
HEBEI_CT_IP=$(echo $HEBEI_CT_CDN | jq -r '.Answer[0].data')
echo $HEBEI_CT_IP
# 获取河北电信记录详情
result_HEBEI_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_hebei --Status Enable --SearchMode ADVANCED)
# 获取河北电信记录详情的 RecordID
HEBEI_CT_RecordID=$(echo $result_HEBEI_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HEBEI_CT_RecordID
# 修改河北电信记录
HEBEI_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HEBEI_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HEBEI_CT_IP --Line cn_telecom_hebei --TTL 60)
echo $HEBEI_CT_UpdateDomainRecord_Result
# 黑龙江电信
# 获取黑龙江电信 CDN 调度结果
HEILONGJIANG_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=112.100.100.100")
# 获取黑龙江电信 CDN 调度结果的 IP 地址
HEILONGJIANG_CT_IP=$(echo $HEILONGJIANG_CT_CDN | jq -r '.Answer[0].data')
echo $HEILONGJIANG_CT_IP
# 获取黑龙江电信记录详情
result_HEILONGJIANG_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_heilongjiang --Status Enable --SearchMode ADVANCED)
# 获取黑龙江电信记录详情的 RecordID
HEILONGJIANG_CT_RecordID=$(echo $result_HEILONGJIANG_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HEILONGJIANG_CT_RecordID
# 修改黑龙江电信记录
HEILONGJIANG_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HEILONGJIANG_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HEILONGJIANG_CT_IP --Line cn_telecom_heilongjiang --TTL 60)
echo $HEILONGJIANG_CT_UpdateDomainRecord_Result
# 河南电信
# 获取河南电信 CDN 调度结果
HENAN_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=222.85.85.85")
# 获取河南电信 CDN 调度结果的 IP 地址
HENAN_CT_IP=$(echo $HENAN_CT_CDN | jq -r '.Answer[0].data')
echo $HENAN_CT_IP
# 获取河南电信记录详情
result_HENAN_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_henan --Status Enable --SearchMode ADVANCED)
# 获取河南电信记录详情的 RecordID
HENAN_CT_RecordID=$(echo $result_HENAN_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HENAN_CT_RecordID
# 修改河南电信记录
HENAN_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HENAN_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HENAN_CT_IP --Line cn_telecom_henan --TTL 60)
echo $HENAN_CT_UpdateDomainRecord_Result
# 湖北电信
# 获取湖北电信 CDN 调度结果
HUBEI_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.103.24.68")
# 获取湖北电信 CDN 调度结果的 IP 地址
HUBEI_CT_IP=$(echo $HUBEI_CT_CDN | jq -r '.Answer[0].data')
echo $HUBEI_CT_IP
# 获取湖北电信记录详情
result_HUBEI_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_hubei --Status Enable --SearchMode ADVANCED)
# 获取湖北电信记录详情的 RecordID
HUBEI_CT_RecordID=$(echo $result_HUBEI_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HUBEI_CT_RecordID
# 修改湖北电信记录
HUBEI_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HUBEI_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HUBEI_CT_IP --Line cn_telecom_hubei --TTL 60)
echo $HUBEI_CT_UpdateDomainRecord_Result
# 湖南电信
# 获取湖南电信 CDN 调度结果
HUNAN_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=222.246.129.80")
# 获取湖南电信 CDN 调度结果的 IP 地址
HUNAN_CT_IP=$(echo $HUNAN_CT_CDN | jq -r '.Answer[0].data')
echo $HUNAN_CT_IP
# 获取湖南电信记录详情
result_HUNAN_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_hunan --Status Enable --SearchMode ADVANCED)
# 获取湖南电信记录详情的 RecordID
HUNAN_CT_RecordID=$(echo $result_HUNAN_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HUNAN_CT_RecordID
# 修改湖南电信记录
HUNAN_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HUNAN_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HUNAN_CT_IP --Line cn_telecom_hunan --TTL 60)
echo $HUNAN_CT_UpdateDomainRecord_Result
# 江苏电信
# 获取江苏电信 CDN 调度结果
JIANGSU_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.2.2.2")
# 获取江苏电信 CDN 调度结果的 IP 地址
JIANGSU_CT_IP=$(echo $JIANGSU_CT_CDN | jq -r '.Answer[0].data')
echo $JIANGSU_CT_IP
# 获取江苏电信记录详情
result_JIANGSU_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_jiangsu --Status Enable --SearchMode ADVANCED)
# 获取江苏电信记录详情的 RecordID
JIANGSU_CT_RecordID=$(echo $result_JIANGSU_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $JIANGSU_CT_RecordID
# 修改江苏电信记录
JIANGSU_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $JIANGSU_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $JIANGSU_CT_IP --Line cn_telecom_jiangsu --TTL 60)
echo $JIANGSU_CT_UpdateDomainRecord_Result
# 江西电信
# 获取江西电信 CDN 调度结果
JIANGXI_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.101.224.69")
# 获取江西电信 CDN 调度结果的 IP 地址
JIANGXI_CT_IP=$(echo $JIANGXI_CT_CDN | jq -r '.Answer[0].data')
echo $JIANGXI_CT_IP
# 获取江西电信记录详情
result_JIANGXI_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_jiangxi --Status Enable --SearchMode ADVANCED)
# 获取江西电信记录详情的 RecordID
JIANGXI_CT_RecordID=$(echo $result_JIANGXI_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $JIANGXI_CT_RecordID
# 修改江西电信记录
JIANGXI_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $JIANGXI_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $JIANGXI_CT_IP --Line cn_telecom_jiangxi --TTL 60)
echo $JIANGXI_CT_UpdateDomainRecord_Result
# 吉林电信
# 获取吉林电信 CDN 调度结果
JILIN_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=219.149.194.55")
# 获取吉林电信 CDN 调度结果的 IP 地址
JILIN_CT_IP=$(echo $JILIN_CT_CDN | jq -r '.Answer[0].data')
echo $JILIN_CT_IP
# 获取吉林电信记录详情
result_JILIN_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_jilin --Status Enable --SearchMode ADVANCED)
# 获取吉林电信记录详情的 RecordID
JILIN_CT_RecordID=$(echo $result_JILIN_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $JILIN_CT_RecordID
# 修改吉林电信记录
JILIN_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $JILIN_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $JILIN_CT_IP --Line cn_telecom_jilin --TTL 60)
echo $JILIN_CT_UpdateDomainRecord_Result
# 辽宁电信
# 获取辽宁电信 CDN 调度结果
LIAONING_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=219.148.204.66")
# 获取辽宁电信 CDN 调度结果的 IP 地址
LIAONING_CT_IP=$(echo $LIAONING_CT_CDN | jq -r '.Answer[0].data')
echo $LIAONING_CT_IP
# 获取辽宁电信记录详情
result_LIAONING_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_liaoning --Status Enable --SearchMode ADVANCED)
# 获取辽宁电信记录详情的 RecordID
LIAONING_CT_RecordID=$(echo $result_LIAONING_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $LIAONING_CT_RecordID
# 修改辽宁电信记录
LIAONING_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $LIAONING_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $LIAONING_CT_IP --Line cn_telecom_liaoning --TTL 60)
echo $LIAONING_CT_UpdateDomainRecord_Result
# 内蒙古电信
# 获取内蒙古电信 CDN 调度结果
NEIMENGGU_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=219.148.162.31")
# 获取内蒙古电信 CDN 调度结果的 IP 地址
NEIMENGGU_CT_IP=$(echo $NEIMENGGU_CT_CDN | jq -r '.Answer[0].data')
echo $NEIMENGGU_CT_IP
# 获取内蒙古电信记录详情
result_NEIMENGGU_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_neimenggu --Status Enable --SearchMode ADVANCED)
# 获取内蒙古电信记录详情的 RecordID
NEIMENGGU_CT_RecordID=$(echo $result_NEIMENGGU_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $NEIMENGGU_CT_RecordID
# 修改内蒙古电信记录
NEIMENGGU_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $NEIMENGGU_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $NEIMENGGU_CT_IP --Line cn_telecom_neimenggu --TTL 60)
echo $NEIMENGGU_CT_UpdateDomainRecord_Result
# 宁夏电信
# 获取宁夏电信 CDN 调度结果
NINGXIA_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=222.75.152.129")
# 获取宁夏电信 CDN 调度结果的 IP 地址
NINGXIA_CT_IP=$(echo $NINGXIA_CT_CDN | jq -r '.Answer[0].data')
echo $NINGXIA_CT_IP
# 获取宁夏电信记录详情
result_NINGXIA_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_ningxia --Status Enable --SearchMode ADVANCED)
# 获取宁夏电信记录详情的 RecordID
NINGXIA_CT_RecordID=$(echo $result_NINGXIA_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $NINGXIA_CT_RecordID
# 修改宁夏电信记录
NINGXIA_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $NINGXIA_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $NINGXIA_CT_IP --Line cn_telecom_ningxia --TTL 60)
echo $NINGXIA_CT_UpdateDomainRecord_Result
# 青海电信
# 获取青海电信 CDN 调度结果
QINGHAI_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.100.128.68")
# 获取青海电信 CDN 调度结果的 IP 地址
QINGHAI_CT_IP=$(echo $QINGHAI_CT_CDN | jq -r '.Answer[0].data')
echo $QINGHAI_CT_IP
# 获取青海电信记录详情
result_QINGHAI_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_qinghai --Status Enable --SearchMode ADVANCED)
# 获取青海电信记录详情的 RecordID
QINGHAI_CT_RecordID=$(echo $result_QINGHAI_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $QINGHAI_CT_RecordID
# 修改青海电信记录
QINGHAI_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $QINGHAI_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $QINGHAI_CT_IP --Line cn_telecom_qinghai --TTL 60)
echo $QINGHAI_CT_UpdateDomainRecord_Result
# 陕西电信
# 获取陕西电信 CDN 调度结果
SHAANXI_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.30.19.40")
# 获取陕西电信 CDN 调度结果的 IP 地址
SHAANXI_CT_IP=$(echo $SHAANXI_CT_CDN | jq -r '.Answer[0].data')
echo $SHAANXI_CT_IP
# 获取陕西电信记录详情
result_SHAANXI_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_shaanxi --Status Enable --SearchMode ADVANCED)
# 获取陕西电信记录详情的 RecordID
SHAANXI_CT_RecordID=$(echo $result_SHAANXI_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHAANXI_CT_RecordID
# 修改陕西电信记录
SHAANXI_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHAANXI_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHAANXI_CT_IP --Line cn_telecom_shaanxi --TTL 60)
echo $SHAANXI_CT_UpdateDomainRecord_Result
# 山东电信
# 获取山东电信 CDN 调度结果
SHANDONG_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=219.146.1.66")
# 获取山东电信 CDN 调度结果的 IP 地址
SHANDONG_CT_IP=$(echo $SHANDONG_CT_CDN | jq -r '.Answer[0].data')
echo $SHANDONG_CT_IP
# 获取山东电信记录详情
result_SHANDONG_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_shandong --Status Enable --SearchMode ADVANCED)
# 获取山东电信记录详情的 RecordID
SHANDONG_CT_RecordID=$(echo $result_SHANDONG_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHANDONG_CT_RecordID
# 修改山东电信记录
SHANDONG_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHANDONG_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHANDONG_CT_IP --Line cn_telecom_shandong --TTL 60)
echo $SHANDONG_CT_UpdateDomainRecord_Result
# 上海电信
# 获取上海电信 CDN 调度结果
SHANGHAI_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.96.209.133")
# 获取上海电信 CDN 调度结果的 IP 地址
SHANGHAI_CT_IP=$(echo $SHANGHAI_CT_CDN | jq -r '.Answer[0].data')
echo $SHANGHAI_CT_IP
# 获取上海电信记录详情
result_SHANGHAI_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_shanghai --Status Enable --SearchMode ADVANCED)
# 获取上海电信记录详情的 RecordID
SHANGHAI_CT_RecordID=$(echo $result_SHANGHAI_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHANGHAI_CT_RecordID
# 修改上海电信记录
SHANGHAI_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHANGHAI_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHANGHAI_CT_IP --Line cn_telecom_shanghai --TTL 60)
echo $SHANGHAI_CT_UpdateDomainRecord_Result
# 山西电信
# 获取山西电信 CDN 调度结果
SHANXI_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=219.149.135.188")
# 获取山西电信 CDN 调度结果的 IP 地址
SHANXI_CT_IP=$(echo $SHANXI_CT_CDN | jq -r '.Answer[0].data')
echo $SHANXI_CT_IP
# 获取山西电信记录详情
result_SHANXI_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_shanxi --Status Enable --SearchMode ADVANCED)
# 获取山西电信记录详情的 RecordID
SHANXI_CT_RecordID=$(echo $result_SHANXI_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHANXI_CT_RecordID
# 修改山西电信记录
SHANXI_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHANXI_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHANXI_CT_IP --Line cn_telecom_shanxi --TTL 60)
echo $SHANXI_CT_UpdateDomainRecord_Result
# 四川电信
# 获取四川电信 CDN 调度结果
SICHUAN_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=61.139.2.69")
# 获取四川电信 CDN 调度结果的 IP 地址
SICHUAN_CT_IP=$(echo $SICHUAN_CT_CDN | jq -r '.Answer[0].data')
echo $SICHUAN_CT_IP
# 获取四川电信记录详情
result_SICHUAN_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_sichuan --Status Enable --SearchMode ADVANCED)
# 获取四川电信记录详情的 RecordID
SICHUAN_CT_RecordID=$(echo $result_SICHUAN_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SICHUAN_CT_RecordID
# 修改四川电信记录
SICHUAN_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SICHUAN_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SICHUAN_CT_IP --Line cn_telecom_sichuan --TTL 60)
echo $SICHUAN_CT_UpdateDomainRecord_Result
# 天津电信
# 获取天津电信 CDN 调度结果
TIANJIN_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=219.150.32.132")
# 获取天津电信 CDN 调度结果的 IP 地址
TIANJIN_CT_IP=$(echo $TIANJIN_CT_CDN | jq -r '.Answer[0].data')
echo $TIANJIN_CT_IP
# 获取天津电信记录详情
result_TIANJIN_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_tianjin --Status Enable --SearchMode ADVANCED)
# 获取天津电信记录详情的 RecordID
TIANJIN_CT_RecordID=$(echo $result_TIANJIN_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $TIANJIN_CT_RecordID
# 修改天津电信记录
TIANJIN_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $TIANJIN_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $TIANJIN_CT_IP --Line cn_telecom_tianjin --TTL 60)
echo $TIANJIN_CT_UpdateDomainRecord_Result
# 西藏电信
# 获取西藏电信 CDN 调度结果
XIZANG_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.98.224.68")
# 获取西藏电信 CDN 调度结果的 IP 地址
XIZANG_CT_IP=$(echo $XIZANG_CT_CDN | jq -r '.Answer[0].data')
echo $XIZANG_CT_IP
# 获取西藏电信记录详情
result_XIZANG_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_xizang --Status Enable --SearchMode ADVANCED)
# 获取西藏电信记录详情的 RecordID
XIZANG_CT_RecordID=$(echo $result_XIZANG_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $XIZANG_CT_RecordID
# 修改西藏电信记录
XIZANG_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $XIZANG_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $XIZANG_CT_IP --Line cn_telecom_xizang --TTL 60)
echo $XIZANG_CT_UpdateDomainRecord_Result
# 云南电信
# 获取云南电信 CDN 调度结果
YUNNAN_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=222.172.200.68")
# 获取云南电信 CDN 调度结果的 IP 地址
YUNNAN_CT_IP=$(echo $YUNNAN_CT_CDN | jq -r '.Answer[0].data')
echo $YUNNAN_CT_IP
# 获取云南电信记录详情
result_YUNNAN_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_yunnan --Status Enable --SearchMode ADVANCED)
# 获取云南电信记录详情的 RecordID
YUNNAN_CT_RecordID=$(echo $result_YUNNAN_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $YUNNAN_CT_RecordID
# 修改云南电信记录
YUNNAN_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $YUNNAN_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $YUNNAN_CT_IP --Line cn_telecom_yunnan --TTL 60)
echo $YUNNAN_CT_UpdateDomainRecord_Result
# 新疆电信
# 获取新疆电信 CDN 调度结果
XINJIANG_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=61.128.114.166")
# 获取新疆电信 CDN 调度结果的 IP 地址
XINJIANG_CT_IP=$(echo $XINJIANG_CT_CDN | jq -r '.Answer[0].data')
echo $XINJIANG_CT_IP
# 获取新疆电信记录详情
result_XINJIANG_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_xinjiang --Status Enable --SearchMode ADVANCED)
# 获取新疆电信记录详情的 RecordID
XINJIANG_CT_RecordID=$(echo $result_XINJIANG_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $XINJIANG_CT_RecordID
# 修改新疆电信记录
XINJIANG_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $XINJIANG_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $XINJIANG_CT_IP --Line cn_telecom_xinjiang --TTL 60)
echo $XINJIANG_CT_UpdateDomainRecord_Result
# 浙江电信
# 获取浙江电信 CDN 调度结果
ZHEJIANG_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.101.172.35")
# 获取浙江电信 CDN 调度结果的 IP 地址
ZHEJIANG_CT_IP=$(echo $ZHEJIANG_CT_CDN | jq -r '.Answer[0].data')
echo $ZHEJIANG_CT_IP
# 获取浙江电信记录详情
result_ZHEJIANG_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_zhejiang --Status Enable --SearchMode ADVANCED)
# 获取浙江电信记录详情的 RecordID
ZHEJIANG_CT_RecordID=$(echo $result_ZHEJIANG_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $ZHEJIANG_CT_RecordID
# 修改浙江电信记录
ZHEJIANG_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $ZHEJIANG_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $ZHEJIANG_CT_IP --Line cn_telecom_zhejiang --TTL 60)
echo $ZHEJIANG_CT_UpdateDomainRecord_Result
# 重庆电信
# 获取重庆电信 CDN 调度结果
CHONGQING_CT_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=61.128.192.68")
# 获取重庆电信 CDN 调度结果的 IP 地址
CHONGQING_CT_IP=$(echo $CHONGQING_CT_CDN | jq -r '.Answer[0].data')
echo $CHONGQING_CT_IP
# 获取重庆电信记录详情
result_CHONGQING_CT_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_telecom_chongqing --Status Enable --SearchMode ADVANCED)
# 获取重庆电信记录详情的 RecordID
CHONGQING_CT_RecordID=$(echo $result_CHONGQING_CT_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $CHONGQING_CT_RecordID
# 修改重庆电信记录
CHONGQING_CT_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $CHONGQING_CT_RecordID --RR $sub_domain --Type $record_type_v4 --Value $CHONGQING_CT_IP --Line cn_telecom_chongqing --TTL 60)
echo $CHONGQING_CT_UpdateDomainRecord_Result
# 联通
# 安徽联通
# 获取安徽联通 CDN 调度结果
ANHUI_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.104.78.2")
# 获取安徽联通 CDN 调度结果的 IP 地址
ANHUI_CU_IP=$(echo $ANHUI_CU_CDN | jq -r '.Answer[0].data')
echo $ANHUI_CU_IP
# 获取安徽联通记录详情
result_ANHUI_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_anhui --Status Enable --SearchMode ADVANCED)
# 获取安徽联通记录详情的 RecordID
ANHUI_CU_RecordID=$(echo $result_ANHUI_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $ANHUI_CU_RecordID
# 修改安徽联通记录
ANHUI_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $ANHUI_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $ANHUI_CU_IP --Line cn_unicom_anhui --TTL 60)
echo $ANHUI_CU_UpdateDomainRecord_Result
# 北京联通
# 获取北京联通 CDN 调度结果
BEIJING_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.106.196.115")
# 获取北京联通 CDN 调度结果的 IP 地址
BEIJING_CU_IP=$(echo $BEIJING_CU_CDN | jq -r '.Answer[0].data')
echo $BEIJING_CU_IP
# 获取北京联通记录详情
result_BEIJING_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_beijing --Status Enable --SearchMode ADVANCED)
# 获取北京联通记录详情的 RecordID
BEIJING_CU_RecordID=$(echo $result_BEIJING_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $BEIJING_CU_RecordID
# 修改北京联通记录
BEIJING_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $BEIJING_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $BEIJING_CU_IP --Line cn_unicom_beijing --TTL 60)
echo $BEIJING_CU_UpdateDomainRecord_Result
# 福建联通
# 获取福建联通 CDN 调度结果
FUJIAN_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.104.128.106")
# 获取福建联通 CDN 调度结果的 IP 地址
FUJIAN_CU_IP=$(echo $FUJIAN_CU_CDN | jq -r '.Answer[0].data')
echo $FUJIAN_CU_IP
# 获取福建联通记录详情
result_FUJIAN_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_fujian --Status Enable --SearchMode ADVANCED)
# 获取福建联通记录详情的 RecordID
FUJIAN_CU_RecordID=$(echo $result_FUJIAN_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $FUJIAN_CU_RecordID
# 修改福建联通记录
FUJIAN_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $FUJIAN_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $FUJIAN_CU_IP --Line cn_unicom_fujian --TTL 60)
echo $FUJIAN_CU_UpdateDomainRecord_Result
# 甘肃联通
# 获取甘肃联通 CDN 调度结果
GANSU_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.7.34.10")
# 获取甘肃联通 CDN 调度结果的 IP 地址
GANSU_CU_IP=$(echo $GANSU_CU_CDN | jq -r '.Answer[0].data')
echo $GANSU_CU_IP
# 获取甘肃联通记录详情
result_GANSU_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_gansu --Status Enable --SearchMode ADVANCED)
# 获取甘肃联通记录详情的 RecordID
GANSU_CU_RecordID=$(echo $result_GANSU_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GANSU_CU_RecordID
# 修改甘肃联通记录
GANSU_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GANSU_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GANSU_CU_IP --Line cn_unicom_gansu --TTL 60)
echo $GANSU_CU_UpdateDomainRecord_Result
# 广东联通
# 获取广东联通 CDN 调度结果
GUANGDONG_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=210.21.196.6")
# 获取广东联通 CDN 调度结果的 IP 地址
GUANGDONG_CU_IP=$(echo $GUANGDONG_CU_CDN | jq -r '.Answer[0].data')
echo $GUANGDONG_CU_IP
# 获取广东联通记录详情
result_GUANGDONG_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_guangdong --Status Enable --SearchMode ADVANCED)
# 获取广东联通记录详情的 RecordID
GUANGDONG_CU_RecordID=$(echo $result_GUANGDONG_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GUANGDONG_CU_RecordID
# 修改广东联通记录
GUANGDONG_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GUANGDONG_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GUANGDONG_CU_IP --Line cn_unicom_guangdong --TTL 60)
echo $GUANGDONG_CU_UpdateDomainRecord_Result
# 广西联通
# 获取广西联通 CDN 调度结果
GUANGXI_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.7.128.68")
# 获取广西联通 CDN 调度结果的 IP 地址
GUANGXI_CU_IP=$(echo $GUANGXI_CU_CDN | jq -r '.Answer[0].data')
echo $GUANGXI_CU_IP
# 获取广西联通记录详情
result_GUANGXI_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_guangxi --Status Enable --SearchMode ADVANCED)
# 获取广西联通记录详情的 RecordID
GUANGXI_CU_RecordID=$(echo $result_GUANGXI_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GUANGXI_CU_RecordID
# 修改广西联通记录
GUANGXI_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GUANGXI_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GUANGXI_CU_IP --Line cn_unicom_guangxi --TTL 60)
echo $GUANGXI_CU_UpdateDomainRecord_Result
# 贵州联通
# 获取贵州联通 CDN 调度结果
GUIZHOU_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.13.28.234")
# 获取贵州联通 CDN 调度结果的 IP 地址
GUIZHOU_CU_IP=$(echo $GUIZHOU_CU_CDN | jq -r '.Answer[0].data')
echo $GUIZHOU_CU_IP
# 获取贵州联通记录详情
result_GUIZHOU_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_guizhou --Status Enable --SearchMode ADVANCED)
# 获取贵州联通记录详情的 RecordID
GUIZHOU_CU_RecordID=$(echo $result_GUIZHOU_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GUIZHOU_CU_RecordID
# 修改贵州联通记录
GUIZHOU_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GUIZHOU_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GUIZHOU_CU_IP --Line cn_unicom_guizhou --TTL 60)
echo $GUIZHOU_CU_UpdateDomainRecord_Result
# 海南联通
# 获取海南联通 CDN 调度结果
HAINAN_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.11.132.2")
# 获取海南联通 CDN 调度结果的 IP 地址
HAINAN_CU_IP=$(echo $HAINAN_CU_CDN | jq -r '.Answer[0].data')
echo $HAINAN_CU_IP
# 获取海南联通记录详情
result_HAINAN_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_hainan --Status Enable --SearchMode ADVANCED)
# 获取海南联通记录详情的 RecordID
HAINAN_CU_RecordID=$(echo $result_HAINAN_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HAINAN_CU_RecordID
# 修改海南联通记录
HAINAN_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HAINAN_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HAINAN_CU_IP --Line cn_unicom_hainan --TTL 60)
echo $HAINAN_CU_UpdateDomainRecord_Result
# 河北联通
# 获取河北联通 CDN 调度结果
HEBEI_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.99.160.68")
# 获取河北联通 CDN 调度结果的 IP 地址
HEBEI_CU_IP=$(echo $HEBEI_CU_CDN | jq -r '.Answer[0].data')
echo $HEBEI_CU_IP
# 获取河北联通记录详情
result_HEBEI_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_hebei --Status Enable --SearchMode ADVANCED)
# 获取河北联通记录详情的 RecordID
HEBEI_CU_RecordID=$(echo $result_HEBEI_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HEBEI_CU_RecordID
# 修改河北联通记录
HEBEI_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HEBEI_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HEBEI_CU_IP --Line cn_unicom_hebei --TTL 60)
echo $HEBEI_CU_UpdateDomainRecord_Result
# 黑龙江联通
# 获取黑龙江联通 CDN 调度结果
HEILONGJIANG_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.97.224.68")
# 获取黑龙江联通 CDN 调度结果的 IP 地址
HEILONGJIANG_CU_IP=$(echo $HEILONGJIANG_CU_CDN | jq -r '.Answer[0].data')
echo $HEILONGJIANG_CU_IP
# 获取黑龙江联通记录详情
result_HEILONGJIANG_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_heilongjiang --Status Enable --SearchMode ADVANCED)
# 获取黑龙江联通记录详情的 RecordID
HEILONGJIANG_CU_RecordID=$(echo $result_HEILONGJIANG_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HEILONGJIANG_CU_RecordID
# 修改黑龙江联通记录
HEILONGJIANG_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HEILONGJIANG_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HEILONGJIANG_CU_IP --Line cn_unicom_heilongjiang --TTL 60)
echo $HEILONGJIANG_CU_UpdateDomainRecord_Result
# 河南联通
# 获取河南联通 CDN 调度结果
HENAN_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.102.224.68")
# 获取河南联通 CDN 调度结果的 IP 地址
HENAN_CU_IP=$(echo $HENAN_CU_CDN | jq -r '.Answer[0].data')
echo $HENAN_CU_IP
# 获取河南联通记录详情
result_HENAN_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_henan --Status Enable --SearchMode ADVANCED)
# 获取河南联通记录详情的 RecordID
HENAN_CU_RecordID=$(echo $result_HENAN_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HENAN_CU_RecordID
# 修改河南联通记录
HENAN_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HENAN_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HENAN_CU_IP --Line cn_unicom_henan --TTL 60)
echo $HENAN_CU_UpdateDomainRecord_Result
# 湖北联通
# 获取湖北联通 CDN 调度结果
HUBEI_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.104.111.114")
# 获取湖北联通 CDN 调度结果的 IP 地址
HUBEI_CU_IP=$(echo $HUBEI_CU_CDN | jq -r '.Answer[0].data')
echo $HUBEI_CU_IP
# 获取湖北联通记录详情
result_HUBEI_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_hubei --Status Enable --SearchMode ADVANCED)
# 获取湖北联通记录详情的 RecordID
HUBEI_CU_RecordID=$(echo $result_HUBEI_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HUBEI_CU_RecordID
# 修改湖北联通记录
HUBEI_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HUBEI_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HUBEI_CU_IP --Line cn_unicom_hubei --TTL 60)
echo $HUBEI_CU_UpdateDomainRecord_Result
# 湖南联通
# 获取湖南联通 CDN 调度结果
HUNAN_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=58.20.127.238")
# 获取湖南联通 CDN 调度结果的 IP 地址
HUNAN_CU_IP=$(echo $HUNAN_CU_CDN | jq -r '.Answer[0].data')
echo $HUNAN_CU_IP
# 获取湖南联通记录详情
result_HUNAN_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_hunan --Status Enable --SearchMode ADVANCED)
# 获取湖南联通记录详情的 RecordID
HUNAN_CU_RecordID=$(echo $result_HUNAN_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HUNAN_CU_RecordID
# 修改湖南联通记录
HUNAN_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HUNAN_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HUNAN_CU_IP --Line cn_unicom_hunan --TTL 60)
echo $HUNAN_CU_UpdateDomainRecord_Result
# 江苏联通
# 获取江苏联通 CDN 调度结果
JIANGSU_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.6.4.66")
# 获取江苏联通 CDN 调度结果的 IP 地址
JIANGSU_CU_IP=$(echo $JIANGSU_CU_CDN | jq -r '.Answer[0].data')
echo $JIANGSU_CU_IP
# 获取江苏联通记录详情
result_JIANGSU_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_jiangsu --Status Enable --SearchMode ADVANCED)
# 获取江苏联通记录详情的 RecordID
JIANGSU_CU_RecordID=$(echo $result_JIANGSU_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $JIANGSU_CU_RecordID
# 修改江苏联通记录
JIANGSU_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $JIANGSU_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $JIANGSU_CU_IP --Line cn_unicom_jiangsu --TTL 60)
echo $JIANGSU_CU_UpdateDomainRecord_Result
# 江西联通
# 获取江西联通 CDN 调度结果
JIANGXI_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=220.248.192.12")
# 获取江西联通 CDN 调度结果的 IP 地址
JIANGXI_CU_IP=$(echo $JIANGXI_CU_CDN | jq -r '.Answer[0].data')
echo $JIANGXI_CU_IP
# 获取江西联通记录详情
result_JIANGXI_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_jiangxi --Status Enable --SearchMode ADVANCED)
# 获取江西联通记录详情的 RecordID
JIANGXI_CU_RecordID=$(echo $result_JIANGXI_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $JIANGXI_CU_RecordID
# 修改江西联通记录
JIANGXI_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $JIANGXI_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $JIANGXI_CU_IP --Line cn_unicom_jiangxi --TTL 60)
echo $JIANGXI_CU_UpdateDomainRecord_Result
# 吉林联通
# 获取吉林联通 CDN 调度结果
JILIN_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.98.0.68")
# 获取吉林联通 CDN 调度结果的 IP 地址
JILIN_CU_IP=$(echo $JILIN_CU_CDN | jq -r '.Answer[0].data')
echo $JILIN_CU_IP
# 获取吉林联通记录详情
result_JILIN_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_jilin --Status Enable --SearchMode ADVANCED)
# 获取吉林联通记录详情的 RecordID
JILIN_CU_RecordID=$(echo $result_JILIN_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $JILIN_CU_RecordID
# 修改吉林联通记录
JILIN_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $JILIN_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $JILIN_CU_IP --Line cn_unicom_jilin --TTL 60)
echo $JILIN_CU_UpdateDomainRecord_Result
# 辽宁联通
# 获取辽宁联通 CDN 调度结果
LIAONING_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.96.64.68")
# 获取辽宁联通 CDN 调度结果的 IP 地址
LIAONING_CU_IP=$(echo $LIAONING_CU_CDN | jq -r '.Answer[0].data')
echo $LIAONING_CU_IP
# 获取辽宁联通记录详情
result_LIAONING_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_liaoning --Status Enable --SearchMode ADVANCED)
# 获取辽宁联通记录详情的 RecordID
LIAONING_CU_RecordID=$(echo $result_LIAONING_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $LIAONING_CU_RecordID
# 修改辽宁联通记录
LIAONING_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $LIAONING_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $LIAONING_CU_IP --Line cn_unicom_liaoning --TTL 60)
echo $LIAONING_CU_UpdateDomainRecord_Result
# 内蒙古联通
# 获取内蒙古联通 CDN 调度结果
NEIMENGGU_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.99.224.68")
# 获取内蒙古联通 CDN 调度结果的 IP 地址
NEIMENGGU_CU_IP=$(echo $NEIMENGGU_CU_CDN | jq -r '.Answer[0].data')
echo $NEIMENGGU_CU_IP
# 获取内蒙古联通记录详情
result_NEIMENGGU_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_neimenggu --Status Enable --SearchMode ADVANCED)
# 获取内蒙古联通记录详情的 RecordID
NEIMENGGU_CU_RecordID=$(echo $result_NEIMENGGU_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $NEIMENGGU_CU_RecordID
# 修改内蒙古联通记录
NEIMENGGU_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $NEIMENGGU_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $NEIMENGGU_CU_IP --Line cn_unicom_neimenggu --TTL 60)
echo $NEIMENGGU_CU_UpdateDomainRecord_Result
# 宁夏联通
# 获取宁夏联通 CDN 调度结果
NINGXIA_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.93.0.81")
# 获取宁夏联通 CDN 调度结果的 IP 地址
NINGXIA_CU_IP=$(echo $NINGXIA_CU_CDN | jq -r '.Answer[0].data')
echo $NINGXIA_CU_IP
# 获取宁夏联通记录详情
result_NINGXIA_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_ningxia --Status Enable --SearchMode ADVANCED)
# 获取宁夏联通记录详情的 RecordID
NINGXIA_CU_RecordID=$(echo $result_NINGXIA_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $NINGXIA_CU_RecordID
# 修改宁夏联通记录
NINGXIA_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $NINGXIA_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $NINGXIA_CU_IP --Line cn_unicom_ningxia --TTL 60)
echo $NINGXIA_CU_UpdateDomainRecord_Result
# 青海联通
# 获取青海联通 CDN 调度结果
QINGHAI_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.207.58.58")
# 获取青海联通 CDN 调度结果的 IP 地址
QINGHAI_CU_IP=$(echo $QINGHAI_CU_CDN | jq -r '.Answer[0].data')
echo $QINGHAI_CU_IP
# 获取青海联通记录详情
result_QINGHAI_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_qinghai --Status Enable --SearchMode ADVANCED)
# 获取青海联通记录详情的 RecordID
QINGHAI_CU_RecordID=$(echo $result_QINGHAI_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $QINGHAI_CU_RecordID
# 修改青海联通记录
QINGHAI_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $QINGHAI_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $QINGHAI_CU_IP --Line cn_unicom_qinghai --TTL 60)
echo $QINGHAI_CU_UpdateDomainRecord_Result
# 陕西联通
# 获取陕西联通 CDN 调度结果
SHAANXI_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.11.1.67")
# 获取陕西联通 CDN 调度结果的 IP 地址
SHAANXI_CU_IP=$(echo $SHAANXI_CU_CDN | jq -r '.Answer[0].data')
echo $SHAANXI_CU_IP
# 获取陕西联通记录详情
result_SHAANXI_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_shaanxi --Status Enable --SearchMode ADVANCED)
# 获取陕西联通记录详情的 RecordID
SHAANXI_CU_RecordID=$(echo $result_SHAANXI_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHAANXI_CU_RecordID
# 修改陕西联通记录
SHAANXI_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHAANXI_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHAANXI_CU_IP --Line cn_unicom_shaanxi --TTL 60)
echo $SHAANXI_CU_UpdateDomainRecord_Result
# 山东联通
# 获取山东联通 CDN 调度结果
SHANDONG_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.102.128.68")
# 获取山东联通 CDN 调度结果的 IP 地址
SHANDONG_CU_IP=$(echo $SHANDONG_CU_CDN | jq -r '.Answer[0].data')
echo $SHANDONG_CU_IP
# 获取山东联通记录详情
result_SHANDONG_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_shandong --Status Enable --SearchMode ADVANCED)
# 获取山东联通记录详情的 RecordID
SHANDONG_CU_RecordID=$(echo $result_SHANDONG_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHANDONG_CU_RecordID
# 修改山东联通记录
SHANDONG_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHANDONG_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHANDONG_CU_IP --Line cn_unicom_shandong --TTL 60)
echo $SHANDONG_CU_UpdateDomainRecord_Result
# 上海联通
# 获取上海联通 CDN 调度结果
SHANGHAI_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=210.22.70.3")
# 获取上海联通 CDN 调度结果的 IP 地址
SHANGHAI_CU_IP=$(echo $SHANGHAI_CU_CDN | jq -r '.Answer[0].data')
echo $SHANGHAI_CU_IP
# 获取上海联通记录详情
result_SHANGHAI_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_shanghai --Status Enable --SearchMode ADVANCED)
# 获取上海联通记录详情的 RecordID
SHANGHAI_CU_RecordID=$(echo $result_SHANGHAI_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHANGHAI_CU_RecordID
# 修改上海联通记录
SHANGHAI_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHANGHAI_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHANGHAI_CU_IP --Line cn_unicom_shanghai --TTL 60)
echo $SHANGHAI_CU_UpdateDomainRecord_Result
# 山西联通
# 获取山西联通 CDN 调度结果
SHANXI_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.99.216.113")
# 获取山西联通 CDN 调度结果的 IP 地址
SHANXI_CU_IP=$(echo $SHANXI_CU_CDN | jq -r '.Answer[0].data')
echo $SHANXI_CU_IP
# 获取山西联通记录详情
result_SHANXI_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_shanxi --Status Enable --SearchMode ADVANCED)
# 获取山西联通记录详情的 RecordID
SHANXI_CU_RecordID=$(echo $result_SHANXI_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHANXI_CU_RecordID
# 修改山西联通记录
SHANXI_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHANXI_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHANXI_CU_IP --Line cn_unicom_shanxi --TTL 60)
echo $SHANXI_CU_UpdateDomainRecord_Result
# 四川联通
# 获取四川联通 CDN 调度结果
SICHUAN_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=119.6.6.6")
# 获取四川联通 CDN 调度结果的 IP 地址
SICHUAN_CU_IP=$(echo $SICHUAN_CU_CDN | jq -r '.Answer[0].data')
echo $SICHUAN_CU_IP
# 获取四川联通记录详情
result_SICHUAN_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_sichuan --Status Enable --SearchMode ADVANCED)
# 获取四川联通记录详情的 RecordID
SICHUAN_CU_RecordID=$(echo $result_SICHUAN_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SICHUAN_CU_RecordID
# 修改四川联通记录
SICHUAN_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SICHUAN_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SICHUAN_CU_IP --Line cn_unicom_sichuan --TTL 60)
echo $SICHUAN_CU_UpdateDomainRecord_Result
# 天津联通
# 获取天津联通 CDN 调度结果
TIANJIN_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.99.96.68")
# 获取天津联通 CDN 调度结果的 IP 地址
TIANJIN_CU_IP=$(echo $TIANJIN_CU_CDN | jq -r '.Answer[0].data')
echo $TIANJIN_CU_IP
# 获取天津联通记录详情
result_TIANJIN_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_tianjin --Status Enable --SearchMode ADVANCED)
# 获取天津联通记录详情的 RecordID
TIANJIN_CU_RecordID=$(echo $result_TIANJIN_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $TIANJIN_CU_RecordID
# 修改天津联通记录
TIANJIN_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $TIANJIN_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $TIANJIN_CU_IP --Line cn_unicom_tianjin --TTL 60)
echo $TIANJIN_CU_UpdateDomainRecord_Result
# 西藏联通
# 获取西藏联通 CDN 调度结果
XIZANG_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.13.65.34")
# 获取西藏联通 CDN 调度结果的 IP 地址
XIZANG_CU_IP=$(echo $XIZANG_CU_CDN | jq -r '.Answer[0].data')
echo $XIZANG_CU_IP
# 获取西藏联通记录详情
result_XIZANG_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_xizang --Status Enable --SearchMode ADVANCED)
# 获取西藏联通记录详情的 RecordID
XIZANG_CU_RecordID=$(echo $result_XIZANG_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $XIZANG_CU_RecordID
# 修改西藏联通记录
XIZANG_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $XIZANG_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $XIZANG_CU_IP --Line cn_unicom_xizang --TTL 60)
echo $XIZANG_CU_UpdateDomainRecord_Result
# 新疆联通
# 获取新疆联通 CDN 调度结果
XINJIANG_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.7.1.21")
# 获取新疆联通 CDN 调度结果的 IP 地址
XINJIANG_CU_IP=$(echo $XINJIANG_CU_CDN | jq -r '.Answer[0].data')
echo $XINJIANG_CU_IP
# 获取新疆联通记录详情
result_XINJIANG_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_xinjiang --Status Enable --SearchMode ADVANCED)
# 获取新疆联通记录详情的 RecordID
XINJIANG_CU_RecordID=$(echo $result_XINJIANG_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $XINJIANG_CU_RecordID
# 修改新疆联通记录
XINJIANG_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $XINJIANG_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $XINJIANG_CU_IP --Line cn_unicom_xinjiang --TTL 60)
echo $XINJIANG_CU_UpdateDomainRecord_Result
# 云南联通
# 获取云南联通 CDN 调度结果
YUNNAN_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.3.131.11")
# 获取云南联通 CDN 调度结果的 IP 地址
YUNNAN_CU_IP=$(echo $YUNNAN_CU_CDN | jq -r '.Answer[0].data')
echo $YUNNAN_CU_IP
# 获取云南联通记录详情
result_YUNNAN_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_yunnan --Status Enable --SearchMode ADVANCED)
# 获取云南联通记录详情的 RecordID
YUNNAN_CU_RecordID=$(echo $result_YUNNAN_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $YUNNAN_CU_RecordID
# 修改云南联通记录
YUNNAN_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $YUNNAN_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $YUNNAN_CU_IP --Line cn_unicom_yunnan --TTL 60)
echo $YUNNAN_CU_UpdateDomainRecord_Result
# 浙江联通
# 获取浙江联通 CDN 调度结果
ZHEJIANG_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.12.1.227")
# 获取浙江联通 CDN 调度结果的 IP 地址
ZHEJIANG_CU_IP=$(echo $ZHEJIANG_CU_CDN | jq -r '.Answer[0].data')
echo $ZHEJIANG_CU_IP
# 获取浙江联通记录详情
result_ZHEJIANG_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_zhejiang --Status Enable --SearchMode ADVANCED)
# 获取浙江联通记录详情的 RecordID
ZHEJIANG_CU_RecordID=$(echo $result_ZHEJIANG_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $ZHEJIANG_CU_RecordID
# 修改浙江联通记录
ZHEJIANG_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $ZHEJIANG_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $ZHEJIANG_CU_IP --Line cn_unicom_zhejiang --TTL 60)
echo $ZHEJIANG_CU_UpdateDomainRecord_Result
# 重庆联通
# 获取重庆联通 CDN 调度结果
CHONGQING_CU_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.5.203.98")
# 获取重庆联通 CDN 调度结果的 IP 地址
CHONGQING_CU_IP=$(echo $CHONGQING_CU_CDN | jq -r '.Answer[0].data')
echo $CHONGQING_CU_IP
# 获取重庆联通记录详情
result_CHONGQING_CU_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_unicom_chongqing --Status Enable --SearchMode ADVANCED)
# 获取重庆联通记录详情的 RecordID
CHONGQING_CU_RecordID=$(echo $result_CHONGQING_CU_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $CHONGQING_CU_RecordID
# 修改重庆联通记录
CHONGQING_CU_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $CHONGQING_CU_RecordID --RR $sub_domain --Type $record_type_v4 --Value $CHONGQING_CU_IP --Line cn_unicom_chongqing --TTL 60)
echo $CHONGQING_CU_UpdateDomainRecord_Result
# 移动
# 安徽移动
# 获取安徽移动 CDN 调度结果
ANHUI_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.138.180.2")
# 获取安徽移动 CDN 调度结果的 IP 地址
ANHUI_CM_IP=$(echo $ANHUI_CM_CDN | jq -r '.Answer[0].data')
echo $ANHUI_CM_IP
# 获取安徽移动记录详情
result_ANHUI_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_anhui --Status Enable --SearchMode ADVANCED)
# 获取安徽移动记录详情的 RecordID
ANHUI_CM_RecordID=$(echo $result_ANHUI_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $ANHUI_CM_RecordID
# 修改安徽移动记录
ANHUI_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $ANHUI_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $ANHUI_CM_IP --Line cn_mobile_anhui --TTL 60)
echo $ANHUI_CM_UpdateDomainRecord_Result
# 北京移动
# 获取北京移动 CDN 调度结果
BEIJING_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.130.33.52")
# 获取北京移动 CDN 调度结果的 IP 地址
BEIJING_CM_IP=$(echo $BEIJING_CM_CDN | jq -r '.Answer[0].data')
echo $BEIJING_CM_IP
# 获取北京移动记录详情
result_BEIJING_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_beijing --Status Enable --SearchMode ADVANCED)
# 获取北京移动记录详情的 RecordID
BEIJING_CM_RecordID=$(echo $result_BEIJING_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $BEIJING_CM_RecordID
# 修改北京移动记录
BEIJING_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $BEIJING_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $BEIJING_CM_IP --Line cn_mobile_beijing --TTL 60)
echo $BEIJING_CM_UpdateDomainRecord_Result
# 福建移动
# 获取福建移动 CDN 调度结果
FUJIAN_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.138.151.161")
# 获取福建移动 CDN 调度结果的 IP 地址
FUJIAN_CM_IP=$(echo $FUJIAN_CM_CDN | jq -r '.Answer[0].data')
echo $FUJIAN_CM_IP
# 获取福建移动记录详情
result_FUJIAN_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_fujian --Status Enable --SearchMode ADVANCED)
# 获取福建移动记录详情的 RecordID
FUJIAN_CM_RecordID=$(echo $result_FUJIAN_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $FUJIAN_CM_RecordID
# 修改福建移动记录
FUJIAN_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $FUJIAN_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $FUJIAN_CM_IP --Line cn_mobile_fujian --TTL 60)
echo $FUJIAN_CM_UpdateDomainRecord_Result
# 甘肃移动
# 获取甘肃移动 CDN 调度结果
GANSU_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.203.160.194")
# 获取甘肃移动 CDN 调度结果的 IP 地址
GANSU_CM_IP=$(echo $GANSU_CM_CDN | jq -r '.Answer[0].data')
echo $GANSU_CM_IP
# 获取甘肃移动记录详情
result_GANSU_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_gansu --Status Enable --SearchMode ADVANCED)
# 获取甘肃移动记录详情的 RecordID
GANSU_CM_RecordID=$(echo $result_GANSU_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GANSU_CM_RecordID
# 修改甘肃移动记录
GANSU_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GANSU_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GANSU_CM_IP --Line cn_mobile_gansu --TTL 60)
echo $GANSU_CM_UpdateDomainRecord_Result
# 广东移动
# 获取广东移动 CDN 调度结果
GUANGDONG_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.139.163.6")
# 获取广东移动 CDN 调度结果的 IP 地址
GUANGDONG_CM_IP=$(echo $GUANGDONG_CM_CDN | jq -r '.Answer[0].data')
echo $GUANGDONG_CM_IP
# 获取广东移动记录详情
result_GUANGDONG_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_guangdong --Status Enable --SearchMode ADVANCED)
# 获取广东移动记录详情的 RecordID
GUANGDONG_CM_RecordID=$(echo $result_GUANGDONG_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GUANGDONG_CM_RecordID
# 修改广东移动记录
GUANGDONG_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GUANGDONG_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GUANGDONG_CM_IP --Line cn_mobile_guangdong --TTL 60)
echo $GUANGDONG_CM_UpdateDomainRecord_Result
# 广西移动
# 获取广西移动 CDN 调度结果
GUANGXI_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.138.245.180")
# 获取广西移动 CDN 调度结果的 IP 地址
GUANGXI_CM_IP=$(echo $GUANGXI_CM_CDN | jq -r '.Answer[0].data')
echo $GUANGXI_CM_IP
# 获取广西移动记录详情
result_GUANGXI_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_guangxi --Status Enable --SearchMode ADVANCED)
# 获取广西移动记录详情的 RecordID
GUANGXI_CM_RecordID=$(echo $result_GUANGXI_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GUANGXI_CM_RecordID
# 修改广西移动记录
GUANGXI_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GUANGXI_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GUANGXI_CM_IP --Line cn_mobile_guangxi --TTL 60)
echo $GUANGXI_CM_UpdateDomainRecord_Result
# 贵州移动
# 获取贵州移动 CDN 调度结果
GUIZHOU_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.139.5.29")
# 获取贵州移动 CDN 调度结果的 IP 地址
GUIZHOU_CM_IP=$(echo $GUIZHOU_CM_CDN | jq -r '.Answer[0].data')
echo $GUIZHOU_CM_IP
# 获取贵州移动记录详情
result_GUIZHOU_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_guizhou --Status Enable --SearchMode ADVANCED)
# 获取贵州移动记录详情的 RecordID
GUIZHOU_CM_RecordID=$(echo $result_GUIZHOU_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $GUIZHOU_CM_RecordID
# 修改贵州移动记录
GUIZHOU_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $GUIZHOU_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $GUIZHOU_CM_IP --Line cn_mobile_guizhou --TTL 60)
echo $GUIZHOU_CM_UpdateDomainRecord_Result
# 海南移动
# 获取海南移动 CDN 调度结果
HAINAN_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.176.88.95")
# 获取海南移动 CDN 调度结果的 IP 地址
HAINAN_CM_IP=$(echo $HAINAN_CM_CDN | jq -r '.Answer[0].data')
echo $HAINAN_CM_IP
# 获取海南移动记录详情
result_HAINAN_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_hainan --Status Enable --SearchMode ADVANCED)
# 获取海南移动记录详情的 RecordID
HAINAN_CM_RecordID=$(echo $result_HAINAN_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HAINAN_CM_RecordID
# 修改海南移动记录
HAINAN_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HAINAN_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HAINAN_CM_IP --Line cn_mobile_hainan --TTL 60)
echo $HAINAN_CM_UpdateDomainRecord_Result
# 河北移动
# 获取河北移动 CDN 调度结果
HEBEI_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.138.13.66")
# 获取河北移动 CDN 调度结果的 IP 地址
HEBEI_CM_IP=$(echo $HEBEI_CM_CDN | jq -r '.Answer[0].data')
echo $HEBEI_CM_IP
# 获取河北移动记录详情
result_HEBEI_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_hebei --Status Enable --SearchMode ADVANCED)
# 获取河北移动记录详情的 RecordID
HEBEI_CM_RecordID=$(echo $result_HEBEI_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HEBEI_CM_RecordID
# 修改河北移动记录
HEBEI_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HEBEI_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HEBEI_CM_IP --Line cn_mobile_hebei --TTL 60)
echo $HEBEI_CM_UpdateDomainRecord_Result
# 黑龙江移动
# 获取黑龙江移动 CDN 调度结果
HEILONGJIANG_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.137.241.34")
# 获取黑龙江移动 CDN 调度结果的 IP 地址
HEILONGJIANG_CM_IP=$(echo $HEILONGJIANG_CM_CDN | jq -r '.Answer[0].data')
echo $HEILONGJIANG_CM_IP
# 获取黑龙江移动记录详情
result_HEILONGJIANG_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_heilongjiang --Status Enable --SearchMode ADVANCED)
# 获取黑龙江移动记录详情的 RecordID
HEILONGJIANG_CM_RecordID=$(echo $result_HEILONGJIANG_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HEILONGJIANG_CM_RecordID
# 修改黑龙江移动记录
HEILONGJIANG_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HEILONGJIANG_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HEILONGJIANG_CM_IP --Line cn_mobile_heilongjiang --TTL 60)
echo $HEILONGJIANG_CM_UpdateDomainRecord_Result
# 河南移动
# 获取河南移动 CDN 调度结果
HENAN_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.138.24.71")
# 获取河南移动 CDN 调度结果的 IP 地址
HENAN_CM_IP=$(echo $HENAN_CM_CDN | jq -r '.Answer[0].data')
echo $HENAN_CM_IP
# 获取河南移动记录详情
result_HENAN_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_henan --Status Enable --SearchMode ADVANCED)
# 获取河南移动记录详情的 RecordID
HENAN_CM_RecordID=$(echo $result_HENAN_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HENAN_CM_RecordID
# 修改河南移动记录
HENAN_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HENAN_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HENAN_CM_IP --Line cn_mobile_henan --TTL 60)
echo $HENAN_CM_UpdateDomainRecord_Result
# 湖北移动
# 获取湖北移动 CDN 调度结果
HUBEI_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.137.58.20")
# 获取湖北移动 CDN 调度结果的 IP 地址
HUBEI_CM_IP=$(echo $HUBEI_CM_CDN | jq -r '.Answer[0].data')
echo $HUBEI_CM_IP
# 获取湖北移动记录详情
result_HUBEI_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_hubei --Status Enable --SearchMode ADVANCED)
# 获取湖北移动记录详情的 RecordID
HUBEI_CM_RecordID=$(echo $result_HUBEI_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HUBEI_CM_RecordID
# 修改湖北移动记录
HUBEI_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HUBEI_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HUBEI_CM_IP --Line cn_mobile_hubei --TTL 60)
echo $HUBEI_CM_UpdateDomainRecord_Result
# 湖南移动
# 获取湖南移动 CDN 调度结果
HUNAN_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.142.210.98")
# 获取湖南移动 CDN 调度结果的 IP 地址
HUNAN_CM_IP=$(echo $HUNAN_CM_CDN | jq -r '.Answer[0].data')
echo $HUNAN_CM_IP
# 获取湖南移动记录详情
result_HUNAN_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_hunan --Status Enable --SearchMode ADVANCED)
# 获取湖南移动记录详情的 RecordID
HUNAN_CM_RecordID=$(echo $result_HUNAN_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $HUNAN_CM_RecordID
# 修改湖南移动记录
HUNAN_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $HUNAN_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $HUNAN_CM_IP --Line cn_mobile_hunan --TTL 60)
echo $HUNAN_CM_UpdateDomainRecord_Result
# 江苏移动
# 获取江苏移动 CDN 调度结果
JIANGSU_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=221.131.143.69")
# 获取江苏移动 CDN 调度结果的 IP 地址
JIANGSU_CM_IP=$(echo $JIANGSU_CM_CDN | jq -r '.Answer[0].data')
echo $JIANGSU_CM_IP
# 获取江苏移动记录详情
result_JIANGSU_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_jiangsu --Status Enable --SearchMode ADVANCED)
# 获取江苏移动记录详情的 RecordID
JIANGSU_CM_RecordID=$(echo $result_JIANGSU_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $JIANGSU_CM_RecordID
# 修改江苏移动记录
JIANGSU_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $JIANGSU_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $JIANGSU_CM_IP --Line cn_mobile_jiangsu --TTL 60)
echo $JIANGSU_CM_UpdateDomainRecord_Result
# 江西移动
# 获取江西移动 CDN 调度结果
JIANGXI_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.141.90.68")
# 获取江西移动 CDN 调度结果的 IP 地址
JIANGXI_CM_IP=$(echo $JIANGXI_CM_CDN | jq -r '.Answer[0].data')
echo $JIANGXI_CM_IP
# 获取江西移动记录详情
result_JIANGXI_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_jiangxi --Status Enable --SearchMode ADVANCED)
# 获取江西移动记录详情的 RecordID
JIANGXI_CM_RecordID=$(echo $result_JIANGXI_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $JIANGXI_CM_RecordID
# 修改江西移动记录
JIANGXI_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $JIANGXI_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $JIANGXI_CM_IP --Line cn_mobile_jiangxi --TTL 60)
echo $JIANGXI_CM_UpdateDomainRecord_Result
# 吉林移动
# 获取吉林移动 CDN 调度结果
JILIN_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.141.16.99")
# 获取吉林移动 CDN 调度结果的 IP 地址
JILIN_CM_IP=$(echo $JILIN_CM_CDN | jq -r '.Answer[0].data')
echo $JILIN_CM_IP
# 获取吉林移动记录详情
result_JILIN_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_jilin --Status Enable --SearchMode ADVANCED)
# 获取吉林移动记录详情的 RecordID
JILIN_CM_RecordID=$(echo $result_JILIN_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $JILIN_CM_RecordID
# 修改吉林移动记录
JILIN_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $JILIN_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $JILIN_CM_IP --Line cn_mobile_jilin --TTL 60)
echo $JILIN_CM_UpdateDomainRecord_Result
# 辽宁移动
# 获取辽宁移动 CDN 调度结果
LIAONING_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.137.32.178")
# 获取辽宁移动 CDN 调度结果的 IP 地址
LIAONING_CM_IP=$(echo $LIAONING_CM_CDN | jq -r '.Answer[0].data')
echo $LIAONING_CM_IP
# 获取辽宁移动记录详情
result_LIAONING_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_liaoning --Status Enable --SearchMode ADVANCED)
# 获取辽宁移动记录详情的 RecordID
LIAONING_CM_RecordID=$(echo $result_LIAONING_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $LIAONING_CM_RecordID
# 修改辽宁移动记录
LIAONING_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $LIAONING_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $LIAONING_CM_IP --Line cn_mobile_liaoning --TTL 60)
echo $LIAONING_CM_UpdateDomainRecord_Result
# 内蒙古移动
# 获取内蒙古移动 CDN 调度结果
NEIMENGGU_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.138.91.1")
# 获取内蒙古移动 CDN 调度结果的 IP 地址
NEIMENGGU_CM_IP=$(echo $NEIMENGGU_CM_CDN | jq -r '.Answer[0].data')
echo $NEIMENGGU_CM_IP
# 获取内蒙古移动记录详情
result_NEIMENGGU_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_neimenggu --Status Enable --SearchMode ADVANCED)
# 获取内蒙古移动记录详情的 RecordID
NEIMENGGU_CM_RecordID=$(echo $result_NEIMENGGU_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $NEIMENGGU_CM_RecordID
# 修改内蒙古移动记录
NEIMENGGU_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $NEIMENGGU_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $NEIMENGGU_CM_IP --Line cn_mobile_neimenggu --TTL 60)
echo $NEIMENGGU_CM_UpdateDomainRecord_Result
# 宁夏移动
# 获取宁夏移动 CDN 调度结果
NINGXIA_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.203.123.116")
# 获取宁夏移动 CDN 调度结果的 IP 地址
NINGXIA_CM_IP=$(echo $NINGXIA_CM_CDN | jq -r '.Answer[0].data')
echo $NINGXIA_CM_IP
# 获取宁夏移动记录详情
result_NINGXIA_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_ningxia --Status Enable --SearchMode ADVANCED)
# 获取宁夏移动记录详情的 RecordID
NINGXIA_CM_RecordID=$(echo $result_NINGXIA_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $NINGXIA_CM_RecordID
# 修改宁夏移动记录
NINGXIA_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $NINGXIA_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $NINGXIA_CM_IP --Line cn_mobile_ningxia --TTL 60)
echo $NINGXIA_CM_UpdateDomainRecord_Result
# 青海移动
# 获取青海移动 CDN 调度结果
QINGHAI_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.138.75.123")
# 获取青海移动 CDN 调度结果的 IP 地址
QINGHAI_CM_IP=$(echo $QINGHAI_CM_CDN | jq -r '.Answer[0].data')
echo $QINGHAI_CM_IP
# 获取青海移动记录详情
result_QINGHAI_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_qinghai --Status Enable --SearchMode ADVANCED)
# 获取青海移动记录详情的 RecordID
QINGHAI_CM_RecordID=$(echo $result_QINGHAI_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $QINGHAI_CM_RecordID
# 修改青海移动记录
QINGHAI_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $QINGHAI_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $QINGHAI_CM_IP --Line cn_mobile_qinghai --TTL 60)
echo $QINGHAI_CM_UpdateDomainRecord_Result
# 陕西移动
# 获取陕西移动 CDN 调度结果
SHAANXI_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.137.130.3")
# 获取陕西移动 CDN 调度结果的 IP 地址
SHAANXI_CM_IP=$(echo $SHAANXI_CM_CDN | jq -r '.Answer[0].data')
echo $SHAANXI_CM_IP
# 获取陕西移动记录详情
result_SHAANXI_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_shaanxi --Status Enable --SearchMode ADVANCED)
# 获取陕西移动记录详情的 RecordID
SHAANXI_CM_RecordID=$(echo $result_SHAANXI_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHAANXI_CM_RecordID
# 修改陕西移动记录
SHAANXI_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHAANXI_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHAANXI_CM_IP --Line cn_mobile_shaanxi --TTL 60)
echo $SHAANXI_CM_UpdateDomainRecord_Result
# 山东移动
# 获取山东移动 CDN 调度结果
SHANDONG_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.201.96.130")
# 获取山东移动 CDN 调度结果的 IP 地址
SHANDONG_CM_IP=$(echo $SHANDONG_CM_CDN | jq -r '.Answer[0].data')
echo $SHANDONG_CM_IP
# 获取山东移动记录详情
result_SHANDONG_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_shandong --Status Enable --SearchMode ADVANCED)
# 获取山东移动记录详情的 RecordID
SHANDONG_CM_RecordID=$(echo $result_SHANDONG_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHANDONG_CM_RecordID
# 修改山东移动记录
SHANDONG_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHANDONG_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHANDONG_CM_IP --Line cn_mobile_shandong --TTL 60)
echo $SHANDONG_CM_UpdateDomainRecord_Result
# 上海移动
# 获取上海移动 CDN 调度结果
SHANGHAI_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.136.112.50")
# 获取上海移动 CDN 调度结果的 IP 地址
SHANGHAI_CM_IP=$(echo $SHANGHAI_CM_CDN | jq -r '.Answer[0].data')
echo $SHANGHAI_CM_IP
# 获取上海移动记录详情
result_SHANGHAI_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_shanghai --Status Enable --SearchMode ADVANCED)
# 获取上海移动记录详情的 RecordID
SHANGHAI_CM_RecordID=$(echo $result_SHANGHAI_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHANGHAI_CM_RecordID
# 修改上海移动记录
SHANGHAI_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHANGHAI_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHANGHAI_CM_IP --Line cn_mobile_shanghai --TTL 60)
echo $SHANGHAI_CM_UpdateDomainRecord_Result
# 山西移动
# 获取山西移动 CDN 调度结果
SHANXI_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.138.106.3")
# 获取山西移动 CDN 调度结果的 IP 地址
SHANXI_CM_IP=$(echo $SHANXI_CM_CDN | jq -r '.Answer[0].data')
echo $SHANXI_CM_IP
# 获取山西移动记录详情
result_SHANXI_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_shanxi --Status Enable --SearchMode ADVANCED)
# 获取山西移动记录详情的 RecordID
SHANXI_CM_RecordID=$(echo $result_SHANXI_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SHANXI_CM_RecordID
# 修改山西移动记录
SHANXI_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SHANXI_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SHANXI_CM_IP --Line cn_mobile_shanxi --TTL 60)
echo $SHANXI_CM_UpdateDomainRecord_Result
# 四川移动
# 获取四川移动 CDN 调度结果
SICHUAN_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.137.82.4")
# 获取四川移动 CDN 调度结果的 IP 地址
SICHUAN_CM_IP=$(echo $SICHUAN_CM_CDN | jq -r '.Answer[0].data')
echo $SICHUAN_CM_IP
# 获取四川移动记录详情
result_SICHUAN_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_sichuan --Status Enable --SearchMode ADVANCED)
# 获取四川移动记录详情的 RecordID
SICHUAN_CM_RecordID=$(echo $result_SICHUAN_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $SICHUAN_CM_RecordID
# 修改四川移动记录
SICHUAN_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $SICHUAN_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $SICHUAN_CM_IP --Line cn_mobile_sichuan --TTL 60)
echo $SICHUAN_CM_UpdateDomainRecord_Result
# 天津移动
# 获取天津移动 CDN 调度结果
TIANJIN_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.137.160.5")
# 获取天津移动 CDN 调度结果的 IP 地址
TIANJIN_CM_IP=$(echo $TIANJIN_CM_CDN | jq -r '.Answer[0].data')
echo $TIANJIN_CM_IP
# 获取天津移动记录详情
result_TIANJIN_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_tianjin --Status Enable --SearchMode ADVANCED)
# 获取天津移动记录详情的 RecordID
TIANJIN_CM_RecordID=$(echo $result_TIANJIN_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $TIANJIN_CM_RecordID
# 修改天津移动记录
TIANJIN_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $TIANJIN_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $TIANJIN_CM_IP --Line cn_mobile_tianjin --TTL 60)
echo $TIANJIN_CM_UpdateDomainRecord_Result
# 西藏移动
# 获取西藏移动 CDN 调度结果
XIZANG_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.139.73.34")
# 获取西藏移动 CDN 调度结果的 IP 地址
XIZANG_CM_IP=$(echo $XIZANG_CM_CDN | jq -r '.Answer[0].data')
echo $XIZANG_CM_IP
# 获取西藏移动记录详情
result_XIZANG_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_xizang --Status Enable --SearchMode ADVANCED)
# 获取西藏移动记录详情的 RecordID
XIZANG_CM_RecordID=$(echo $result_XIZANG_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $XIZANG_CM_RecordID
# 修改西藏移动记录
XIZANG_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $XIZANG_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $XIZANG_CM_IP --Line cn_mobile_xizang --TTL 60)
echo $XIZANG_CM_UpdateDomainRecord_Result
# 新疆移动
# 获取新疆移动 CDN 调度结果
XINJIANG_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.202.152.130")
# 获取新疆移动 CDN 调度结果的 IP 地址
XINJIANG_CM_IP=$(echo $XINJIANG_CM_CDN | jq -r '.Answer[0].data')
echo $XINJIANG_CM_IP
# 获取新疆移动记录详情
result_XINJIANG_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_xinjiang --Status Enable --SearchMode ADVANCED)
# 获取新疆移动记录详情的 RecordID
XINJIANG_CM_RecordID=$(echo $result_XINJIANG_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $XINJIANG_CM_RecordID
# 修改新疆移动记录
XINJIANG_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $XINJIANG_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $XINJIANG_CM_IP --Line cn_mobile_xinjiang --TTL 60)
echo $XINJIANG_CM_UpdateDomainRecord_Result
# 云南移动
# 获取云南移动 CDN 调度结果
YUNNAN_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.139.29.68")
# 获取云南移动 CDN 调度结果的 IP 地址
YUNNAN_CM_IP=$(echo $YUNNAN_CM_CDN | jq -r '.Answer[0].data')
echo $YUNNAN_CM_IP
# 获取云南移动记录详情
result_YUNNAN_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_yunnan --Status Enable --SearchMode ADVANCED)
# 获取云南移动记录详情的 RecordID
YUNNAN_CM_RecordID=$(echo $result_YUNNAN_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $YUNNAN_CM_RecordID
# 修改云南移动记录
YUNNAN_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $YUNNAN_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $YUNNAN_CM_IP --Line cn_mobile_yunnan --TTL 60)
echo $YUNNAN_CM_UpdateDomainRecord_Result
# 浙江移动
# 获取浙江移动 CDN 调度结果
ZHEJIANG_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=211.140.13.188")
# 获取浙江移动 CDN 调度结果的 IP 地址
ZHEJIANG_CM_IP=$(echo $ZHEJIANG_CM_CDN | jq -r '.Answer[0].data')
echo $ZHEJIANG_CM_IP
# 获取浙江移动记录详情
result_ZHEJIANG_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_zhejiang --Status Enable --SearchMode ADVANCED)
# 获取浙江移动记录详情的 RecordID
ZHEJIANG_CM_RecordID=$(echo $result_ZHEJIANG_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $ZHEJIANG_CM_RecordID
# 修改浙江移动记录
ZHEJIANG_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $ZHEJIANG_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $ZHEJIANG_CM_IP --Line cn_mobile_zhejiang --TTL 60)
echo $ZHEJIANG_CM_UpdateDomainRecord_Result
# 重庆移动
# 获取重庆移动 CDN 调度结果
CHONGQING_CM_CDN=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=218.201.4.3")
# 获取重庆移动 CDN 调度结果的 IP 地址
CHONGQING_CM_IP=$(echo $CHONGQING_CM_CDN | jq -r '.Answer[0].data')
echo $CHONGQING_CM_IP
# 获取重庆移动记录详情
result_CHONGQING_CM_RecordID=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line cn_mobile_chongqing --Status Enable --SearchMode ADVANCED)
# 获取重庆移动记录详情的 RecordID
CHONGQING_CM_RecordID=$(echo $result_CHONGQING_CM_RecordID | jq -r '.DomainRecords.Record[0].RecordId')
echo $CHONGQING_CM_RecordID
# 修改重庆移动记录
CHONGQING_CM_UpdateDomainRecord_Result=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $CHONGQING_CM_RecordID --RR $sub_domain --Type $record_type_v4 --Value $CHONGQING_CM_IP --Line cn_mobile_chongqing --TTL 60)
echo $CHONGQING_CM_UpdateDomainRecord_Result
# 默认
# 获取默认 CDN 调度结果
DEFAULT_CDN_IPv4=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.112.144.30")
# 获取默认 CDN 调度结果的 IP 地址
DEFAULT_IP_IPv4=$(echo $DEFAULT_CDN_IPv4 | jq -r '.Answer[0].data')
echo $DEFAULT_IP_IPv4
# 获取默认记录详情
result_DEFAULT_RecordID_IPv4=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line default --Status Enable --SearchMode ADVANCED)
# 获取默认记录详情的 RecordID
DEFAULT_RecordID_IPv4=$(echo $result_DEFAULT_RecordID_IPv4 | jq -r '.DomainRecords.Record[0].RecordId')
echo $DEFAULT_RecordID_IPv4
# 修改默认记录
DEFAULT_UpdateDomainRecord_Result_IPv4=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $DEFAULT_RecordID_IPv4 --RR $sub_domain --Type $record_type_v4 --Value $DEFAULT_IP_IPv4 --Line default --TTL 60)
echo $DEFAULT_UpdateDomainRecord_Result_IPv4
# 教育网
# 获取教育网 CDN 调度结果
EDUWAN_CDN_IPv4=$(curl -s "https://223.5.5.5/resolve?name=$CDNCNAME&type=$record_type_v4&edns_client_subnet=202.112.144.30")
# 获取教育网 CDN 调度结果的 IP 地址
EDUWAN_IP_IPv4=$(echo $EDUWAN_CDN_IPv4 | jq -r '.Answer[0].data')
echo $EDUWAN_IP_IPv4
# 获取教育网记录详情
result_EDUWAN_RecordID_IPv4=$(aliyun alidns DescribeDomainRecords --region cn-shenzhen --DomainName $domain --RRKeyWord $sub_domain --Type $record_type_v4 --Line edu --Status Enable --SearchMode ADVANCED)
# 获取教育网记录详情的 RecordID
EDUWAN_RecordID_IPv4=$(echo $result_EDUWAN_RecordID_IPv4 | jq -r '.DomainRecords.Record[0].RecordId')
echo $EDUWAN_RecordID_IPv4
# 修改教育网记录
EDUWAN_UpdateDomainRecord_Result_IPv4=$(aliyun alidns UpdateDomainRecord --region cn-shenzhen --RecordId $EDUWAN_RecordID_IPv4 --RR $sub_domain --Type $record_type_v4 --Value $EDUWAN_IP_IPv4 --Line edu --TTL 60)
echo $EDUWAN_UpdateDomainRecord_Result_IPv4
