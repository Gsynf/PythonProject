#!usr/bin/env python3
#coding:utf-8
__author__ = 'hpf'
#绘制科赫雪花
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)
def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 1 #3阶科赫雪花
    size = 400 #单条长度
    koch(size, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
    turtle.done()  #使绘图窗口在绘制完成之后不退出

main()