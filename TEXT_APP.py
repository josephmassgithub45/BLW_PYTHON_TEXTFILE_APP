from tkinter import *

class TEXT_APP:
    def __init__(self,at,ac):
        self.apptitle=at
        self.appcolor=ac

    def home(self):
        mainwindow=Tk()
        mainwindow.title(self.apptitle)
        mainwindow.configure(background=self.appcolor)





        mainwindow.mainloop()



APPLICATION=TEXT_APP("BLW_TEXT_APP","red")
APPLICATION.home()