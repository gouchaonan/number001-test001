#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import money
# import send_money

from money import saved_money
from send_money import salary


def select_zong_money(zong_send_money):
    return zong_send_money


select_money = select_zong_money(saved_money + salary)
print(select_money)
