from tkinter import *
import tkinter.messagebox as messagebox
import time

user={'jump':'123456','admin':'000000'}

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createwidgets()
	
	def createwidgets(self):
		global logo
		logo = PhotoImage (file=r'F:\HYVideoDesktop\Video\愤怒的舔屏.png')
		self.logoshow = Label(self,image=logo,compound = CENTER)
		self.logoshow.pack()
		self.usrnameInput = Entry(self,text='用户名')
		self.usrnameInput.pack()
		self.passwordInput = Entry (self,show='*')
		self.passwordInput.pack()
		self.alertButton = Button(self, text='Sign in', command=self.check)
		self.alertButton.pack()
		# self.Scale = Scale(self)
		# self.Scale.pack(side=RIGHT)
		
	def check(self):
		name = self.usrnameInput.get()
		password = self.passwordInput.get()
		if user[name] == password:
			messagebox.showinfo ('Message', 'Hello, %s' % self.usrnameInput.get())
		else:
			self.showerro = Label(self,bitmap='warning',text='usrname or password is wrong!',fg='red',compound='left')
			self.showerro.pack()
			self.showerro.after(1000*3,self.reset)
	
	def reset(self):
		self.showerro.pack_forget()

app = Application()
app.master.title('ヽ(ﾟ∀ﾟ)ﾒ(ﾟ∀ﾟ)ﾉ --Sign in')
app.mainloop()