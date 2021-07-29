import tkinter as tk
win=tk.Tk()
#標題
win.title('hi')
#大小
win.geometry('400x200')  #寬x高
win.resizable(0,0)  #固定大小  0=false  1=true


#顏色
win.config(background='yellow')

#透明度
win.attributes('-alpha',0.5)  #1~0  透明度

#置頂
win.attributes('-topmost',1)  #1開啟置頂  0關閉  

win.mainloop()