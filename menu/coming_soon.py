from tkinter import Tk, Button, Label
from tkinter.ttk import Frame

from menu.mindstorm_frame import MindstormFrame

class ComingSoonFrame(MindstormFrame):
    def __init__(self, master, display, frame):
        MindstormFrame.__init__(self, master, display, frame)
        from menu.main_menu import MainMenuFrame
        Label(self, text='Coming soon!').grid(column=0, row=0)
        Button(self, text='Back', command=lambda:
               master.switch_frame(MainMenuFrame)).grid(column=0, row=1)
        self.pack()