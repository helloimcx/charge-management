﻿## 使用方法

1. 自行安装Docker
2. 命令行下进入项目文件夹
3. `docker-compose up`   下载镜像并启动项目
4. `docker exec -it chargemanagement_web_1 /bin/bash` 进入web容器内部
5. `python manage.py makemigrations`
6. `python manage.py migrate`  根据模型建表

#####  最后，浏览器地址栏输入`127.0.0.1:8000/home/index/`
---

### 使用 Windows 可能遇到的问题

> 1. 自行安装Docker

如果你的Windows版本无Hyper-V（比如Win10 家庭版），应下载Docker ToolBox

> 3. `docker-compose up`   下载镜像并启动项目

如果出现镜像下载缓慢甚至无法下载的问题，查看 C:/Users/USERNAME/.docker/ 是否有`daemon.json`文件，有则转到 `registry-mirrors`字段，添加一个国内的镜像源（比如 https://registry.docker-cn.com ）

运行的时候如果出现`python: can't open file 'manage.py': [Errno 2] No such file or directory`，可转到`docker-compose.yml`文件，找到`web`,去掉`volumes`字段和相应值。

> 最后，浏览器地址栏输入`127.0.0.1:8000/home/index/`

由于在Windows容器是运行在VirtualBox的Linux虚拟机之上，不能使用127.0.0.1(localhost)访问容器，所以要使用Linux虚拟机的IP而不是Windows的IP。输入`docker-machine ip default` 查看容器所在的IP（一般是192.168.99.100）然后浏览器地址栏输入`XXX.XXX.XXX.XXX:8000/home/index/`

---

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



