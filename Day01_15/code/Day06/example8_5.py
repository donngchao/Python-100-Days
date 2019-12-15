# encoding: utf-8
'''
@author: developer
@software: python
@file: example8_5.py
@time: 2019/12/15 19:49
@desc:
'''


def describe_city(city_name, nation_name='China'):
    print(city_name.title()+" is in "+nation_name.title()+".")


describe_city('reykjavik', 'iceland')
describe_city('beijing')
describe_city('new york', 'America')
describe_city('london','britain')