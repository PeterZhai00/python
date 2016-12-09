#!/usr/bin/env python
"""
name = input ("请输入你的名字：")
print  (name)


import getpass
passwd = getpass.getpass("请输入您的密码：")
print (passwd)
"""

"""
import getpass

usr = getpass.getuser()
pwd = getpass.getpass("enter password for user %s: " % usr)
print (usr, pwd)
"""
"""
import  getpass

user = input("请输入用户名：")
pwd = getpass.getpass("请输入密码：")

if user == "zhaikun" and pwd == "zhai":
    print (欢迎%s登录 % user)
else:
    print (滚蛋)

"""

"""
#根据登录用户判断权限
# sunzhikun 管理员
# qiuyang  副管理
# zhaikun  操作员
# 其他  普通用户

name = input("请输入您的名字:")
if  name == "sunzhikun":
    print ("超级管理员")
elif name == "qiuyang":
    print  ("副管理员")
elif name == "zhaikun":
    print ("操作员")
else:
    print ("业务员")
"""
# while使用方法
# 只要条件为True 就无限循环;
"""
while True:
    print (123)
    break
    print (234)
while True:
    print (123)
    continue
    print (234)
"""
#使用 while 循环输入 1 2 3 4 5 6 8 9 10
"""
i = 0
while  i < 10:
    i = i+1
    if i == 7:
        continue
    print (i)

"""
#输出100内的所有奇数
"""

i = -1
while i < 99:
    i = i + 2
    print (i)
for i in range(1,100,2):
    print (i)
"""
#输出100内的所有偶数
"""
#形式一
for i in range(2,100,2):
    print (i)
#形式二
i = 0
while i < 100:
    i = i + 2
    print (i)
"""
#求1-2+3-4+5...99的所有数的和
#思路
#通过读题可以看到所有的奇数都是正数，所有的偶数都为负数，奇数和减去偶数和就是结果
'''
sum1,sum2 =0,0
for i in range(1,100,2):
    sum1 += i
print (sum1)
for i in range(2,100,2):
    sum2 += i
print(sum2)

sum = sum1-sum2
print (sum)
#方法二
a,b,sum=0,0,1
while sum <100:
    if sum%2==0:
        b += sum
        sum +=1
    else:
        a += sum
        sum +=1
print (a)
print (b)
print (a-b)

'''
#用户登陆（三次机会重试）
"""
user = "zhaikun"
pwd = "zhai"
count = 0
while count <3:
    userIN=input("请输入您的用户名：")
    pwdIN=input("请输入您的密码：")
    if user == userIN and pwd == pwdIN:
        print ("登录成功")
        break
#    elif user != userIN or pwd != pwdIN:
    else:
        print ("用户名密码不正确，请重新输入")
        count +=1
    if count >=3:
        print("超过次数，滚蛋")
"""

