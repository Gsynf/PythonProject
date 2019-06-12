#!usr/bin/env python3
#coding:utf-8
__author__ = 'hpf'
#利用蒙特卡洛方法近似计算圆周率
from random import random
from time import perf_counter
DARTS = 5000*5000
hits = 0.0
start = perf_counter()
for i in range (1,DARTS):
    x,y = random(),random()
    dist = pow(x**2+y**2,0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4*(hits/DARTS)
print("圆周率近似值为：{}".format(pi))
print("运行时间为：{:.5f}".format(perf_counter()-start))