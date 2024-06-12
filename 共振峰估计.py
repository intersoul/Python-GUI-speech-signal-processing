from soundBase import *
from gongzhenfenggujihanhu import *
from scipy.signal import lfilter

def Formant_estimation(filepath):
    print('共振峰估计')
    plt.figure(figsize=(14, 12))

    data, fs = soundBase(filepath).audioread()
    # 预处理-预加重
    u = lfilter([1, -0.99], [1], data)

    cepstL = 6
    wlen = len(u)
    wlen2 = wlen // 2
    # 预处理-加窗
    u2 = np.multiply(u, np.hamming(wlen))
    # 预处理-FFT,取对数
    U_abs = np.log(np.abs(np.fft.fft(u2))[:wlen2])
    # 4.3.1
    freq = [i * fs / wlen for i in range(wlen2)]
    val, loc, spec = Formant_Cepst(u, cepstL)
    plt.subplot(4, 1, 1)
    plt.plot(freq, U_abs, 'k')
    plt.title('频谱')
    plt.subplot(4, 1, 2)
    plt.plot(freq, spec, 'k')
    plt.title('倒谱法共振峰估计')
    for i in range(len(loc)):
        plt.subplot(4, 1, 2)
        plt.plot([freq[loc[i]], freq[loc[i]]], [np.min(spec), spec[loc[i]]], '-.k')
        plt.text(freq[loc[i]], spec[loc[i]], 'Freq={}'.format(int(freq[loc[i]])))
    # 4.3.2
    p = 12
    freq = [i * fs / 512 for i in range(256)]
    F, Bw, pp, U, loc = Formant_Interpolation(u, p, fs)

    plt.subplot(4, 1, 3)
    plt.plot(freq, U)
    plt.title('LPC内插法的共振峰估计')

    for i in range(len(Bw)):
        plt.subplot(4, 1, 3)
        plt.plot([freq[loc[i]], freq[loc[i]]], [np.min(U), U[loc[i]]], '-.k')
        plt.text(freq[loc[i]], U[loc[i]], 'Freq={:.0f}\nHp={:.2f}\nBw={:.2f}'.format(F[i], pp[i], Bw[i]))

    # 4.3.3

    p = 12
    freq = [i * fs / 512 for i in range(256)]

    n_frmnt = 4
    F, Bw, U = Formant_Root(u, p, fs, n_frmnt)

    plt.subplot(4, 1, 4)
    plt.plot(freq, U)
    plt.title('LPC求根法的共振峰估计')

    for i in range(len(Bw)):
        plt.subplot(4, 1, 4)
        plt.plot([freq[loc[i]], freq[loc[i]]], [np.min(U), U[loc[i]]], '-.k')
        plt.text(freq[loc[i]], U[loc[i]], 'Freq={:.0f}\nBw={:.2f}'.format(F[i], Bw[i]))

    plt.savefig('./images/gongzhenfengguji.png')
    #plt.show()
    plt.close()
    print('共振峰估计完成')

if __name__ == '__main__':
    Formant_estimation('./C4_3_y.wav')