# encoding: utf-8
'''
@author: developer
@software: python
@file: example8_6.py
@time: 2019/12/15 21:07
@desc:
'''


def city_country(city_name, country_name):
    return city_name.title()+', '+country_name.title()


print(city_country('santiago', 'chile'))
print(city_country('shanghai', 'china'))
print(city_country('london', 'britain'))

'''
Santiago, Chile
Shanghai, China
London, Britain
'''