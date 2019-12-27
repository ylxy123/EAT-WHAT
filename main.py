# @Time : 2019/12/22 2:50
# @Author : YLXY
# @File : main.py
# -*- coding: utf-8 -*-

import pygame as pg
from settings import Settings
import functions as fc
from botton import Botton

screen_settings = Settings()
global screen
screen = pg.display.set_mode((screen_settings.screen_width, screen_settings.screen_length))
icon = pg.image.load("./image/eat.png").convert_alpha()
pg.display.set_icon(icon)
pg.display.set_caption("今天吃什么？？？")

def start():
    while True:
        if screen_settings.status == 0:
            fc.draw_start(screen_settings, screen)
        elif screen_settings.status == 1:
            fc.draw_circle(screen_settings, screen)
        elif screen_settings.status == 2:
            fc.start_circle(screen_settings, screen)


if __name__ == "__main__":
    pg.init()
    start()