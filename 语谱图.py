from windows import *
from timefeature import *
from soundBase import *

def yuputu(filepath):
    print("语谱图生成中...")
    def STFFT(x, win, nfft, inc):
        xn = enframe(x, win, inc)
        xn = xn.T
        y = np.fft.fft(xn, nfft, axis=0)
        return y[:nfft // 2, :]


    data, fs = soundBase(filepath).audioread()

    wlen = 256
    nfft = wlen
    win = hanning_window(wlen)
    inc = 128

    y = STFFT(data, win, nfft, inc)
    freq = [i * fs / wlen for i in range(wlen // 2)]
    frame = FrameTimeC(y.shape[1], wlen, inc, fs)

    plt.matshow(np.log10(np.flip(np.abs(y) * np.abs(y), 0)))
    plt.colorbar()
    plt.savefig('images/yuputu.png')
    plt.close()

    plt.specgram(data, NFFT=256, Fs=fs, window=np.hanning(256))
    plt.ylabel('Frequency')
    plt.xlabel('Time(s)')
    print("语谱图生成完成！")
    #plt.show()

# if __name__ == '__main__':    
#     filepath = "测试音频2.wav"
#     yuputu(filepath)

# import numpy as np
# import wave
# import matplotlib.pyplot as plt

# def yuputu(filepath):
#     print("语谱图生成中...")
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
#     #plt.show()
#     print("语谱图生成完成！")

# if __name__ == '__main__':    
#     filepath = "测试音频2.wav"
#     yuputu(filepath)

