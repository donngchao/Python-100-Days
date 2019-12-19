# encoding: utf-8
'''
@author: developer
@software: python
@file: timeout_test.py
@time: 2019/12/20 0:47
@desc:
'''
import requests
link = "http://www.baidu.com"
r = requests.get(link, timeout=100)
r = requests.get(link, timeout=0.0001)

#requests.exceptions.ReadTimeout: HTTPConnectionPool(host='127.0.0.1', port=60255): Read timed out. (read timeout=0.0001)


