# encoding: utf-8
'''
@author: developer
@software: python
@file: downloadPic.py
@time: 2019/12/17 23:13
@desc:
'''

import re
import requests
from urllib import error
from bs4 import BeautifulSoup  #从bs4这个库导入BeautifulSoup
import os

num = 0
numPicture = 0
file = ''
List = []

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}


def find(url):
    global List
    print('We are now searching the total number of pictures , please wait a moment.....')
    t = 0
    i = 1
    s = 0

    while t < 1000:
        Url = url + str(t)
        try:
            Result = requests.get(Url, timeout=20, headers=headers)
        except BaseException:
            t = t + 60
            continue
        else:
            result = Result.text
            pic_url = re.findall('"objURL":"(.*?)",', result, re.S)  # 先利用正则表达式找到图片url
            s += len(pic_url)
            if len(pic_url) == 0:
                break
            else:
                List.append(pic_url)
                t = t + 60
    return s


def recommend(url):
    Re = []
    try:
        html = requests.get(url, headers=headers)
    except error.HTTPError as e:
        return
    else:
        html.encoding = 'utf-8'
        bsObj = BeautifulSoup(html.text, 'html.parser')  #使用BeautifulSoup解析
        div = bsObj.find('div', id='topRS')
        if div is not None:
            listA = div.findAll('a')
            for i in listA:
                if i is not None:
                    Re.append(i.get_text())
        return Re


def downloadPicture(html, keyword):
    global num
    # t =0
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
    print('找到关键词:' + keyword + '的图片，即将开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(num + 1) + '张图片，图片地址:' + str(each))
        try:
            if each is not None:
                pic = requests.get(each, timeout=20, headers=headers)
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:
            string = file + r'/' + keyword + '_' + str(num) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num += 1
        if num >= numPicture:
            return


if __name__ == '__main__':  # 主函数入口
    word = input("请输入搜索关键词(可以是人名，地名等): ")
    # add = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%BC%A0%E5%A4%A9%E7%88%B1&pn=120'
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
    tot = find(url)
    Recommend = recommend(url)  # 记录相关推荐
    print('经过检测%s类图片共有%d张' % (word, tot))
    numPicture = int(input('请输入想要下载的图片数量 '))
    file = input('请建立一个存储图片的文件夹，输入文件夹名称即可')
    y = os.path.exists(file)
    while y == 1:
        print('该文件夹已存在，请重新输入')
        file = input('请建立一个存储图片的文件夹，输入文件夹名称即可')
        y = os.path.exists(file)

    os.mkdir(file)
    t = 0
    tmp = url
    while t < numPicture:
        try:
            url = tmp + str(t)
            result = requests.get(url, timeout=20, headers=headers)
            print(url)
        except error.HTTPError as e:
            print('网络错误，请调整网络后重试')
            t = t + 60
        else:
            downloadPicture(result.text, word)
            t = t + 60

    print('Searching ending, Thank you!')
    print('Guess you like')
    for re in Recommend:
        print(re, end='  ')
