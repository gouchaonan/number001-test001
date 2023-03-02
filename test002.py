#!/usr/bin/python
# -*- coding: UTF-8 -*-
from openpyxl import load_workbook
from openpyxl import Workbook
"""
加载已存在的工作簿
"""
#实例化
wb=Workbook()
wb = load_workbook('/Users/gouchaonan/Desktop/abcd.xlsx') # openpyxl第三方库只能处理.xlsx格式的Excel表格
print(wb)
#获取worksheet对象
ws=wb.active
print(ws)

"""
新建名为XXX的工作簿
"""
b = Workbook('abc.xlsx')    #新建名为abc的工作簿
wb.save('abc.xlsx')         #保存工作簿，完成新工作簿的建立(将覆盖同名文件且无警告）

#打开excel文件
ws= wb.active        #激活当前sheet表
print(wb.sheetnames)  #打印工作的表的名字
print(ws['A1'].value)  # 获取指定位置的单元格对象

