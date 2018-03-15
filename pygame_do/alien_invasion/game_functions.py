# !usr/bin/env python3
# -*- coding: utf-8 -*-
# Create by Jump on 2018/02/02 15:51
__author__ = 'Jump Hu'
# Github : https://github.com/jump1003
"""重构"""
import sys
import pygame
from time import sleep
from pygame_do.alien_invasion.bullet import Bullet
from pygame_do.alien_invasion.alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按下"""
	if event.key == pygame.K_RIGHT:
		# 向右移动飞船
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# 向左移动飞船
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		# 向右移动飞船
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		# 向左移动飞船
		ship.moving_left = False
	
def check_events(ai_settings, screen, ship, bullets):
	"""响应鼠标键盘事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
				
def update_screen(ai_settings, screen, ship, aliens, bullets):
	"""更新屏幕上图像，并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	pygame.display.flip()


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		# 进入下一关
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)


def update_bullets(ai_settings, screen, ship, aliens, bullets):
	# 更新子弹数量
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# 检查是否有子弹击中外星人,若击中则删除子弹和外星人
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
	
		
def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
		alien = Alien(ai_settings, screen)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		aliens.add(alien)
	# 计算一行能容纳多少外星人
def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x
	# 计算多少行
def get_number_rows(ai_settings, ship_height, alien_height):
	available_space_y = (ai_settings.screen_height -
	                     (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
	
def create_fleet(ai_settings, screen, ship, aliens):
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	# 创建外星人群
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	"""响应被外星人撞到的飞船"""
	if stats.ships_left > 0:
		# 将ship_left -1
		stats.ships_left -= 1
		# 清空子弹和外星人
		aliens.empty()
		bullets.empty()
		# 创建新的外星人 以及飞船
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		# 暂停
		sleep(1)
	else:
		stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	"""检查外星人是否到达屏幕低端"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# 同飞船被撞处理
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
			break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	"""检查是否有外星人到达屏幕边缘
		然后更新所有外星人的位置
	"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	# 检测外星人和飞船的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
	
def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
	"""外星人到达边缘采取相应的措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

