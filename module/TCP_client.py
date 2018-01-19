import random
import socket,select
# import re
import threading


class TcpClient(threading.Thread):
	
	"""client for chat"""
	def __init__(self, frame):
		super(TcpClient, self).__init__()
		# 取聊天界面
		self.frame = frame
		# 监听tcp客户端,发送命令
		self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.host = "127.0.0.1"
		self.udpPort = random.randint(8000, 9000)
		self.addr = (self.host, 9999)
		self.udpSocket.bind((self.host, self.udpPort))
		# select的读入参数
		self.listSocket = [self.tcpSocket, self.udpSocket]
	
	def connect(self):
		try:
			self.tcpSocket.connect(self.addr)
			# self.tcpSocket.setblocking(False)
			print('connect server success\n' + self.tcpSocket.recv(1024).decode('utf-8'))
			return True
		except Exception as e:
			print(e)
			return False
		
	def run(self):
		# 发送客户端用户名
		self.sendinfo()
		while self.listSocket:
			# print('waiting event')
			r_list, w_list, e_list = select.select(self.listSocket, [], [])
			for sock in r_list:
				if sock is self.tcpSocket:
					# print('tcpSocket_connect')
					command = sock.recv(1024).decode('utf-8')
					if command:
						self.parse(command)
					else:
						break
				else:
					try:
						print('udpSocket_connect')
						data, addr = sock.recvfrom(1024)
						print(data)
						self.append_msg(data.decode('utf-8'))
					except Exception as e:
						print(e)
		self.tcpSocket.close()
		self.udpSocket.close()
		
	def parse(self, command):
		key, value = command.split(':')
		if key == 'Owner':
			listusr = value.split(';')
			listusr.remove('')
			self.ref_listname(listusr)
		# 如果是Owner: ***。则更新在线列表
		# self.ref_listname(owner_list)
		# 如果是Username:*** Msg:****。则更新聊天窗口消息
		# self.ref_listmsg(data)
	
	# 发送客户端所属用户
	def sendinfo(self):
		self.tcpSocket.sendall(str.encode('Owner:' + self.frame.owner + ',' + self.host + '@' + str(self.udpPort)))

	# 用于GUI调用，发送消息
	def send_message(self, msg):
		self.udpSocket.sendto(str.encode(msg), self.addr)
		
	# 发送退出消息
	def send_exit(self):
		self.tcpSocket.sendall(str.encode('exit:' + self.frame.owner))
	
	def ref_listname(self, owner_list):
		self.frame.relistusr(owner_list)
	
	def append_msg(self, data):
		print('append_msg starting')
		self.frame.append_msg(data)


if __name__ == '__main__':
	client = TcpClient('jump')
	client.start()
# 	def __init__(self, frame):
# 		threading.Thread.__init__(self)
# 		self.tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 		self.frame = frame
# 		self.usrname = None
# 		self.owner = []
# 		self.msg = None
# 		self.connect()
#
# 	def connect(self):
# 		self.tcpsocket.connect(('127.0.0.1', 9999))
# 		print(self.tcpsocket.recv(1024).decode('utf-8'))
# 		# 获取客户端标识
# 		# self.send_msg(msg)
# 		# self.tcpsocket.send(msg)
# 		# self.get_note()
#
# 	# 发送消息
# 	def send_msg(self, msg):
# 		# if msg !=
# 		self.tcpsocket.sendall(msg)
# 		self.get_note()
# 		self.refreshlist()
#
# 	def refreshlist(self):
# 		self.frame.relistusr()
#
# 	# 捕获服务器返回消息
# 	def get_note(self):
# 		get_msg = self.tcpsocket.recv(1024).decode('utf-8')
# 		print('Now_Msg:'+get_msg)
# 		owner_m = re.match(r'^(Owner:)(.+)', get_msg)
# 		if owner_m:
# 			# self.owner = owner_m.group(2)
# 			self.owner.append(owner_m.group(2))
# 			# print('get_owner'+self.owner)
# 		msg_m = re.match(r'^(Usrname:)(.+)\s(Msg:)(.+)', get_msg)
# 		if msg_m:
# 			self.usrname = msg_m.group(2)
# 			self.msg = msg_m.group(4)
# 			print(self.usrname, self.msg)
# 		# self.tcpsocket.send(b'exit')
# 		# self.tcpsocket.close()
#
# 	def get_usrname(self):
# 		return self.usrname
#
# 	def get_owner(self):
# 		# for owner in self.owner:
# 		return self.owner
#
# 	def get_msg(self):
# 		return self.msg
#
# 	def clear_note(self):
# 		self.usrname = None
# 		self.msg = None
#
#
# if __name__ == '__main__':
# 	s = TcpClient(b'Owner:jump')
# 	s.send_msg(str.encode('Usrname:' + 'jump'+' Msg:' + '123'))
# 	s.send_msg(str.encode('hello world'))
# 	print(s.get_msg())
# 	# self.client.send_msg(str.encode('Usrname:'+ self.owner+' Msg:'+self.msg))
