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
        mainwindow.geometry('1065x650')
        mainwindow.resizable(False,False)

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


        heading=Label(mainwindow,text="BLUE LIGHT WAVES ",font='times 25 bold',foreground="white",background="blue")
        heading.place(x=350,y=5)

        textarea=Text(mainwindow,width=96,height=20,font='times 15 bold',background='grey',border=20)
        textarea.place(x=30,y=50)
        
        open_button=Button(mainwindow,text="Open Text File",font='times 15 bold',command=open_text)
        open_button.place(x=390,y=560)
        
        save_button=Button(mainwindow,text="Save File",font='times 15 bold',background="red",command=save_text)
        save_button.place(x=560,y=560)
        
        developer=Label(mainwindow,text="Developed By Mr Joseph Massaquoi.",font='times 20 bold',background="blue",foreground="white")
        developer.place(x=30,y=600)

        mainwindow.mainloop()



APPLICATION=TEXT_APP("BLUE LIGHT WAVES      BLW_TEXT_APP","blue","BLW_LOGO.ico")
APPLICATION.home()