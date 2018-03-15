# !usr/bin/env python3
# -*- coding: utf-8 -*-
# Create by Jump on 2018/02/02 15:51
__author__ = 'Jump Hu'
# Github : https://github.com/jump1003
"""微信模块练习"""
from wxpy import *
bot = Bot(cache_path=True)
friend_stat = bot.friends().stats()

friend_loc = []
for province, count in friend_stat['province'].items():
	if province != '':
		friend_loc.append([province, count])

friend_loc.sort(key=lambda x: x[1], reverse=True)
for item in friend_loc[:10]:
	print(item[0], item[1])

for sex,count in friend_stat["sex"].items():
	if sex == 1:
		print("MALE %d" % count)
	elif sex == 2:
		print("FEMALE %d" % count)

		