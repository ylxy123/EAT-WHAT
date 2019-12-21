# @Time : 2019/12/22 2:50
# @Author : YLXY
# @File : main.py
# -*- coding: utf-8 -*-

import pygame as pg
from settings import Settings

screen_settings = Settings()
screen = pg.display.set_mode(screen_settings.screen_width, screen_settings.screen_length)
pg.display.set_caption("今天吃什么？？？")

def start():
    while True:


if __name__ == "__main__":
    pg.init()