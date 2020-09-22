#!/usr/bin/env python
# encoding: utf-8
'''
@author: developer
@contact: developer
@software: test
@file: email_test.py
@time: 2020/9/21 7:51 下午
@desc:
'''

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'test@qq.com'
    receivers = ['test1@qq.com']
    message = MIMEText('This is a message send by python code.', 'plain', 'utf-8')
    message['From'] = Header('jj', 'utf-8')
    message['To'] = Header('kk', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件-test', 'utf-8')
    print(type(message))
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'passwd')
    smtper.sendmail(sender, receivers, message.as_string())
    print('finish sending email!')


if __name__ == '__main__':
    main()