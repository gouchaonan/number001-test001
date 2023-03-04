import os
import time
from datetime import datetime
if not os.path.exists('/Users/gouchaonan/Desktop/test.txt'):
    os.mkdir('/Users/gouchaonan/Desktop/test.txt')
if  os.path.exists('/Users/gouchaonan/Desktop/hahaha.txt'):
    f=open('/Users/gouchaonan/Desktop/hahaha.txt','w')
    f.write("hello,os using")
    f.close()

f = open('/Users/gouchaonan/Desktop/hahaha.txt','a+',encoding = 'utf-8')
content = f.write('\n睡意沉沉，哈哈哈哈哈哈')
content = f.read()
print(content)
f.close()

#获取当前时间戳
print(time.time())
now_time=time.time()

currentDateAndTime = datetime.now()
print("The current date and time is", currentDateAndTime)
currentTime = currentDateAndTime.strftime("%H:%M:%S")
print("The current time is", currentTime)

#打印结果示例
# time.struct_time(tm_year=2023, tm_mon=3, tm_mday=5, tm_hour=0, tm_min=43, tm_sec=9, tm_wday=6, tm_yday=64, tm_isdst=0)
print(time.localtime())

# 获取前1天或N天的日期，beforeOfDay=1：前1天；beforeOfDay=N：前N天
def getdate(beforeOfDay):
    import datetime
    today = datetime.datetime.now()
    # 计算偏移量
    offset = datetime.timedelta(days=-beforeOfDay)
    # 获取想要的日期的时间
    re_date = (today + offset).strftime('%Y/%m/%d') # #号可以去除0
    return re_date

two_day_time3=getdate(2)
print(two_day_time3)


#抛出异常
try:
    num1=int(input("输入一个整数"))
    num2=int(input("输入一个被除数"))
    print(num1/num2)
except ZeroDivisionError:
    print("被除数不能为0")
except ValueError:
    print("输入的值需要是数值型整数")
finally:
    print("无论发没发生异常，都执行")