# encoding: utf-8
'''
@author: developer
@software: python
@file: remember_me.py
@time: 2019/12/25 23:01
@desc:
'''

import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    print("Is your name called", username, "?")
    ans = input("Please input yes or no:")
    if (ans == 'Y' or ans == 'yes') and username:
        print("Welcome back, "+username+"!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back,"+username+"!")


greet_user()