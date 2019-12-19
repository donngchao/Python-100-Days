# encoding: utf-8
'''
@author: developer
@software: python
@file: requests_test_get.py
@time: 2019/12/20 0:28
@desc:
'''

import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

key_dict = {'key1':'value1', 'key2':'value2'}
r = requests.get('http://httpbin.org/get', params=key_dict, headers=headers)
print("URL info: \n", r.url)
print("Response: \n", r.text)
print("响应状态码：", r.status_code)
'''
URL info: 
 https://httpbin.org/get?key1=value1&key2=value2
Response: 
 {
  "args": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
  }, 
  "origin": "119.123.68.61, 119.123.68.61", 
  "url": "https://httpbin.org/get?key1=value1&key2=value2"
}

响应状态码： 200
'''