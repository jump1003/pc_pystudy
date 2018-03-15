# !usr/bin/env python3
# -*- coding: utf-8 -*-
# Create by Jump on 2018/02/02 15:51
__author__ = 'Jump Hu'
# Github : https://github.com/jump1003
"""设置游戏中飞船"""
import pygame

class Ship(object):
	def __init__(self, ai_settings, screen):
		"""初始化飞船并设置初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings
		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.image_centerx = self.rect.centerx
		# 每艘新飞船放置屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		self.moving_right = False
		self.moving_left = False
	
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		# 更新位置
		self.rect.centerx = self.center
		
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)
	
	def center_ship(self):
		"""让飞船在屏幕居中"""
		self.center = self.screen_rect.centerx
		