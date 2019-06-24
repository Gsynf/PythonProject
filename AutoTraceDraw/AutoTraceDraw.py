#!usr/bin/env python3
#coding:utf-8
__author__ = 'hpf'
#300,0,144,1,0,1
import turtle as t
import time
t.title('自动轨迹绘制')
t.setup(800,600, 0, 0)
t.pencolor("red")
t.pensize(5)
t.fd(-150)
#数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval, line.split(","))))
    #map()函数的第一个参数是个指向函数的变量,第二个参数是一个序列,常为list,它将list中的每一个元素输入函数,最后将每个返回值合并成一个新的list返回.
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5]) #RGB三个通道
    t.fd(datals[i][0])  # 移动一定距离
    if datals[i][1]:   #左转右转
        t.rt(datals[i][2])
    else:
        t.lt(datals[i][2])

time.sleep(3)