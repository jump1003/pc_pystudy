# !usr/bin/env python3
# -*- coding: utf-8 -*-
# Create by Jump on 2018/02/02 15:51
__author__ = 'Jump Hu'
# Github : https://github.com/jump1003
"""创建Pygame窗口以及相应用户输入"""
import pygame
import pygame_do.alien_invasion.game_functions as gf
from pygame.sprite import Group
from pygame_do.alien_invasion.settings import Settings
from pygame_do.alien_invasion.ship import Ship
from pygame_do.alien_invasion.game_stats import GameStats

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	stats = GameStats(ai_settings)
	# screen = pygame.display.set_mode((1100, 600))
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	#设置背景色
	# bg_color = (230, 230, 230)
	# 创建飞船
	ship = Ship(ai_settings, screen)
	# 创建子弹编组和外星人编组
	bullets = Group()
	aliens = Group()
	# 创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	# 开始游戏循环
	while True:
		# 监视键盘鼠标事件
		gf.check_events(ai_settings, screen, ship, bullets)
		if stats.game_active:
			#每次循环重绘屏幕，实现平滑效果
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

		
if __name__ == '__main__':
	run_game()
