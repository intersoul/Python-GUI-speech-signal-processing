import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
#import pygame
import threading
from PIL import Image, ImageTk

import 变幅
import 频域特性
import 变速
import 语谱图
import 时域特性
import 基音频率
import 共振峰估计
import os
import librosa
import sounddevice as sd

# 全局变量，用于存储用户选择的播放倍速
playback_speed = "1.0"  # 初始化播放速度为正常速度
playback_amplitude = "1.0"  
filepath = ""  # 全局变量，用于存储用户选择的音频文件路径

def on_closing():
    """关闭窗口时，退出程序"""
    sd.stop()  # 停止播放
    root.destroy()
    os._exit(0)  # 退出程序

def on_speed_selected(event):
    """当用户从下拉菜单中选择新的倍速时，更新全局变量"""
    global playback_speed
    playback_speed = speed_combobox.get()
    print(f"播放速度设置为：{playback_speed}倍速")

def on_amplitude_selected(event):
    """当用户从下拉菜单中选择新的倍速时，更新全局变量"""
    global playback_amplitude
    playback_amplitude = amplitude_combobox.get()
    print(f"播放幅度设置为：{playback_amplitude}幅度")

def select_audio():
    global filepath
    filepath = filedialog.askopenfilename(title="选择音频文件", filetypes=[("音频文件", "*.mp3 *.wav")])
    if filepath:
        audio_label.config(text=filepath)
        global selected_audio
        # selected_audio = "Jaychou1.wav"
        selected_audio = filepath

def play_pause_audio():
    """播放/暂停音频"""
    y, sr = librosa.load(filepath)  # 加载音频文件
    sd.play(y, sr)  # 播放音频文件


def pause_audio():
    sd.stop()  # 停止播放


def thread_play_pause_audio():
    thread = threading.Thread(target=play_pause_audio)
    thread.start()


# 新按钮定义
def extract_features():
    """执行特征提取功能，确保在分析期间暂停音频播放"""

    feature_label.config(text="正在提取特征...")

    # 当需要停止时调用
    print("正在提取特征")
    变幅.bianfu_main(filepath, float(playback_amplitude))  # 假设这是bianfu.py中需要执行的函数
    变速.change_audio_speed(filepath, float(playback_speed))
    语谱图.yuputu(filepath)
    时域特性.Time_domain_characteristics(filepath)
    频域特性.Frequency_domain_characteristics(filepath)
    #频域特性.yuputu(filepath)
    基音频率.Pitch_period_detection(filepath)
    共振峰估计.Formant_estimation(filepath)

    # 特征提取完成，显示结果图标
    feature_label.config(text="特征提取完成")


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("结果图")
    
    label = tk.Label(new_window, text="运行结果图")
    label.pack()


    def load_and_display_image(image_path, label, x, y, text):
        """加载并显示图像到指定位置，并添加描述文本"""
        try:
            image = Image.open(image_path)
            image = image.resize((200, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo
            label.place(x=x, y=y)
            tk.Label(new_window, text=text).place(x=x+105, y=y)  # 假设文本放置在图片右侧
        except IOError as e:
            print(f"Error loading image: {e}")

    def view_image(image_path):
        """打开新窗口查看图片"""
        top = tk.Toplevel(new_window)
        img = Image.open(image_path)
        img_resized = img.resize((1000, 600), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img_resized)
        image_label = tk.Label(top, image=photo)
        image_label.image = photo
        image_label.pack()
        top.title(os.path.basename(image_path))

    def load_and_setup_images():
        """加载所有图片并设置按钮"""
        images_info = [
            ("./images/bianfu.png", "变幅"),
            ("./images/biansu.png", "变速"),
            ("./images/pinyutexing.png", "频谱"),
            ("./images/yuputu.png", "语谱图"),
            ("./images/Amdf.png", "短时幅度差"),
            ("./images\corr.png", "短时自相关"),
            ("./images/ellip.png", "基音频率"),
            ("./images/energy.png", "短时幅值/能量"),
            ("./images\pitch.png", "共振峰"),
            ("./images/Zcr.png", "短时过零率"),
            ("./images/gongzhenfengguji.png", "共振峰估计"),
        ]
        row_count = 0
        col_count = 0
        for idx, (img_path, text) in enumerate(images_info):
            label = tk.Label(new_window)
            load_and_display_image(img_path, label, col_count * 250 + 100, row_count * 130 + 50, text)
            
            # 添加查看按钮
            btn = tk.Button(new_window, text="查看", command=lambda p=img_path: view_image(p))
            btn.place(x=(col_count * 250 + 100), y=row_count * 130 + 110)  # 调整按钮的位置
            
            col_count += 1
            
            # 每处理三个图片换行
            if col_count >= 3:  # 修改条件以适应三个一排的布局
                col_count = 0
                row_count += 1

    # 创建新窗口
    new_window.geometry("900x600")  # 调整主窗口大小以适应布局

    load_and_setup_images()



# 主程序开始
root = tk.Tk()
root.title("语音信号处理")
root.geometry("500x400")  # 调整窗口大小以适应所有图像

# 显示音频路径的标签
audio_label = tk.Label(root, text="未选择音频")
audio_label.place(x=10, y=50)

# 选择音频按钮
select_button = tk.Button(root, text="选择音频", command=select_audio)
select_button.place(x=100, y=100)
#select_button.pack(pady=10)

# 添加特征提取按钮
feature_button = tk.Button(root, text="提取特征", command=extract_features)
feature_button.place(x=300, y=100)
feature_label = tk.Label(root, text="未处理音频")
feature_label.place(x=300, y=50)

# 创建下拉菜单
speed_options = ["0.25", "0.35","0.5", "0.75", "1.0", "1.25", "1.5", "1.75"]  # 可供选择的倍速选项
speed_combobox = ttk.Combobox(root, values=speed_options)
speed_combobox.current(2)  # 默认选择“1.0”倍速
speed_combobox.place(x=100, y=200)
speed_label = tk.Label(root, text="选择播放速度")
speed_label.place(x=10, y=200)
# 创建下拉菜单
amplitude_options = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]  # 可供选择的倍速选项
amplitude_combobox = ttk.Combobox(root, values=amplitude_options)
amplitude_combobox.current(2)  # 默认选择“1.0”倍速
amplitude_combobox.place(x=100, y=250)
amplitude_label = tk.Label(root, text="选择幅度大小")
amplitude_label.place(x=10, y=250)

# 播放/暂停按钮
is_paused = False
play_pause_button = tk.Button(root, text="播放", command=play_pause_audio)
play_pause_button.place(x=400, y=200)

pause_button = tk.Button(root, text="暂停", command=pause_audio)
pause_button.place(x=400, y=260)

Image_button = tk.Button(root, text="结果图", command=open_new_window)
Image_button.place(x=400, y=100)

# 绑定事件处理函数
speed_combobox.bind("<<ComboboxSelected>>", on_speed_selected)
amplitude_combobox.bind("<<ComboboxSelected>>", on_amplitude_selected)

# 绑定窗口关闭事件到自定义的on_closing函数
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()