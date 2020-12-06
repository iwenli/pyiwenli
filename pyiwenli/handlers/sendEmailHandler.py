#!/usr/bin/env python
'''
Author: iwenli
License: Copyright © 2020 iwenli.org Inc. All rights reserved.
Github: https://github.com/iwenli
Date: 2020-12-06 20:49:36
LastEditors: iwenli
LastEditTime: 2020-12-06 22:57:56
Description: 发送邮件
'''
__author__ = 'iwenli'

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


class SendEmailHandler(object):
    """
    发送邮件
    """
    def __init__(self, **kwargs):
        """[实例化]
        参数：
            kwargs = {
                "host": "smtp.exmail.qq.com",
                "user": "open@iwenli.org",
                "password": os.getenv("emall_pwd"),
                "port": 465,
                "sender": "open@iwenli.org",
                "ssl":False
            }
        """
        self.user = kwargs.get("user", "open@iwenli.org")
        self.password = kwargs.get("password")
        self.host = kwargs.get("host", "smtp.exmail.qq.com")
        self.port = kwargs.get("port", 465)
        self.display = kwargs.get("display", "iwenli.org")
        self.sender = kwargs.get("sender", "open@iwenli.org")
        self.ssl = kwargs.get("ssl", True)

        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.host, self.port)
        else:
            self.smtp = smtplib.SMTP(self.host, self.port)

        self.smtp.login(self.user, self.password)

    def send(self):
        to = ['admin@iwenli.org']
        cc = ['234486036@qq.com']
        receivers = to + cc

        message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
        message['From'] = Header(self.display, 'utf-8')
        message['To'] = ",".join([
            formataddr((Header(addr, 'utf-8').encode(), addr)) for addr in to
        ])
        message['Cc'] = "，".join([
            formataddr((Header(addr, 'utf-8').encode(), addr)) for addr in cc
        ])
        message['Subject'] = Header('Python SMTP 邮件测试', 'utf-8')

        self.smtp.sendmail(self.sender, receivers, message.as_string())
        print("邮件发送成功")


if __name__ == '__main__':
    import os
    dic = {
        "host": "smtp.exmail.qq.com",
        "user": "open@iwenli.org",
        "password": os.getenv("emall_pwd"),
        "port": 465,
        "display": "iwenli.org",
        "sender": "open@iwenli.org",
        "ssl": True
    }

    handler = SendEmailHandler(**dic)
    handler.send()
