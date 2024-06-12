import numpy as np
import wave
import matplotlib.pyplot as plt

def yuputu(filepath):
    print("语谱图生成中...")
    def windows(name='Hamming', N=20):
        # Rect/Hanning/Hamming
        if name == 'Hamming':
            window = np.array([0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1)) for n in range(N)])
        elif name == 'Hanning':
            window = np.array([0.5 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) for n in range(N)])
        elif name == 'Rect':
            window = np.ones(N)
        return window
    f = wave.open(filepath, "rb")
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = f.readframes(nframes)
    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data = wave_data*1.0/(max(abs(wave_data)))
    plt.specgram(wave_data,Fs = framerate, window=windows("Hanning",256),scale_by_freq = True, sides = 'default')
    plt.savefig("./images/语谱图.png")
    plt.show()
    print("语谱图生成完成！")

yuputu("测试音频.wav")
