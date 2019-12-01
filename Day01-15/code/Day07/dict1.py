"""
定义和使用字典

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82, "诸葛亮":88}
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    print(scores['诸葛亮'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85, 无聊=99)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))  # None
    print(scores.get('李治'))  # None
    print(scores.get('武则天', 60))
    print(scores)
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))
    print(scores)
    scores.clear()
    print(scores)  #  {}


if __name__ == '__main__':
    main()
