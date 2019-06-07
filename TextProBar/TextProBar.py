#!usr/bin/env python3
#coding:utf-8
__author__ = 'hpf'
#文本进度条
import time
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    #\r每次回到行首，起到刷新作用，注意在IDLE中会屏蔽\r；^3.0f居中，三位数，0位小数；end=‘’取消print默认换行
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, "-"))
