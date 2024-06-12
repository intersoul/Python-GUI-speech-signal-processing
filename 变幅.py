import librosa
import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd
import matplotlib.pyplot as plt

def bianfu_main(filepath, volume_factor):
    print("开始变幅音量处理...",volume_factor)
    # 加载音频文件
    audio_path = filepath
    y, sr = librosa.load(audio_path, sr=None)  # sr=None会以原始采样率加载音频

    # volume_factor = 2

    # 改变音量（注意避免过大声导致失真或损坏扬声器）
    y_volume_adjusted = y * volume_factor

    # 确保调整后的信号值在合适的范围内，避免溢出
    y_volume_adjusted = np.clip(y_volume_adjusted, -1.0, 1.0)
    # 如果你想将修改后的音频保存到文件，可以使用如下代码
    output_path = 'Jaychou_volume_adjusted.wav'
    write(output_path, sr, np.int16(y_volume_adjusted * 32767))

    # # 播放音频
    # sd.play(y_volume_adjusted, sr)

    # # 等待音频播放完成
    # sd.wait()

    # 绘制原始音频信号的波形
    # plt.figure(figsize=(14, 5))
    plt.plot(y, label='Original Audio')
    plt.title('Waveform of Original and Adjusted Volume Audio')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.legend()

    # 绘制调整音量后音频信号的波形
    plt.plot(y_volume_adjusted, label='Adjusted Volume Audio', alpha=0.5)
    plt.legend()

    # 显示图形
    # plt.grid(True)
    # 绘制完图形之后，在显示之前保存它
    plt.savefig('./images/bianfu.png')  # 保存为PNG格式，您可以根据需要更改文件名和格式
    # # 显示图形
    # plt.show()
    print("1. 变幅音量处理成功完成！")

# if __name__ == '__main__':
#     filepath = 'Jaychou.wav'
#     volume_factor = 0.5
#     bianfu_main(filepath, volume_factor)

