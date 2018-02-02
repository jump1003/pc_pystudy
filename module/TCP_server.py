import socket, select, threading


class ChatServer(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		# 建立字典存储已连接客户端信息
		self.clientinfo = {}
		self.sock_info = {}
		self.sock = None
		self.host = "127.0.0.1"
		self.addr = (self.host, 9999)
		self.listSocket = None
		self.tcpServer = None
		self.udpServer = None
		
	def bulidserver(self):
		print('launch threading...')
		# 建立 tcp_server
		self.tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# self.tcpServer.setblocking(False)
		# 绑定地址
		self.tcpServer.bind(self.addr)
		self.tcpServer.listen(5)
		# 建立 udp_server
		self.udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.udpServer.bind(self.addr)
		# self.udpServer.setblocking(False)
		# select数据
		self.listSocket = [self.tcpServer, self.udpServer]
	
	def run(self):
		self.bulidserver()
		
		while self.listSocket:
			rlist, wlist, elist = select.select(self.listSocket, [], [])
			if not (rlist or wlist or elist):
				print('time out')
				break
			for sock in rlist:
				self.sock = str(sock)
				# self.tcpServer表示有新客户端发出连接请求
				if sock is self.tcpServer:
					print('connecting...')
					try:
						client, addr = sock.accept()
						print('connect from %s:%s' % addr)
						client.send(b'Welcome')
						# client.setblocking(False)
						# 将新链接进来的客户端加入到listSocket
						self.listSocket.append(client)
						print(self.listSocket)
					except Exception as e:
						print(e)
						break
				elif sock is self.udpServer:
					try:
						# 表示有聊天消息发过来
						data, addr = sock.recvfrom(1024)
						# print('recvfrom：%s, from %s' % (data, addr))
						# 广播
						for key, value in self.clientinfo.items():
							sock.sendto(data, value)
							# print(self.clientinfo.items())
							# print(key + ':' + value)
					except Exception as e:
						print(e)
				else:
					try:
						# 客户端发送的命令
						command = sock.recv(1024).decode('utf-8')
						print('command: %s' % command)
						# 若command为空，则说明tcp客户端连接已断开
						if command:
							self.parse(command)
						else:
							self.listSocket.remove(sock)
					except Exception as e:
						print(e)
						self.listSocket.remove(sock)
						command_exit = 'exit:' + str(sock)
						self.parse(command_exit)
		print('out threading')
		self.tcpServer.close()
	
	def parse(self, command):
		"""解析命令"""
		key, value = command.split(':')
		if key == 'Owner':
			name, addr = value.split(',')
			print(name+':'+addr)
			host, port = addr.split('@')
			self.clientinfo[name] = (host, int(port))
			print(self.clientinfo)
			self.sendlistusr()
			self.sock_info[self.sock] = name
			print(self.sock_info)
		if key == 'exit':
			del self.clientinfo[self.sock_info[value]]
			self.sendlistusr()
	
	def sendlistusr(self):
		"""向客户端发送新的好友列表"""
		listName = 'Owner:'
		for name in self.clientinfo:
			listName += name + ';'
		print(listName)
		count = len(self.listSocket)
		for i in range(2, count):
			self.listSocket[i].sendall(str.encode(listName))


if __name__ == '__main__':
	server = ChatServer()
	server.start()
