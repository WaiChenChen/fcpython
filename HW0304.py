# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:40:09 2021

@author: user
"""

#第一題：請利用for range 計算1~50(含50)之間之偶數和以及奇數和
print("第一題：請利用for range 計算1~50(含50)之間之偶數和以及奇數和")
sum_odd = 0#基數
sum_even = 0#偶數

for i in range(1,51,1):
    if i %2 ==0:#餘數為→偶數
        sum_even += i
    elif i % 2 == 1:#餘數為1→奇數
        sum_odd += i

print("奇數和為：",sum_odd)
print("偶數和為：",sum_even)

#第二題：請利用for range 印出2,4,6,8
print("第二題：請利用for range 印出2,4,6,8")
for j in range(2,9,2):
    if j < 7:
        print(j,end=",")#結尾有逗號
    else:
        print(j,end="")#結尾無逗號







