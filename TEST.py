from tkinter import *

mainwindow=Tk()
mainwindow.geometry('1065x650')
mainwindow.configure(background="blue")

textarea=Text(mainwindow,width=96,height=20,font='times 15 bold',background='grey',border=20)
textarea.place(x=30,y=50)
mainwindow.mainloop()