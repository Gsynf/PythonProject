#!usr/bin/env python3
#coding:utf-8
__author__ = 'hpf'
#《哈姆雷特》词频统计
def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()  #全部转换为小写
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")
    return  txt

hamletTxt = getText()
words = hamletTxt.split()  #默认所有空字符为分隔符，包括空格、换行\n、制表符\t等
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{:<10}{:>5}".format(word, count))