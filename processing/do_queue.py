from multiprocessing import Process, Queue
import os, time ,random


def write(q):
	print('Process %s is writing.' % os.getpid())
	for value in range(4):
		print('Push %d into %s\'s queues.' % (value, os.getpid()))
		q.put(value)
		time.sleep(random.random())


def read(q):
	print('Process %s is reading.' % os.getpid())
	while True:
		value = q.get(True)
		print('from %s\'s queue read %s ' % (os.getpid(), value))


if __name__ == '__main__':
	q = Queue()
	qw = Process(target=write, args=(q,))
	qr = Process(target=read, args=(q,))
	# 执行写入
	qw.start()
	# 执行读取
	qr.start()
	# 等待写入结束
	qw.join()
	# 强制结束读取
	qr.terminate()
