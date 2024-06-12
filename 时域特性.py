# C3_2_y.py
from scipy.io import wavfile
import matplotlib.pyplot as plt
import 分帧加窗
import timefeature
import windows
import soundBase
from 分帧加窗 import *
from timefeature import *
from windows import *
from soundBase import *

def Time_domain_characteristics(filepath):
    print("正在计算时域特征...")
    data, fs = soundBase(filepath).audioread()
    inc = 100
    wlen = 200
    win = hanning_window(wlen)
    N = len(data)
    time = [i / fs for i in range(N)]

    EN = STEn(data, win, inc)  # 短时能量
    Mn = STMn(data, win, inc)  # 短时平均幅度
    Zcr = STZcr(data, win, inc)  # 短时过零率

    X = 分帧加窗(data, win, inc)
    X = X.T
    Ac = STAc(X)
    Ac = Ac.T
    Ac = Ac.flatten()

    Amdf = STAmdf(X)
    Amdf = Amdf.flatten()

    fig = plt.figure(figsize=(14, 13))
    plt.subplot(3, 1, 1)
    plt.plot(time, data)
    plt.title('(a)语音波形')
    plt.subplot(3, 1, 2)
    frameTime = FrameTimeC(len(EN), wlen, inc, fs)
    plt.plot(frameTime, Mn)
    plt.title('(b)短时幅值')
    plt.subplot(3, 1, 3)
    plt.plot(frameTime, EN)
    plt.title('(c)短时能量')
    plt.savefig('images/energy.png')

    fig = plt.figure(figsize=(10, 13))
    plt.subplot(2, 1, 1)
    plt.plot(time, data)
    plt.title('(a)语音波形')
    plt.subplot(2, 1, 2)
    plt.plot(frameTime, Zcr)
    plt.title('(b)短时过零率')
    plt.savefig('images/Zcr.png')

    fig = plt.figure(figsize=(10, 13))
    plt.subplot(2, 1, 1)
    plt.plot(time, data)
    plt.title('(a)语音波形')
    plt.subplot(2, 1, 2)
    plt.plot(Ac)
    plt.title('(b)短时自相关')
    plt.savefig('images/corr.png')

    fig = plt.figure(figsize=(10, 13))
    plt.subplot(2, 1, 1)
    plt.plot(time, data)
    plt.title('(a)语音波形')
    plt.subplot(2, 1, 2)
    plt.plot(Amdf)
    plt.title('(b)短时幅度差')
    plt.savefig('images/Amdf.png')

    print("时域特征计算完毕！")

    #plt.show()

