# -*- coding:utf-8 -*-
import vapaa
import time

#實作1 :起手式
vapaa = vapaa.conn('COM4') #請依com編號修改
print (vapaa.ai(0,'RH')) #ai(端口, 連接感測器類型：T:溫度 | RH:溼度 | soil:土壤)
vapaa.do(0,0) #do(端口, 0:開 | 1:關)