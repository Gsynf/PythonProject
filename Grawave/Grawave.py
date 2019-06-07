#!usr/bin/env python3
#引力波：物理学中，因为时空弯曲对外以辐射形式传播的能量。
#coding:utf-8
__author__ = 'hpf'
import numpy as np
import matplotlib.pyplot as plt
#用于读取波形的库
from scipy.io import wavfile

#原始采集的引力波
rate_h, hstrain = wavfile.read(r"H1_Strain.wav", "rb")
rate_l, lstrain = wavfile.read(r"L1_Strain.wav", "rb")
# reftime, ref_H1 = np.genfromtxt('GW150914_4_NR_waveform_template.txt').transpose()
reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose()  # 使用python123.io下载文件，引力波理想模板

htime_interval = 1 / rate_h  #求倒数，得到波形的时间间隔
ltime_interval = 1 / rate_l
fig = plt.figure(figsize=(12, 6))

# 丢失信号起始点
htime_len = hstrain.shape[0] / rate_h  #shape[0]读取数据第一维度，也就是数据点的个数，除以rate,得到函数在坐标轴上的总长度
htime = np.arange(-htime_len / 2, htime_len / 2, htime_interval)  #处理成以原点为中心
plth = fig.add_subplot(221)
plth.plot(htime, hstrain, 'y')
plth.set_xlabel('Time (seconds)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')

ltime_len = lstrain.shape[0] / rate_l
ltime = np.arange(-ltime_len / 2, ltime_len / 2, ltime_interval)
pltl = fig.add_subplot(222)
pltl.plot(ltime, lstrain, 'g')
pltl.set_xlabel('Time (seconds)')
pltl.set_ylabel('L1 Strain')
pltl.set_title('L1 Strain')

pltref = fig.add_subplot(212)
pltref.plot(reftime, ref_H1)
pltref.set_xlabel('Time (seconds)')
pltref.set_ylabel('Template Strain')
pltref.set_title('Template')
fig.tight_layout()

plt.savefig("Gravitational_Waves_Original.png")
plt.show()
plt.close(fig)