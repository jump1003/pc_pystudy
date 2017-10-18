import time, threading


def loop_t():
	print('Thread %s is running...' % threading.current_thread ().name)
	n = 0
	while n < 5:
		n += 1
		start = time.time()
		time.sleep(1)
		end = time.time()
		print('Thread %s >>> %s,using %.2f seconds' %(threading.current_thread().name, n, (end-start)))
	print('Thread %s ended.' % threading.current_thread ().name)


print('Thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop_t, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)
