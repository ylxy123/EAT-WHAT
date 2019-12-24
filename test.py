# @Time : 2019/12/22 21:50
# @Author : YLXY
# @File : test.py
# -*- coding: utf-8 -*-

import pygame
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import time
import pyautogui as gui

# time.sleep(3)

# while True:
#     x, y = gui.position()
#     print("\r %d %d"%(x, y),end='')

# 创建窗体
root = tk.Tk()

# 窗口大小自定义
root.geometry("800x600+10+10")

# 窗口标题
root.title('获取指针实时位置')

x, y = gui.position()
# 窗口文本
txt = tk.Label(root, text="↓下面显示实时位置↓")

# 获取键盘指针位置
position = tk.Label(root, text="%d %d"%(x, y))

# 窗口布局
txt.pack()
position.pack()

# 由root窗口创建root1子窗口
# root1 = tk.Toplevel(root)

root.mainloop()


