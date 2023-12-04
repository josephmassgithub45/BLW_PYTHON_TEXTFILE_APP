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


        textarea=Text(mainwindow,width=100,height=20,font='times 15 bold')
        textarea.place(x=30,y=20)
        
        
        open_button=Button(mainwindow,text="Open Text File",command=open_text)
        open_button.place(x=30,y=500)
        
        save_button=Button(mainwindow,text="Save File",command=save_text)
        save_button.place(x=150,y=500)
        


        mainwindow.mainloop()



APPLICATION=TEXT_APP("BLUE LIGHT WAVES                 BLW_TEXT_APP","red")
APPLICATION.home()