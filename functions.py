# @Time : 2019/12/22 3:07
# @Author : YLXY
# @File : functions.py
# -*- coding: utf-8 -*-

import pygame as pg
import sys
from botton import Botton
import turtle


# 监测起始页的键盘操作
def check_start_events(screen_settings, screen):
    botton = Botton("./image/botton.png", "./image/botton_mouse.png", (400, 500))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.type == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and botton.isInBotton():
            screen_settings.status = 1

# 绘制起始页
def draw_start(screen_settings, screen):

    botton = Botton("./image/botton.png", "./image/botton_mouse.png", (400, 500))
    title_image = pg.image.load("./image/title.png").convert_alpha()
    面汤 = pg.image.load("./image/面汤.png").convert_alpha()
    # 炒面
    # 蛋夹馍
    # 杂酱面
    # 汉堡大师
    # 米线
    # 肯德基
    # 麻辣烫
    x, y = botton.position
    length, width = botton.Up_img.get_size()
    while True:
        check_start_events(screen_settings, screen)
        screen.fill(screen_settings.bg_color)
        screen.blit(title_image, (0, 50))
        screen.blit(pg.image.load("./image/面汤.png").convert_alpha(), (30, 200))
        screen.blit(pg.image.load("./image/炒面.png").convert_alpha(), (200, 200))
        screen.blit(pg.image.load("./image/蛋夹馍.png").convert_alpha(), (400, 200))
        screen.blit(pg.image.load("./image/杂酱面.png").convert_alpha(), (600, 200))
        screen.blit(pg.image.load("./image/汉堡大师.png").convert_alpha(), (30, 300))
        screen.blit(pg.image.load("./image/米线.png").convert_alpha(), (200, 300))
        screen.blit(pg.image.load("./image/KFC.png").convert_alpha(), (400, 300))
        screen.blit(pg.image.load("./image/麻辣烫.png").convert_alpha(), (600, 300))
        botton.whichImg(screen)
        if screen_settings.status != 0:
            break;
        pg.display.update()

# 监测转盘页的键鼠操作
def check_circle_events(screen_settings, screen):
    botton_start = Botton("./image/start_circle.png", "./image/start_circle_down.png", (400, 500))
    botton_return = Botton("./image/return.png", "./image/return_down.png", (400, 500))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.type == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and botton_start.isInBotton():
            pass
        elif event.type == pg.MOUSEBUTTONDOWN and botton_return.isInBotton():
            pass


# 转盘页
def draw_circle(screen_settings, screen):
    botton_start = Botton("./image/start_circle.png", "./image/start_circle_down.png", (400, 400))
    botton_return = Botton("./image/return.png","./image/return_down.png", (400, 500))
    while True:
        check_circle_events(screen_settings, screen)
        screen.fill(screen_settings.bg_color)
        botton_start.whichImg(screen)
        botton_return.whichImg(screen)
        if screen_settings.status == 0:
            break;
        pg.display.update()


