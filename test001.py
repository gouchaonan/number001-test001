import operator

print("helle,word")
str_a = "checkio"
print(str_a[1:4:2])
list1 = ['physics', 'chemistry', 'ertyu', 'fghjk']
print(list1)
del list1[2]
print("After deleting value at index 2 : ")
print(list1)
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]:", list1[0])
print("list2[1:5]:", list2[1:5])

list001 = []
list001.append('shajfa')
list001.append('jdsfjkf')
print(list001)

print(operator.eq(list1, list2))

thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)
thislist01 = ["apple", "banana", "cherry"]
mylist = thislist01.copy()
print(mylist)

list3 = ["a", "b", "c"]
list4 = [1, 2, 3]

for x in list4:
    list3.append(x)
print(list3)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple1[-4:-1])

x = ("sdfgh001", "fdfghjk002", "dfghjkl003")
y = list(x)
print(y)
y[1] = "kiwi"
x = tuple(y)
print("aaaaaaaaa")
print(x)

thistupletest = ("apple")
print(type(thistupletest))

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

thisset002 = set(("apple", "banana002", "cherry003"))  # 请留意这个双括号
print(thisset002)

thisdict = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
for key in thisdict:
    print(key, ":", thisdict[key]);

a = 0
if a == 0:
    print("a==0")
else:
    print("a!=0")

'''
money = int(input("请输入你的钱包余额"))
if money > 300:
  print("餐馆吃饭")
else:
  print("回家吃饭")
'''

'''
height=float(input("请输入您的身高（单位为米）："))
print("您的身高：",height,"米")
weight=float(input("请输入您的体重（单位为千克）："))
print("您的体重：",weight,"千克")
bmi = weight/(height*height)
if bmi<18.4:
    print("您的体重偏瘦")
if 18.5<bmi<23.9:
    print("您的体重正常，注意保持！")
if 24.0<bmi<27.9:
    print("您的体重过重 ")
if bmi>=28.0:
	print("您的体重肥胖！")
'''

'''
heigth=float(input("请输入你的身高（单位为米）："))
if 0<heigth<1.2:
  print("您无需购买火车票！")
else:
  if 1.2 <= height < 1.5:
    print("请您购买火车儿童票！")
  else:
    print("请您购买火车全价票！")
'''

'''
price=float(input("请输入商品价格:"))
cost=0
if 0<price<=200:
  cost==price
  print("您购买该商品应付金额为", cost, "元")
elif 200<price<=500:
  cost=price*0.9
  print("您购买该商品应付金额为", cost, "元")
elif 500<price<=1000:
  cost=price*0.8
  print("您购买该商品应付金额为", cost, "元")
else:
  cost=price*0.5
  print("您购买该商品应付金额为", cost, "元")
'''

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print("even列表数据是：", even)
print("odd列表数据是：", odd)

thislist003 = ["apple", "banana", "cherry"]
thislist004 = thislist003.pop()
print("pop方法返回从列表中已删除的对象:", thislist004)

print(type('Learn Python in imooc.'))

a = 3.14
b = 1.57
c = round(a * b, 2)
print(c)

# 请综合使用while和break，计算0~1000以内，所有偶数的和
'''
num = 0
sum = 0
while True:
    if num > 1001:
        break
    sum = sum + num
    num = num + 2
print(sum)
'''

# 请综合使用while和continue，计算0~1000以内，所有偶数的和
'''
num = 0
sum = 0
while num < 1002:
  num = num + 2
  if num%2==0:
    if num>1000:
      continue
    sum = sum + num
print(sum)


num = 0
sum = 0
while num <= 1000:
    num = num + 1
    if num % 2 == 1:
        continue
    sum = sum + num
print(sum)
'''

'''
L = ['Alice', 66, 'Bob', True, 'False', 100]
num=0
for i in L:
  num=num+1
  if num%2!=0:
      continue
  print(i)
'''

nums = [18, 39, 11, 34, 51, 100, 69, 71, 92, 88, 5, 75]
max = nums[0]  # 最大值是第一个元素
min = nums[0]  # 最小值是第一个元素
for num in nums:
    # 将认为的最大值与列表中的剩余元素进行比较，这里认为最大值是第一个元素，将第一个元素与第二、三、四...逐个进行比较，
    # 如果在比较的过程中遇到了比第一个元素还大的值 ，则把该元素赋值给max
    if num > max:
        max = num
    # 将认为的最小值与列表中的剩余元素进行比较，这里认为最小值是第一个元素，将第一个元素与第二、三、四...逐个进行比较，
    # 如果在比较的过程中遇到了比第一个元素还小的值 ，则把该元素赋值给min
    if min > num:
        min = num
print("-------------第二种方式-------------")
print("最大值：", max)
print("最小值", min)


def func1(e, f, g):
    """
    :param e:
    :param f:
    :param g:
    :return:
    """
    print("这是一个函数e", e)
    print("这是一个函数f", f)
    print("这是一个函数g", g)
    return


print(func1(1, 2, 3))
