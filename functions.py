# @Time : 2019/12/22 3:07
# @Author : YLXY
# @File : functions.py
# -*- coding: utf-8 -*-

import pygame as pg
import sys
from botton import Botton


# 监测起始页的键盘操作
def check_start_events(screen_settings, screen):
    botton = Botton("./image/botton.png", "./image/botton_mouse.png", "./image/botton_down.png", (400, 400))
    x, y = botton.position
    length, width = botton.Up_img.get_size()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.type == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and botton.isInBotton():
            pass

# 绘制起始页
def draw_start(screen_settings, screen):

    botton = Botton("./image/botton.png", "./image/botton_mouse.png", "./image/botton_down.png", (400, 500))
    x, y = botton.position
    length, width = botton.Up_img.get_size()
    while True:
        check_start_events(screen_settings, screen)
        screen.fill(screen_settings.bg_color)

        botton.whichImg(screen)

        pg.display.update()



