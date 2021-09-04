from tkinter.ttk import Frame

class MindstormFrame(Frame):
    def __init__(self, master, display, frame):
        Frame.__init__(self, master)
        self.display = display
        self.frame = frame
        if self.frame is not None:
            self.frame.destroy()
        self.frame = self
