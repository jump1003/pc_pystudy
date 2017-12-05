# -*- coding: utf-8 -*-
import hashlib
db = {}


def get_md5(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()


def register():
	global db
	print('开始注册\n')
	username = input('请输入用户名：')
	password = input('请输入账户密码：')
	password2 = input('请确认账户密码：')
	if password == password2:
		if db.__contains__(username):
			print('用户名已存在！')
		else:
			db[username] = get_md5(password + username + 'The-Salt')
			print('注册成功')
	else:
		print('两次输入的密码不一致!')


def login():
	print('正在登录\n')
	username = input('请输入用户名：')
	password = input('请输入账户密码：')
	(print('登录成功，欢迎%s\n' % username) if db[username] ==get_md5(password + username + 'The-Salt') else print('用户名或密码错误\n'))\
		if (db.__contains__(username)) else print('用户名或密码错误\n')


while True:
	print('选择操作：\n')
	print('登录--1\n注册--2\n退出--3\n')
	state = input()
	if state == '1':
		login()
	elif state == '2':
		register()
	elif state == '3':
		exit()
	else:
		print('输入错误，请重新输入！\n')



