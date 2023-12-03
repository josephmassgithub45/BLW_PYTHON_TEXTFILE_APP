from tkinter import *

class TEXT_APP:
    def __init__(self,at,ac):
        self.apptitle=at
        self.appcolor=ac

    def home(self):
        mainwindow=Tk()
        mainwindow.title(self.apptitle)
        mainwindow.configure(background=self.appcolor)
        mainwindow.geometry('800x550')
        mainwindow.resizable(False,False)

        def read():
            textfile=open("DATABASE.txt")
            notes=textfile.read()
            textarea.insert(END,notes)

       

        textarea=Text(mainwindow,width=50)
        textarea.grid(row=0,column=2)
        

        openbutton=Button(mainwindow,text="OPEN",action=read())
        openbutton.grid(row=1,column=2)


        mainwindow.mainloop()



APPLICATION=TEXT_APP("BLW_TEXT_APP","red")
APPLICATION.home()