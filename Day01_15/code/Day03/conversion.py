"""
英制单位英寸和公制单位厘米互换

this program is used to convert differt units number
"""

value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
elif unit == 'km' or unit == '公里':
    print('%f公里 = %f米' % (value, value*1000))
else:
    print('请输入有效的单位')
'''
请输入长度: 9
请输入单位: in
9.000000英寸 = 22.860000厘米
'''