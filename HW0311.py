# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 21:41:06 2021

@author: user
"""

#HW0311
#作業一
print("作業一：\n請隨機取數1~49取六個且不重複數字，並放入串列中")
import random
list1 = [0,0,0,0,0,0]
ok=True

while ok == True:
    #產生六個數字放在串列 list1 內
    for i in range(6):
        list1[i] = random.randint(1,49)
        
        
        
    #互相比較不重複，才可改變ok的值
    k=0
    for j in range(6):#0,1,2,3,4,5
        #不和自己比較
        if j == k: 
            continue
        
        #若數字不一樣則判斷下一對數字，使 k+1
        elif list1[j] != list1[k]:
            k += 1
            #若跑了五輪代表和其他數字都不同，即可跳出while迴圈
            if k == 5:
                ok = False
        #若有一樣的數字則跳出迴圈，取新的一輪數字 
        elif list1[j] == list1[k]:
            break
        
print("串列結果為：",list1,"\n")

#作業二
print("作業二：\n將串列[100,80,1,3,10,7]重新由小到大排列")

list2 = [100,80,1,3,10,7]
list3 = []

#每次取出最小數字pop出來再append到其他串列內
for i in range(len(list2)):
    #取得最小數字
    nubmin = min(list2)
    
    #取得其索引值
    indmin = list2.index(nubmin)
    
    #利用pop取出並利用append加入新陣列
    list2pop = list2.pop(indmin)
    list3.append(list2pop)

print("排序後的陣列為：",list3)
