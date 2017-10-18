import os, time, random
from multiprocessing import Pool


def longtime_process(name):
	print('Run %s task (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('Task %s runs %0.2f seconds...' % (name, (end - start)))


if __name__ == '__main__':
	print('Parent process %s...' % os.getpid())
	p = Pool(3)
	for i in range(5):
		p.apply_async(func=longtime_process, args=(i,))
	print('Please waiting for process done...')
	p.close()
	p.join()
	print('All taskes is done.')
