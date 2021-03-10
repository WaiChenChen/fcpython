# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 21:46:33 2021

@author: user
"""
#0309HW
#作業一
#顯示數字:
#123456789
#12345678
#1234567
#...
#...
#12
#1
print("作業一：顯示數字")
for i in range(9,0,-1):  #9個數字~1個數字
    k=1  #顯示的數字，從1累加至9，此行歸零用
    for j in range(i):
        print(k,end="")
        k+=1  #累加顯示的數字
    print("")

print()
#作業二
#顯示以下圖形
#   *   
#  ***
# *****
#*******
# *****
#  ***
#   *
print("作業二：顯示圖形")
#上半，前四行
space=3#上半的起始空白數和*符號數量
dot=1
for i in range(4):#前四行
    for j in range(space):#顯示幾次(格)空白
        print(" ",end="")
    for j in range(dot):#顯示幾次「*」符號
        print("*",end="")
    space+=-1#下一行的空白數減少一個
    dot+=2#下一行的*符號增加兩個
    print()

#下半，後三行
space=1#下半的起始空白數和*符號數量
dot=5
for i in range(3):#後三行
    for j in range(space):#同上
        print(" ",end="")
    for j in range(dot):#同上
        print("*",end="")
    space+=1#下一行的空白數增加一個
    dot+=-2#下一行的*符號減少兩個
    print()

    
#作業三
#終極密碼
#會隨著猜測數字改變
import random
top = 99#上限
low = 0#下限
answer = random.randint(low,top)#答案
print("作業三：終極密碼")
print("終極密碼！請輸入0至99其中一個數字")
typein=int(input("請輸入數字："))

while (answer != typein):
    if typein > answer and typein < top:#猜測介於答案和上限，則修改上限
        top=typein
        print("請繼續！答案介於",str(low),"和",str(top),"之間")
    elif typein < answer and typein > low:#猜測介於答案和下限，則修改下限
        low=typein
        print("請繼續！答案介於",str(low),"和",str(top),"之間")
    elif typein >=top or typein <= low:#猜測並不介於上限和下限之間，顯示三行警告文字
        for three in range(3):
            print("此數字不在範圍內哦！！！")
        print("請繼續！答案介於",str(low),"和",str(top),"之間")
    else:#輸入串並非整數
        print("輸入錯誤，請輸入正整數，請重試")
    typein = int(input("請繼續輸入數字："))   
else:
    print("答對了！密碼就是：",str(answer))