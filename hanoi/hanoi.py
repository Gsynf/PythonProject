#!usr/bin/env python3
#coding:utf-8
__author__ = 'hpf'
#汉诺塔
count = 0
#n号小圆盘从src到dst，mid作为过渡
def hanoi(n, src, dst, mid):
    global count
    if n==1:
        print("{}:{}->{}".format(1, src, dst))
        count +=1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count +=1
        hanoi(n-1, mid, dst, src)

def main():
    hanoi(5, "A", "B", "C")
    print("共搬运了{}次".format(count))

main()
