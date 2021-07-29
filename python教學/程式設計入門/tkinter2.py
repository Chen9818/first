from tkinter import*
win=Tk()

win.title('tkinter')
win.geometry('400x200')

img=PhotoImage(file=r'C:\Users\chen\Desktop\bomb_PNG5.png')

def bomb():
    print('bomb!!!!!!!!!')
#button
btn=Button(text="click me")
# btn.config(width=10,height=5)
btn.config(image=img)
btn.config(command=bomb)
btn.pack()





win.mainloop()