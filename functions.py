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
            screen_settings.status = 2

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
        screen.blit(pg.image.load("./image/米线.png").convert_alpha(), (250, 300))
        screen.blit(pg.image.load("./image/KFC.png").convert_alpha(), (400, 300))
        screen.blit(pg.image.load("./image/麻辣烫.png").convert_alpha(), (600, 300))
        botton.whichImg(screen)
        if screen_settings.status != 0:
            break;
        pg.display.update()

# 监测转盘页的键鼠操作
def check_circle_events(screen_settings, screen):
    botton_start = Botton("./image/start_circle.png", "./image/start_circle_down.png", (400, 400))
    botton_return = Botton("./image/return.png", "./image/return_down.png", (400, 500))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.type == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and botton_start.isInBotton():  # 开始
            screen_settings.status = 2
        elif event.type == pg.MOUSEBUTTONDOWN and botton_return.isInBotton(): # 返回主菜单
            screen_settings.status = 0

# 转盘页
def draw_circle(screen_settings, screen):
    botton_start = Botton("./image/start_circle.png", "./image/start_circle_down.png", (400, 400))
    botton_return = Botton("./image/return_main.png","./image/return_main_down.png", (400, 500))
    while True:
        check_circle_events(screen_settings, screen)
        screen.fill(screen_settings.bg_color)
        botton_start.whichImg(screen)
        botton_return.whichImg(screen)
        if screen_settings.status == 0 or screen_settings.status == 2:
            break;
        pg.display.update()

def check_start_circle_events(screen_settings, screen):
    botton_return = Botton("./image/return.png", "./image/return_down.png", (500, 500))
    botton_stop = Botton("./image/STOP.png", "./image/STOP_down.png", (500, 550))
    botton_again = Botton("./image/again.png", "./image/again_down.png", (250, 500))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.type == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and botton_return.isInBotton(): # 返回主菜单
            screen_settings.status = 0
        elif event.type == pg.MOUSEBUTTONDOWN and botton_stop.isInBotton(): # 停止旋转
            screen_settings.stop = True
        elif event.type == pg.MOUSEBUTTONDOWN and botton_again.isInBotton(): # 重新开始旋转
            screen_settings.stop = False

# 开始转盘
def start_circle(screen_settings, screen):
    botton_return = Botton("./image/return.png", "./image/return_down.png", (500, 500))
    botton_stop = Botton("./image/STOP.png", "./image/STOP_down.png", (500, 550))
    botton_again = Botton("./image/again.png", "./image/again_down.png", (250, 500))
    angle = 0
    point = pg.image.load("./image/指针.png").convert_alpha()
    pointRect = point.get_rect()
    pointRect = pointRect.move((250, 250))
    stop = False
    while True:
        check_start_circle_events(screen_settings,screen)
        screen.fill(screen_settings.bg_color)
        screen.blit(pg.image.load("./image/面汤.png").convert_alpha(), (50, 50))
        screen.blit(pg.image.load("./image/炒面.png").convert_alpha(), (340, 50))
        screen.blit(pg.image.load("./image/蛋夹馍.png").convert_alpha(), (600, 50))
        screen.blit(pg.image.load("./image/杂酱面.png").convert_alpha(), (20, 220))
        screen.blit(pg.image.load("./image/汉堡大师.png").convert_alpha(), (20, 380))
        screen.blit(pg.image.load("./image/米线.png").convert_alpha(), (340, 380))
        screen.blit(pg.image.load("./image/KFC.png").convert_alpha(), (580, 220))
        screen.blit(pg.image.load("./image/麻辣烫.png").convert_alpha(), (580, 360))
        botton_return.whichImg(screen)
        botton_stop.whichImg(screen)
        botton_again.whichImg(screen)

        # 如果没有停止 ，继续旋转
        if not screen_settings.stop:
            angle += 45

        # 旋转后的图片
        newpoint = pg.transform.rotate(point , angle)
        newRect = newpoint.get_rect(center=pointRect.center)
        screen.blit(newpoint, newRect)

        if screen_settings.status == 0:
            break
        pg.display.flip()



