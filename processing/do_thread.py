# import time, threading
#
#
# def loop_t():
# 	print('Thread %s is running...' % threading.current_thread ().name)
# 	n = 0
# 	while 1:
# 		n += 1
# 		start = time.time()
# 		time.sleep(1)
# 		end = time.time()
# 		print('Thread %s >>> %s,using %.2f seconds' %(threading.current_thread().name, n, (end-start)))
# 	print('Thread %s ended.' % threading.current_thread ().name)
#
#
# print('Thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop_t, name='LoopThread')
# t.start()
# # t.join()
# print('Thread %s ended.' % threading.current_thread().name)
# -*- coding: utf-8 -*-
import threading
import time


class Test (object):
	def __init__(self):
		# threading.Thread.__init__(self)
		self._sName = "machao"
		self.process()
		
	def process(self):
		# args是关键字参数，需要加上名字，写成args=(self,)
		th1 = threading.Thread (target=Test.buildList, args=(self,))
		th1.start()
		th1.join()
	
	def buildList(self):
		while True:
			print("start")
			time.sleep (3)


test = Test()
