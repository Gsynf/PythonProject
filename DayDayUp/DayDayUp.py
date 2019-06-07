#!usr/bin/env python3
#coding:utf-8
__author__ = 'hpf'
# 工作日工作进步，双休日休息退步1%，相比于每天都工作进步1%，工作日多努力才能追的上
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < round(pow(1+0.01, 365),2):
    dayfactor += 0.001
print("工作日努力参数是：{:.3f}".format(dayfactor))