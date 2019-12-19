# encoding: utf-8
'''
@author: developer
@software: python
@file: requests_test_post.py
@time: 2019/12/20 0:40
@desc:
'''
import requests
key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=key_dict)
print(r.url)
print(r.text)
'''
https://httpbin.org/post
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
'''