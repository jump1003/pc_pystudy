import threading


account = 0
lock = threading.Lock()


def change_it(n):
	global account
	account += n
	account -= n


def run_thread(n):
	for i in range(1000000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Account is %d.' % account)
