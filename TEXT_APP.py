from string import hexdigits
from tkinter import *
from tkinter import filedialog


class TEXT_APP:
    def __init__(self,at,ac,ic):
        self.apptitle=at
        self.appcolor=ac
        self.icon=ic

    def home(self):
        mainwindow=Tk()
        mainwindow.title(self.apptitle)
        mainwindow.configure(background=self.appcolor)
        mainwindow.iconbitmap(self.icon)
        mainwindow.geometry('1300x650')
        mainwindow.resizable(False,True)

        def open_text():
            text_file=filedialog.askopenfilename(initialdir="c:",title="BLW_OPEN TEXT FILE")
            textfile=open(text_file,'r')
            notes=textfile.read()
            textarea.insert(END,notes)
            textfile.close()

        def save_text():
            text_file=filedialog.askopenfilename(initialdir="c:",title="BLW_OPEN TEXT FILE")
            text_file=open(text_file,"w")
            text_file.write(textarea.get(1.0,END))
            text_file.close()
            message=Label(dialog,text="File Saved Successfully...",font='times 20 bold',background="grey")
            message.place(x=50,y=1)
        
        

        heading=Label(mainwindow,text="BLUE LIGHT WAVES ",font='times 25 bold',foreground="white",background="blue")
        heading.place(x=490,y=5)

        textarea=Text(mainwindow,width=123,height=20,font='times 15 bold',border=20)
        textarea.place(x=14,y=50)
  

        dialog=Frame(mainwindow,width=400,height=50,border=10)
        dialog.place(x=886,y=570)
        
        open_button=Button(mainwindow,text="Open Text File",font='times 15 bold',background="lightblue",command=open_text)
        open_button.place(x=290,y=560)
        
        save_button=Button(mainwindow,text="Save File",font='times 15 bold',background="lightblue",command=save_text)
        save_button.place(x=460,y=560)

        developer=Label(mainwindow,text='Developer : "Mr Joseph Massaquoi".',font='times 20 bold',background="blue",foreground="white")
        developer.place(x=10,y=610)

        mainwindow.mainloop()



APPLICATION=TEXT_APP("BLUE LIGHT WAVES   TEXT_APP","blue","BLW_LOGO.ico")
APPLICATION.home()

