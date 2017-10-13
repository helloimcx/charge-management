## 使用方法

1. 自行安装docker
2. 命令行下进入项目文件夹
3. `docker-compose up`   下载镜像并启动项目
4. `docker exec -it chargemanagement_web_1 /bin/bash` 进入web容器内部
5. `python manage.py makemigrations`
6. `python manage.py migrate`  根据模型建表

#####  最后，浏览器地址栏输入`127.0.0.1:8000/home/index/`

# 通用数据类型 #


---
## 用户 ##

| 字段 | 类型 | 说明 | 大小|
| ---- | ---- | ---- | ----|
|    user_id  |integer|用户id|
|user_name|string|用户名|12|

---

手机
--
| 字段 | 类型 | 说明 | 大小|
| ---- | ---- | ---- | ----|
|  phone |String|手机号码|11|
|balance|double|余额|
|user_id|integer|用户id|

---


## 账单 ##

| 字段 | 类型 | 说明 | 大小|
| ---- | ---- | ---- | ----|
|phone|integer|手机号码|11|
|account|string|账目项|2|
|amount_receivable|double|应收金额|
|paid_amount|double|已缴金额|
|paid_time|datetime|时间|yyyy-mm-dd hr-mi-se|
|paid_status|boolean|状态|1|
|count|int|账目项数量（通话时长/短信数量）|

---

## 缴费记录 ##
| 字段 | 类型 | 说明 | 大小|
| ---- | ---- | ---- | ----|
|phone|integer|手机号码|11|
|place|string|缴费渠道|
|way|string|缴费方式|
|paid_amount|double|缴费金额|
|paid_time|datetime|时间|yyyy-mm-dd hr-mi-se|
|assistant|string|营业员|




---
## 账目项 ##
| 账目项 | 名称 | 单价 |
| ---- | ---- | ---- | 
|call_pay|语音收费|
|msg_pay|短信收费|


---
## 渠道 ##

| 缴费渠道 | 名称 | 
| ---- | ---- | 
|business_hall|营业厅|
|ol_business|网上营业厅|
|wechat_pay|微信|
|alipay|支付宝|

---



