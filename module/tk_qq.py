from tkinter import *
import time, threading
from module import TCP_client
from tkinter.scrolledtext import ScrolledText

class SendMsg(Frame):
    def __init__(self, title,master=None):
        Frame.__init__(self, master)
        self.master.title('畅聊吧...ヽ(ﾟ∀ﾟ)ﾒ(ﾟ∀ﾟ)ﾉ ')
        self.owner = title
        self.client = None
        self.pack()
        self.sendmsgpool()
        self.framemsg()
        self.thread_conn = threading.Thread(target=SendMsg.connect, args=(self,))
        self.thread_conn.setDaemon(True)
        self.thread_conn.start()
        
    def connect(self):
        # 连接服务器
        self.client = TCP_client.TcpClient(self)
        if self.client.connect():
            self.client.start()
            print('connect success')
            return True
        else:
            return False
        # self.client.send_msg(str.encode('Owner:'+ self.owner))
        # self.text_listusr.insert(END,str(self.client.get_owner()))
        # self.titlelist["text"] = '当前在线成员('+str(self.text_listusr.size())+')'
    
    #刷新聊天窗口内容
    def append_msg(self, data):
        msg_m = re.match(r'^(Usrname:)(.+)\s(Msg:)(.+)', data)
        usrname = None
        msg = None
        if msg_m:
            usrname = msg_m.group(2)
            msg = msg_m.group(4)
            print(usrname, msg)
        if usrname == self.owner:
            msgcontent = '我:' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
        else:
            msgcontent = '' if usrname is None else usrname + ':' + time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
        self.text_listmsg["state"] = 'normal'
        self.text_listmsg.insert(END, msgcontent, 'green')
        self.text_listmsg.insert(END, msg + '\n')
        # self.text_msg.delete('1.0', END)
        self.text_listmsg["state"] = 'disable'
        # self.client.clear_note()
        # msgcontent = None
    
    # 刷新在线列表
    def relistusr(self, listname):
        # print('%s relistusr is staring '% listname)
        self.text_listusr.delete(0,END)
        for owner in listname:
            print(owner)
            self.text_listusr.insert(END, str (owner))
        self.titlelist["text"] = '当前在线成员('+str(self.text_listusr.size())+')'
        time.sleep(1)

    # 设计框架
    def sendmsgpool(self):
        # 创建几个frame作为容器
        self.frame_left_top = Frame(width=380, height=270, bg='white')
        self.frame_left_center = Frame(width=380, height=100, bg='white')
        self.frame_left_bottom = Frame(width=380, height=30)
        self.frame_right = Frame(width=170, height=100, bg='white')
        self.frame_right.pack(side=RIGHT, expand=YES, fill=Y, padx=4, pady=5)
        self.frame_left_top.pack(expand=YES, fill=NONE, padx=2, pady=5)
        self.frame_left_center.pack(expand=YES, fill=NONE, padx=2, pady=5)
        self.frame_left_bottom.pack(expand=YES, fill=NONE)
        self.frame_right.propagate(0)
        self.frame_left_top.propagate(0)
        self.frame_left_center.propagate(0)
        self.frame_left_bottom.propagate(0)

    # 发送事件
    def selfsendmsg(self,event="<Return>"):
        self.msg = 'Usrname:' + self.owner + ' Msg:' + self.text_msg.get('1.0', END)
        print('SendMessage: %s' % self.msg)
        self.client.send_message(self.msg)
        self.text_msg.delete('0.0', END)

    # 装饰Frame
    def framemsg(self):
        self.text_listmsg = ScrolledText(self.frame_left_top, width=20, height=20, background='#ffffff',state='disabled')
        self.text_listmsg.tag_config('green',foreground='#008B00')
        self.text_msg = Text(self.frame_left_center)
        self.text_listusr = Listbox(self.frame_right,width=25)
        self.titlelist = Label(self.frame_right,text='当前在线成员('+str(self.text_listusr.size())+')')
        global piclogo
        piclogo = PhotoImage (file=r'F:\python_book\headpic\picture.png')
        self.picture = Label(self.frame_right,image=piclogo,compound = CENTER)
        self.button_send = Button(self.frame_left_bottom,text='发送',command=self.selfsendmsg)
        self.text_msg.bind ("<Return>", self.selfsendmsg)
        self.picture.pack()
        self.titlelist.pack(expand=1, fill=X)
        self.text_listmsg.pack(expand=1, fill="both")
        self.text_msg.pack()
        self.text_listusr.pack(expand=0, fill=Y)
        self.button_send.pack(side=RIGHT)
        
        
if __name__ == '__main__':
    app = SendMsg('admin')
    # app.process()
    # 设置窗口标题:
    # app.master.title('与***聊天中')
    # 主消息循环:
    app.mainloop()