from tkinter import *
from tkinter.scrolledtext import ScrolledText
import time
root = Tk()


lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.delete(3)
print (lb.size())
lb.pack()
# frame_left_top   = Frame(width=380, height=270, bg='white')
# frame_left_center  = Frame(width=380, height=100, bg='white')
# frame_left_bottom  = Frame(width=380, height=20)
# frame_right     = Frame(width=170, height=400, bg='white')
# frame_left_top.grid(row=0, column=0, padx=2, pady=5)
# frame_left_center.grid(row=1, column=0, padx=2, pady=5)
# frame_left_bottom.grid(row=2, column=0)
# frame_right.grid(row=0, column=1, rowspan=3, padx=4, pady=5)
# frame_left_top.grid_propagate(0)
# frame_left_center.grid_propagate(0)
# frame_left_bottom.grid_propagate(0)
# logo = PhotoImage(file=r'F:\HYVideoDesktop\Video\愤怒的舔屏.png')
# logoshow = Label(root, image=logo)
# logoshow.pack()
# def code(event):
# 	if text.get() == '123':
# 		global logo2
# 		logo2 = PhotoImage(file=r'F:\Python_study\re_test\code.gif')
# 		logoshow.config(image=logo2)
# 		#logoshow.pack()
# text = Entry(root)
# text.bind("<Return>", code)
# text.pack()
root.mainloop()

# from tkinter import *
# from math import *
# def evaluate(event):
#     res.configure(text = "Ergebnis: " + str(eval(entry.get())))
# w = Tk()
# Label(w, text="Your Expression:").pack()
# entry = Entry(w)
# entry.bind("<Return>", evaluate)
# entry.pack()
# res = Label(w)
# res.pack()
# w.mainloop()