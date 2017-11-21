# 关于使用模板导航栏

## 客户导航栏 

导航栏文件`base_customer.html`分三部分，使用三个tag来标识：
> `base_customer_top_css`: 引用 css 文件
> 
> `base_customer_body`: 正文
>
> `base_customer_bottom_js`: 引用 js 文件
>
根据需要覆盖相应的部分，具体做法是将你的代码包裹在 ```{% block tag %} ... {% endblock tag %} ```。

例如有一个网页 helloworld.html：

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>helloworld</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
    </html>
    
要应用导航栏，那么：

1. 在html文件顶部添加：
    
    {% extends base_customer.html %}
    
    {% load staticfiles %}    


2. 要覆盖 `base_customer_body` ，则以 {% block base_customer_body %} 和 {% endblock base_customer_body %} 包裹代码：

```
{% extends base_customer.html %}
{% load staticfiles %}  
{% block base_customer_body %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>helloworld</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
</html>
{% endblock base_customer_body %}
```
    
## 营业员导航栏

导航栏文件`base_worker.html`分三部分，使用三个tag来标识：
> `base_worker_top_css`: 引用 css 文件
> 
> `base_worker_body`: 正文
>
> `base_worker_bottom_js`: 引用 js 文件
>
使用用法与 `base_customer.html` 一致。

## 关于使用其它插件
引用其它插件应该要覆盖对应的css, js代码块。有些插件不能加载两次（比如`jquery`），原因未知。
所以在这种情况下应在块中引用所有即将用到资源，例如`jquery`和`bootstrap`的文件或url或纯文本。

