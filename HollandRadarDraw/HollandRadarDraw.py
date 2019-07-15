#!usr/bin/env python3
#coding:utf-8
__author__ = 'hpf'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
radar_labels = np.array(['研究型(I)', '艺术型(A)', '社会型(S)', \
                         '企业型(E)', '常规型(C)', '现实型(R)'])    #雷达标签
nAttr = 6
data = np.array([[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
                 [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
                 [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
                 [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
                 [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
                 [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]])   #数据值
data_labels = ('艺术家', '实验员', '工程师', '推销员', '社会工作者', '记事员')
angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)   #在0到2*np.pi之间返回nAttr个均匀分布的样本,endpoint为false,不包括2*np.pi这个stop端点

data = np.concatenate((data, [data[0]]))  #沿着指定的轴（axis=0 by default）加入一系列数组
angles = np.concatenate((angles, [angles[0]])) #这两行的用意不是很懂
#print(data)
#print(angles)


fig = plt.figure(facecolor="white")  #窗口背景颜色为白色
plt.subplot(111, polar=True)  #表示分为1行1列,占用第一个.子图的投影类型为polar
plt.plot(angles, data, 'o-', linewidth=1, alpha=0.2) #alpha是透明度
plt.fill(angles, data, alpha=0.25) #填充x轴和曲线y之间区域
plt.thetagrids(angles * 180 / np.pi, radar_labels, frac=1.2)  #设置极坐标网格θ位置
plt.figtext(0.52, 0.95, '霍兰德人格分析', ha='center', size=20)
legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)   #在当前axes放置legend标签,loc为标签位置,labelspacing为行距
plt.setp(legend.get_texts(), fontsize='large')  #设置property属性
plt.grid(True)
plt.savefig('holland_radar.jpg')
plt.show()
