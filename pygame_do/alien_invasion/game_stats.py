# !usr/bin/env python3
# -*- coding: utf-8 -*-
# Create by Jump on 2018/02/02 15:51
__author__ = 'Jump Hu'
# Github : https://github.com/jump1003
"""跟踪游戏的统计信息"""

class GameStats(object):
	"""跟踪游戏的统计信息"""
	def __init__(self, ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = True
		
	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ships_left = self.ai_settings.ship_limit
		