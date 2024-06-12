import librosa
import soundfile as sf

import librosa
import soundfile as sf
import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd
import matplotlib.pyplot as plt

def change_audio_speed(file_path, speed_factor):
    # 加载音频文件
    y, sr = librosa.load(file_path)

    # 改变音频速度
    y_stretched = librosa.effects.time_stretch(y, rate=speed_factor)

    # 保存处理后的音频
    output_file = "temp.wav"

    # 使用soundfile库保存处理后的音频
    sf.write(output_file, y_stretched, sr)
    print(f"处理完成，已保存至 {output_file}")


    # 加载音频文件
    audio_path = "temp.wav"
    y, sr = librosa.load(audio_path, sr=None)  # sr=None会以原始采样率加载音频

    # 绘制原始音频信号的波形
    # plt.figure(figsize=(14, 5))
    plt.plot(y, label='Original Audio')
    plt.title('Waveform of Original and Adjusted Volume Audio')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    # plt.legend()
    plt.legend(loc="upper right")  # 或者其他位置


    # 显示图形
    plt.grid(True)
    # 绘制完图形之后，在显示之前保存它
    plt.savefig('./images/biansu.png')  # 保存为PNG格式，您可以根据需要更改文件名和格式
    # # 显示图形
    #plt.show()
    print("变速音量处理完成！")


# file_path = 'Jaychou.wav'  # 这里替换为您的音频文件路径
# speed_factor = 1.0  # 示例中的速度因子，根据需要调整

# change_audio_speed(file_path, speed_factor)