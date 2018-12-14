# -*- coding:utf-8 -*-
import vapaa
import time

#實作2 :基礎判斷
### windows 10 中文亂碼修正
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
###

#取目前溫度
vapaa = vapaa.conn('COM4')
temp=int(vapaa.ai(0,'T'))

#判斷溫度到多少，打開開關給水
if temp < 40 :
    vapaa.do(0,0)
    print ("現在溫度",temp, '開關：開')
else:
    vapaa.do(0,1)
    print ("現在溫度",temp, '開關：開')