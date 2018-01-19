# import socket, select
#
# # host = socket.gethostname()
# port = 8888
# addr = ("127.0.0.1", port)
#
# inputs = []
# fd_name = {}
#
#
# def who_in_room(w):
# 	name_list = []
# 	for k in w:
# 		name_list.append(w[k])
#
# 	return name_list
#
#
# def conn():
# 	print('running')
# 	ss = socket.socket()
# 	ss.bind(addr)
# 	ss.listen(5)
#
# 	return ss
#
#
# def new_coming(ss):
# 	client, add = ss.accept ()
# 	print('welcome %s %s' % (client, add))
# 	wel = '''''welcome into the talking room . please decide your name.....'''
# 	try:
# 		client.send(wel)
# 		name = client.recv(1024)
# 		inputs.append(client)
# 		fd_name[client] = name
#
# 		nameList = "Some people in talking room, these are %s" % (who_in_room (fd_name))
# 		client.send(nameList)
#
# 	except Exception as e:
# 		print(e)
#
#
# def server_run():
# 	ss = conn()
# 	inputs.append(ss)
#
# 	while True:
# 		r, w, e = select.select(inputs, [], [])
# 		for temp in r:
# 			if temp:
# 				new_coming(temp)
# 			else:
# 				disconnect = False
# 				try:
# 					data = temp.recv (1024)
# 					data = fd_name[temp] + ' say : ' + data
# 				except socket.error:
# 					data = fd_name[temp] + ' leave the room'
# 					disconnect = True
#
# 				if disconnect:
# 					inputs.remove (temp)
# 					print(data)
# 					for other in inputs:
# 						if other != ss and other != temp:
# 							try:
# 								other.send(data)
# 							except Exception as e:
# 								print(e)
# 					del fd_name[temp]
#
# 				else:
# 					print(data)
#
# 					for other in inputs:
# 						if other != ss and other != temp:
# 							try:
# 								other.send(data)
# 							except Exception as e:
# 								print(e)
#
#
# if __name__ == '__main__':
# 	server_run()
#
# # import socket
# # import threading
# # import time, re
# #
# # s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# # s.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# # s.bind (('127.0.0.1', 9999))
# # CONNECTION_LIST = []
# # Owner_list = []
# # s.listen (5)
# # print ('Waiting for connection...')
# #
# #
# # def tcp_link(sock, addr):
# # 	print ('Accept new connection from %s:%s...' % addr)
# # 	# CONNECTION_LIST.append(sock)
# # 	sock.send (b'Welcome!')
# # 	while True:
# # 		data = sock.recv (1024)
# # 		time.sleep (1)
# # 		owner_m = re.match (r'^(Owner:)(.+)', data.decode ('utf-8'))
# # 		if owner_m:
# # 			Owner_list.append (owner_m.group (2))
# # 			for usr in Owner_list:
# # 				sock.send (str.encode ('Owner:' + usr))
# # 		else:
# # 			# 	print(Owner_list)
# # 			# if not data or data.decode('utf-8') == 'exit':
# # 			# 	break
# # 			# datain = input('Input:')
# # 			sock.sendall (data)
# # 	# sock.send(str.encode(datain))
# # 	# for conn_socket in CONNECTION_LIST:
# # 	# 	try:
# # 	# 		conn_socket.send(data)
# # 	# 		print(conn_socket)
# # 	# 	except :
# # 	# 		conn_socket.close()
# # 	# CONNECTION_LIST.remove(conn_socket)
# # 	# sock.close()
# # 	print ('Connection from %s: %s closed' % addr)
# #
# #
# # while True:
# # 	# 接受一个新连接
# # 	sock, addr = s.accept ()
# # 	CONNECTION_LIST.append (sock)
# # 	t = threading.Thread (target=tcp_link, args=(sock, addr))
# # 	t.start ()
# # # for conn_socket in CONNECTION_LIST:
# # # 	try:
# # # 		# 创建新线程处理连接
# # # 		t = threading.Thread (target=tcp_link, args=(conn_socket, addr))
# # # 		t.start ()
# # # 	except:
# # # 		# conn_socket.close ()
# # # 		CONNECTION_LIST.remove (conn_socket)
#
#  """第二版"""
# # import socket,select
# #
# # host = "127.0.0.1"
# # port = 9999
# # addr = (host, addr)
# #
# # # 存连接客户端
# # connect_list = []
# # # 存用户名，key:客户端名字，value:客户端ip地址
# # conn_name = {}
# #
# # def who_in_room(c):
# # 	name_list = []
# # 	for owner in c:
# # 		name_list.append(c[owner])
# # 	return name_list
# #
# # # 建立服务器端口
# # def connect():
# # 	print('Waiting for connection...')
# # 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 	s.bind(addr)
# # 	s.listen(5)
# # 	return s
# #
# # def new_connect(s):
# # 	sock, addr = s.accept()
# # 	print('Accept new connection from %s:%s...' % (sock, addr))
# # 	try:
# # 		sock.sendall(b'welcome into the talking room .')
# # 		owner = sock.recv(1024).decode('utf-8')
# # 		connect_list.append(sock)
# # 		conn_name[sock] = owner
# #
# # 		nameList = 'Some people in chat_room,these are %s' % (who_in_room(conn_name))
# # 	except Exception as e:
# # 		print(e)
# #
# # def server_run():
# #
# # 	s = connect()
# # 	connect_list.append(s)
# #
# # 	while True:
# # 		r,w,e = select.select(connect_list,[],[])
# # 		for sock in r:
# # 			if sock == s:
# # 				new_connect(s)
# # 			else:
# # 				disconnect = False
# # 				try:
# # 					data = sock.recv(1024).decode('utf-8')
# # 					msg = conn_name[sock]+'say:'+data
# # 				except socket.error:
# # 					msg = conn_name[sock]+'leave the room'
# # 					disconnect = True
# #
# # 				if disconnect:
# # 					connect_list.remove(sock)
# # 					print(msg)
# # 					for other in connect_list:
# # 						if other!=s and other!=sock:
# # 							try:
# # 								other.sendall(str.encode(msg))
# # 							except Exception as e:
# # 								print(e)
# # 					del conn_name[sock]
# # 				else:
# # 					print(msg)
# # 					for other in connect_list:
# # 						if other!=s and other!=sock:
# # 							try:
# # 								other.sendall(str.encode(msg))
# # 							except Exception as e:
# # 								print(e)
# #
# # if __name__=='__main__':
# # 	server_run()