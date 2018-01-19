from tkinter import *
from PIL import Image
from re_test import CODE_YANZHENG
from module import TCP_client,tk_qq
import tkinter.scrolledtext
import tkinter.messagebox as messagebox
import time

# 用户账户
user={'jump':'123456','admin':'000000'}
# 用户头像
pic={'jump':'\pic1.gif','admin':'\pic2.gif','':'\moren.gif'}
# 登入统计
count={'jump':0,'admin':0,'bz':0}

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.codeclass = CODE_YANZHENG.CheckCode ()
		self.createwidgets()
	
	def changePic(self,event):
		if self.usrnameInput.get() in pic:
			global headpic
			# 更换头像
			headpic = PhotoImage (file=headpic_url + pic[self.usrnameInput.get()])
			self.picshow["image"] = headpic
		else:
			headpic = PhotoImage (file=headpic_url + '\moren.gif')
			self.picshow["image"] = headpic
			
	def checkcode(self,event):
		if str.upper(self.codecheck.get()) != self.code_list:
			messagebox.showinfo ('Message','checkcode is wrong!' )
			count['bz'] = 1
		else:
			count['bz'] = 0
		
	def createwidgets(self):
		global logo
		# 背景图片
		logo = PhotoImage (file=r'F:\HYVideoDesktop\Video\愤怒的舔屏.png')
		self.logoshow = Label(self,image=logo,compound = CENTER)
		self.logoshow.pack(ipadx=22)
		global headpic
		# 用户头像
		global headpic_url
		headpic_url = r'F:\python_book\headpic'
		headpic = PhotoImage (file=headpic_url+'\moren.gif')
		self.picshow = Label(self,image=headpic)
		self.picshow.pack (side=LEFT,ipadx=10)
		self.blank = Label (self,text='ヽ(ﾟ∀ﾟ)ﾒ(ﾟ∀ﾟ)ﾉ --Sign in')
		self.blank.pack (pady=5)
		# 输入用户名
		self.usrnameInput = Entry(self)
		self.usrnameInput.bind("<Key>", self.changePic)
		self.usrnameInput.pack(pady=3)
		# 输入密码
		self.passwordInput = Entry (self,show='*')
		self.passwordInput.pack(pady=3)
		# 登入检查
		self.alertButton = Button (self, text='Sign in', command=self.check)
		self.alertButton.pack (expand=FALSE,fill=X,padx=15)
		# 验证码 输入框
		self.codecheck = Entry(self,width=6)
		self.code_list = self.codeclass.get_code ()
		self.codecheck.bind ("<Return>", self.checkcode)
		# 验证码图片
		global codepic
		codepic = PhotoImage(file=r'code.gif')
		self.codeshow = Label(self,image=codepic)
		# self.codeshow.pack(side=RIGHT,padx=17)
		# self.codecheck.pack (side=RIGHT)
		# self.alertButton.pack (expand=FALSE,fill=BOTH)
	# 登入检查
	def check(self):
		name = self.usrnameInput.get()
		password = self.passwordInput.get()
		# 验证码标志位 0|通过;1|失败
		# count['bz']
		self.changePic("<Return>")
		if count['bz'] == 1:
			self.checkcode("<Return>")
		if user[name] == password and count['bz'] == 0:
			# 验证通过，调用其他事件
			# messagebox.showinfo ('Message', 'Hello, %s' % self.usrnameInput.get())
			# 聊天框
			self.destroy()
			self.sendmsg = tk_qq.SendMsg(name)
			# msg = str.encode(name)
			# self.client = TCP_client.TcpClient(msg)
		else:
			# 验证失败，报错信息
			count[name]=count[name]+1
			self.blank.config(text='usrname or password is wrong!',fg='red',compound='left')
			# 延时撤销报错信息
			self.blank.after(1000*2,self.reset)
			if count[name] >= 3:
				self.codeshow.pack (side=RIGHT, padx=17)
				self.codecheck.pack (side=RIGHT)
				count['bz'] = 1
			else:
				self.codeshow.pack_forget ()
				self.codecheck.pack_forget ()
	
	def reset(self):
		self.blank.config(text='ヽ(ﾟ∀ﾟ)ﾒ(ﾟ∀ﾟ)ﾉ --Sign in',fg='black')

app = Application()
app.master.title('ヽ(ﾟ∀ﾟ)ﾒ(ﾟ∀ﾟ)ﾉ ')
app.mainloop()