from tkinter import Tk
from tkinter.ttk import Frame

from menu.main_menu import MainMenuFrame

class MindstormApp(Tk):
    '''
    Application that controls the frames.
    '''

    def __init__(self):
        '''
        Initialize the frames and start on the main menu.
        '''
        Tk.__init__(self)
        self._frame = None
        self.display = Frame(self)
        self.switch_frame(MainMenuFrame)

    def switch_frame(self, frame_class):
        '''
        Switch from one frame to another.

        :param frame_class: class of the frame to switch to
        :return: None
        '''
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame_class(self, self.display, self._frame)
