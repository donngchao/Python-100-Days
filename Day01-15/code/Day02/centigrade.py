"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
'''
请输入华氏温度: 100
100.0华氏度 = 37.8摄氏度
'''


"""
将摄氏温度转换为华氏温度
F = 1.8C + 32

Version: 0.2
Author: developer
Date: 2019-11-27
"""
celcius = float(input('请输入摄氏温度：'))
fahrenheit = 1.8 * celcius + 32
print('%.2f 摄氏温度 = %.2f 华氏温度' % (celcius,fahrenheit))
print(celcius,'摄氏温度=',fahrenheit,'华氏温度')
'''
请输入华氏温度: 100
100.0华氏度 = 37.8摄氏度
请输入摄氏温度：37.8
37.80 摄氏温度 = 100.04 华氏温度
37.8 摄氏温度= 100.03999999999999 华氏温度
'''