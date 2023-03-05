#!/usr/bin/python
# -*- coding: UTF-8 -*-
def yuan_money(yuan_saved_money):
    if yuan_saved_money != 0:
        yuan_saved_money = 1000
    else:
        print("没有工资存款")
    return yuan_saved_money


saved_money = yuan_money(1000)
print(saved_money)
