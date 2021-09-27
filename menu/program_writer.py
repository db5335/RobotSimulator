from os.path import exists
from tkinter import Label, INSERT, Text, Button, END

from menu.mindstorm_frame import MindstormFrame

file_name_prefix = 'files/programs/'
file_name_suffix = '.txt'

class ProgramWriterFrame(MindstormFrame):
    '''
    Program Writer Frame allows the user to create a custom program.
    '''

    def check_file_name(self):
        '''
        Check if the file name already exists.

        :return: whether or not the file name has been taken
        '''
        file_name = self.name_textbox.get(1.0, END)
        file_name = file_name[:-1]
        for c in file_name:
            i = ord(c)
            if i in range(65, 91) or i in range(97, 123) or i in range(48, 58):
                continue
            elif i == 32 or i == 45 or i == 95:
                continue
            else:
                return False
        return True

    def save(self):
        '''
        Save the program in a file.

        :return: None
        '''
        global file_name_prefix, file_name_suffix
        if self.check_file_name():
            self.message_label.config(text='')
            file_name = self.name_textbox.get(1.0, END)
            file_name = file_name_prefix + file_name[:-1] + file_name_suffix
            if exists(file_name):
                self.message_label.config(text='Program name already taken!')
            else:
                self.saved = True
                with open(file_name, 'w') as file:
                    file.write(self.program_textbox.get(1.0, END))
                from menu.main_menu import MainMenuFrame
                self.frame.destroy()
                self.master.switch_frame(MainMenuFrame)

    def __init__(self, master, display, frame):
        '''
        Initialize the frame.

        :param master: the app that controls the frames
        :param display: the Tkinter display
        :param frame: the Tkinter frame
        '''
        MindstormFrame.__init__(self, master, display, frame)
        Label(self, text='Program Name:').grid(column=0, row=0)
        self.name_textbox = Text(self, width=25, height=1)
        self.name_textbox.grid(column=1, row=0)
        self.name_textbox.insert(INSERT, 'Program')

        Label(self, text='Sample Program:').grid(column=0, row=1)
        Label(self, text='Write Program:').grid(column=1, row=1)

        Label(self, text='move [f/b] at [speed] for [duration]\n'
                         'turn [cw/ccw] at [speed] for [duration]\n'
                         'move [f/b] at [speed] until [sensor] [port] [condition]').grid(column=0, row=2)

        self.program_textbox = Text(self, width=50, height=30)
        self.program_textbox.grid(column=1, row=2)

        Button(self, text='Save Program', command=self.save).grid(column=0, row=9)

        self.message_label = Label(self, text='', fg='#ff0000')
        self.message_label.grid(column=1, row=9)
        self.pack()