from tkinter import Tk
from tkinter.ttk import Frame

from menu.main_menu import MainMenuFrame

class MindstormApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.display = Frame(self)
        self.switch_frame(MainMenuFrame)

    def switch_frame(self, frame_class):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame_class(self, self.display, self._frame)
