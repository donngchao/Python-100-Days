"""
百分制成绩转等级制成绩
90分以上，输出A
80分~89分，输出B
70分~79分，输出C
60分~69分，输出D
60分以下，输出E

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""

score = float(input('请输入成绩: '))
if score < 0:
    grade = 'unknown...'
    print('your input is not valid ...')
elif score >= 90:
    grade = 'A'
    print('good job , please continue...')
elif score >= 80:
    grade = 'B'
    print('almost good , please work harder')
elif score >= 70:
    grade = 'C'
    print('you need to be more careful next time ...')
elif score >= 60:
    grade = 'D'
    print("warning...it's a little dangerous...")
else:
    grade = 'E'
    print("oh no, you need to catch up ...")

print('对应的等级是:', grade)
