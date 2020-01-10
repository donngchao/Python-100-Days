# encoding: utf-8
'''
@author: developer
@software: python
@file: alien_invasion.py
@time: 2020/1/10 22:52
@desc:
'''

import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    while True:
        screen.fill(ai_setting.bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


run_game()