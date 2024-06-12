import numpy as np
import wave
import matplotlib.pyplot as plt

def Frequency_domain_characteristics(filepath):
    print("正在计算频域特性...")    
    # f = wave.open(r"Jaychou.wav", "rb")
    f = wave.open(filepath, "rb")
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = f.readframes(nframes)
    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data = wave_data*1.0/(max(abs(wave_data)))
    fft_signal = np.fft.fft(wave_data)     #语音信号FFT变换
    fft_signal = abs(fft_signal)#取变换结果的模
    plt.figure(figsize=(10,4))
    time=np.arange(0,nframes)*framerate/nframes
    plt.plot(time,fft_signal,c="g")
    plt.grid()
    plt.savefig("./images/pinyutexing.png")

    print("频域特性计算完成！")
    #plt.show()

# def yuputu(filepath):

#     print("正在计算语谱图...")
#     def windows(name='Hamming', N=20):
#         # Rect/Hanning/Hamming
#         if name == 'Hamming':
#             window = np.array([0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1)) for n in range(N)])
#         elif name == 'Hanning':
#             window = np.array([0.5 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) for n in range(N)])
#         elif name == 'Rect':
#             window = np.ones(N)
#         return window
#     f = wave.open(filepath, "rb")
#     params = f.getparams()
#     nchannels, sampwidth, framerate, nframes = params[:4]
#     str_data = f.readframes(nframes)
#     wave_data = np.fromstring(str_data, dtype=np.short)
#     wave_data = wave_data*1.0/(max(abs(wave_data)))
#     plt.specgram(wave_data,Fs = framerate, window=windows("Hanning",256),scale_by_freq = True, sides = 'default')
#     plt.savefig("./images/yuputu.png")

#     print("语谱图计算完成！")
#     #plt.show()
