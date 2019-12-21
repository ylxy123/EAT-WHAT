# @Time : 2019/12/22 3:07
# @Author : YLXY
# @File : functions.py
# -*- coding: utf-8 -*-

import pygame as pg
import sys


# 监测起始页的键盘操作
def start_events(screen_settings):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        else: