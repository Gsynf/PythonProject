#!usr/bin/env python3
#coding:utf-8
#wordcloud库安装同jieba，官网下载.tar.gz链接：https://pypi.org/project/wordcloud/#files
#版本差别：参数是否有mask
__author__ = 'hpf'


import jieba
import wordcloud
from scipy.misc import imread
mask = imread("chinamap.jpg")
excludes = { }
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "uming.ttc", mask = mask
)
w.generate(txt)
w.to_file("grwordcloudm.png")