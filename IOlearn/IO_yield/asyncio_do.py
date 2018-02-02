# import asyncio
# import threading
# import time
#
# @asyncio.coroutine
# def hello():
# 	print('Hello World! %s (%s)' % (time.strftime('%H:%M:%S', time.localtime()), threading.currentThread()))
# 	# 异步调用asyncio.sleep(1)
# 	yield from asyncio.sleep(2)
# 	print('Hello again! %s (%s)' % (time.strftime('%H:%M:%S', time.localtime()), threading.currentThread()))
#
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# # 执行coroutine
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
import asyncio



def wget(host):
	print('wget %s...' % host)
	connect = asyncio.open_connection(host, 80)
	reader, writer = yield from connect
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line = yield from reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
	writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.baidu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
