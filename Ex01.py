# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:46:51 2021

@author: user
"""

#if和、else、和elif練習
#print("")
weightstr=input("請輸入您的體重：")
weight=int(weightstr)
if weight >= 100:
    print("體重太重囉！該減肥了")
    
elif weight >= 80:
    print("體重有點重，該運動了。")
    
elif weight >= 60:
    print("體重適中")
    
elif weight >= 40:
    print("體重過輕了")
    
else :
    print("紙片人您好~")

print("(程式執行完畢)")












