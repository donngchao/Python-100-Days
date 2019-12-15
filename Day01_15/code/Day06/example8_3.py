# encoding: utf-8
'''
@author: developer
@software: python
@file: example8_3.py
@time: 2019/12/15 19:32
@desc:
'''


def make_shirt(size='big size', slogan="I love Python"):
    print("Make a T-shirt with size: "+size+" and printed slogan: "+slogan)


make_shirt('38', 'Python is great!')
make_shirt(size='36', slogan='Java is great!')
make_shirt()
make_shirt(size='middle size')
make_shirt('small size', "I like listen to music")