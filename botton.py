# @Time : 2019/12/22 19:33
# @Author : YLXY
# @File : botton.py
# -*- coding: utf-8 -*-

import pygame as pg

class Botton(object):
    def __init__(self, up_img, hang_img, position):
        self.Up_img = pg.image.load(up_img).convert_alpha()
        self.Hang_img = pg.image.load(hang_img).convert_alpha()
        self.position = position

    # 判断鼠标是否在图片范围内；若是，返回True
    def isInBotton(self):
        # 获取当前指针位置
        self.mouseX, self.mouseY = pg.mouse.get_pos()
        # 获取图片位置
        x, y = self.position
        # 图片尺寸
        length, width = self.Up_img.get_size()

        in_x = x - length/2 < self.mouseX < x + length/2
        in_y = y - width/2 < self.mouseY < y + width/2

        return in_x and in_y


    # 判断该显示哪张图
    def whichImg(self, screen):
        x, y = self.position
        length, width = self.Up_img.get_size()

        if self.isInBotton():
            screen.blit(self.Hang_img, (x - length/2, y - width/2))
        else:
            screen.blit(self.Up_img, (x - length/2, y - width/2))


