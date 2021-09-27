from tkinter.ttk import Frame

class MindstormFrame(Frame):
    '''
    Abstract class for frames in the application.
    '''

    def __init__(self, master, display, frame):
        '''
        Initialize the frame.

        :param master: the app that controls the frames
        :param display: the Tkinter display
        :param frame: the Tkinter frame
        '''
        Frame.__init__(self, master)
        self.display = display
        self.frame = frame
        if self.frame is not None:
            self.frame.destroy()
        self.frame = self
