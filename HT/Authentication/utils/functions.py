# encoding: utf-8
import functools
import hashlib
import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from django.utils.crypto import get_random_string


def error_json(msg, **kw):
    if msg is None:
        msg = ""
    temp_json = {'success': False, 'msg': msg}
    temp_json.update(kw)
    return temp_json


def success_json(msg, **kw):
    if msg is None:
        msg = ""
    temp_json = {'success': True, 'msg': msg}
    temp_json.update(kw)
    return temp_json


def hash_pwd(pwd, salt=None):
    if salt:
        return hashlib.sha256((pwd + salt).encode()).hexdigest()

    salt = get_random_string(5)
    hashed_pwd = hashlib.sha256((pwd + salt).encode()).hexdigest()
    return hashed_pwd, salt


def bytes_to_json(data):
    return json.loads(data.decode()) if data.decode() else {}


def send_email(content, *destinations, header="来自solink的消息"):
    """发送email到指定的destinations

    :param content:         email文件的内容
    :param destinations:    邮件的目的地，可变参数
    :param header:          邮件的标题
    :return:
    """
    SMTP_HOST = 'localhost'
    SMTP_PORT = 25
    DEFAULT_FROM_ADDR = 'solink<do-not-reply>@so-link.org'

    msg = MIMEText(content, _charset='utf-8')
    msg['From'] = 'solink'
    msg['To'] = ','.join(destinations)
    msg['Subject'] = Header(header, 'utf-8').encode()

    smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    smtp.sendmail(DEFAULT_FROM_ADDR, destinations, msg.as_string())
    smtp.quit()
