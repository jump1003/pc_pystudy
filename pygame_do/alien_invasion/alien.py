# !usr/bin/env python3
# -*- coding: utf-8 -*-
# Create by Jump on 2018/02/02 15:51
__author__ = 'Jump Hu'
# Github : https://github.com/jump1003
"""创建外星人"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		# 加载图像
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		# 从左上角刷新外星人
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""向左或向右移动外星人"""
		self.x += (self.ai_settings.alien_speed_factor *
					self.ai_settings.fleet_direction)
		self.rect.x = self.x
	
	def check_edges(self):
		"""碰到边缘就返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
	