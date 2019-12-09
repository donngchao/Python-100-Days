"""
定义和使用学生类

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""

# 单下划线开头的受保护成员
def _foo():
    print('test')


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age, school, hobby):
        self.name = name
        self.age = age
        self.school = school
        self.hobby = hobby

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def getHobby(self):
        print("%s 's hobby is %s." % (self.name, self.hobby))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国大电影.' % self.name)

    def listen_music(self):
        if self.school == '外国语学校':
            print('%s likes listen to English songs' % self.name)
        else:
            print('%s likes listen to Chinese songs... ' % self.name)

def main():
    stu1 = Student('骆昊', 38, '外国语学校', '踢足球')
    stu1.study('Python程序设计')
    stu1.getHobby()
    stu1.watch_av()
    stu1.listen_music()
    stu2 = Student('王大锤', 15, '人大附中', '弹钢琴')
    stu2.study('思想品德')
    stu2.watch_av()
    stu2.getHobby()
    stu2.listen_music()
    stu3 = Student('Doraemon', 10, '外国语学校','写毛笔字')
    stu3.study('Linux')
    stu3.listen_music()
    stu3.getHobby()

if __name__ == '__main__':
    main()

'''
骆昊正在学习Python程序设计.
骆昊正在观看岛国大电影.
骆昊 likes listen to English songs
王大锤正在学习思想品德.
王大锤只能观看《熊出没》.
王大锤 likes listen to Chinese songs... 
Doraemon正在学习Linux.
Doraemon likes listen to English songs
'''