from tkinter import Tk, Button, Label

from menu.mindstorm_frame import MindstormFrame

class ComingSoonFrame(MindstormFrame):
    '''
    Menu Frame to take the place of a frame that has not been created.
    '''

    def __init__(self, master, display, frame):
        '''
        Initialize the frame.

        :param master: the app that controls the frames
        :param display: the Tkinter display
        :param frame: the Tkinter frame
        '''
        MindstormFrame.__init__(self, master, display, frame)
        from menu.main_menu import MainMenuFrame
        Label(self, text='Coming soon!').grid(column=0, row=0)
        Button(self, text='Back', command=lambda:
               master.switch_frame(MainMenuFrame)).grid(column=0, row=1)
        self.pack()