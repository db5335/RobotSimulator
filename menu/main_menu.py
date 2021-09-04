from tkinter import Button
from tkinter.ttk import Frame

from menu.coming_soon import ComingSoonFrame
from menu.map_creator import MapCreatorFrame
from menu.mindstorm_frame import MindstormFrame
from menu.program_writer import ProgramWriterFrame
from menu.robot_creator import RobotCreatorFrame
from menu.selection import SelectionFrame


class MainMenuFrame(MindstormFrame):
    def switch_to_robot_creator(self):
        self.frame.destroy()
        self.master.switch_frame(RobotCreatorFrame)

    def switch_to_map_creator(self):
        self.frame.destroy()
        self.master.switch_frame(MapCreatorFrame)

    def switch_to_program_writer(self):
        self.frame.destroy()
        self.master.switch_frame(ProgramWriterFrame)

    def run(self):
        self.frame.destroy()
        self.master.switch_frame(SelectionFrame)

    def __init__(self, master, display, frame):
        MindstormFrame.__init__(self, master, display, frame)
        Button(self, text='Make your own robot!', command=self.switch_to_robot_creator).grid(column=0, row=0)
        Button(self, text='Create your own map!', command=self.switch_to_map_creator).grid(column=0, row=1)
        Button(self, text='Write your own program!', command=self.switch_to_program_writer).grid(column=0, row=2)
        Button(self, text='Run!', command=self.run).grid(column=0, row=3)
        Button(self, text='Help', command=lambda:
               master.switch_frame(ComingSoonFrame)).grid(column=0, row=4)
        self.pack()
