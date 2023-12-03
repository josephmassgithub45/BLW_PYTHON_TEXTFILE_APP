from tkinter import *
from tkinter import filedialog

class TEXT_APP:
    def __init__(self,at,ac):
        self.apptitle=at
        self.appcolor=ac

    def home(self):
        mainwindow=Tk()
        mainwindow.title(self.apptitle)
        mainwindow.configure(background=self.appcolor)
        mainwindow.iconbitmap()
        mainwindow.geometry('770x650')
        mainwindow.resizable(False,False)

        def open_text():
            file=filedialog.askopenfilename(initialdir="c:",title="BLW_OPEN TEXT FILE")
            textfile=open(file,'r')
            notes=textfile.read()
            textarea.insert(END,notes)
            textfile.close()

        def save_text():
            man="man"

        textarea=Text(mainwindow,width=70,height=15,font='times 15 bold')
        textarea.pack(pady=30)
        
        open_button=Button(mainwindow,text="Open Text File",command=open_text)
        open_button.pack(pady=10)

        save_button=Button(mainwindow,text="Save File",command=save_text)
        save_button.pack(padx=20)
        


        mainwindow.mainloop()



APPLICATION=TEXT_APP("BLW_TEXT_APP","red")
APPLICATION.home()