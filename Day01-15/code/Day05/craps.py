"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False

print('你破产了, 游戏结束!')
'''
你的总资产为: 1000
请下注: 10
玩家摇出了8点
玩家摇出了11点
玩家摇出了2点
玩家摇出了10点
玩家摇出了5点
玩家摇出了7点
庄家胜
你的总资产为: 990
请下注: 90
玩家摇出了9点
玩家摇出了8点
玩家摇出了8点
玩家摇出了8点
玩家摇出了12点
玩家摇出了6点
玩家摇出了12点
玩家摇出了8点
玩家摇出了11点
玩家摇出了6点
玩家摇出了9点
玩家胜
你的总资产为: 1080
请下注: 900
玩家摇出了3点
庄家胜!
你的总资产为: 180
请下注: 180
玩家摇出了8点
玩家摇出了6点
玩家摇出了7点
庄家胜
你破产了, 游戏结束!
'''