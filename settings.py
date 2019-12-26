# @Time : 2019/12/22 2:55
# @Author : YLXY
# @File : settings.py
# -*- coding: utf-8 -*-

import pygame as pg
import numpy as np

# 定义设置类
class Settings():
    def __init__(self):
        # 定义背景颜色
        self.bg_color = (255, 255, 255)
        # 定义屏幕尺寸
        self.screen_width = 800
        self.screen_length = 600
        # 该变量表示状态
        self.status = 0

