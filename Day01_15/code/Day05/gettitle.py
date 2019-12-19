# encoding: utf-8
'''
@author: developer
@software: python
@file: gettitle.py
@time: 2019/12/20 0:12
@desc:
'''
import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
r = requests.get(link, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)
with open('title_test.txt', 'a+') as f:
    f.write(title)
