# task_work

import time,sys,queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
	pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
server_add = '127.0.0.1'
print('Connect to server %s...' % server_add)

m = QueueManager(address=(server_add, 8080), authkey=b'jump')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
	try:
		n = task.get(timeout=1)
		print('run task %d * %d ...' % (n, n))
		r = '%d * %d = %d' % (n, n, n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')

# 处理结束
print('work is exit.')

