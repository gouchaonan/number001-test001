#!/usr/bin/python
# -*- coding: UTF-8 -*-

def send_money_hou(send_salary):
    if send_salary == 0:
        print("没有发工资")
    else:
        send_salary = 1000
    return send_salary


salary = send_money_hou(1000)
print(salary)
