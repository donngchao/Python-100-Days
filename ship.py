# encoding: utf-8
'''
@author: developer
@software: python
@file: ship.py
@time: 2020/1/10 23:12
@desc:
'''

import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)