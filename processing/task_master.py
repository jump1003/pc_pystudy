# task_master

import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送队列
task_queue = queue.Queue()
# 接受队列
result_queue = queue.Queue()

# 从BaseManager继承QueueManager
class QueueManager(BaseManager):
	pass


def return_task_queue():
	global task_queue
	return task_queue


def return_result_queue():
	global result_queue
	return result_queue

def test():
	# 注册Queue,关联queue对象
	QueueManager.register('get_task_queue', callable=return_task_queue)
	QueueManager.register('get_result_queue', callable=return_result_queue)
	# 设置端口号：8080 ，验证码：jump
	manager = QueueManager(address=('127.0.0.1', 8080), authkey=b'jump')
	# 启动Queue
	manager.start()
	# 获取通过网络获取的Queue 对象
	task = manager.get_task_queue()
	result = manager.get_result_queue()
	# 放置任务
	for i in range(10):
		n = random.randint(0, 1000)
		print('Put task %d...' % n)
		task.put(n)
	# 从result读取任务
	print('Try get result..')
	for i in range(10):
		r = result.get(timeout=10)
		print('Result: %s ' % r)
	# 关闭
	manager.shutdown()
	print('master exit.')


if __name__ == '__main__':
	freeze_support()
	test()