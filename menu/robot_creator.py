from os.path import exists
from tkinter import Label, Text, Button, INSERT, IntVar, StringVar, END
from tkinter.ttk import OptionMenu

import pygame

from menu.mindstorm_frame import MindstormFrame
from robot.base import Base
from robot.color_sensor import ColorSensor
from robot.touch_sensor import TouchSensor


file_name_prefix = 'files/robots/'
file_name_suffix = '.txt'

class RobotCreatorFrame(MindstormFrame):
    def add_component(self):
        sensor_str = self.sensor.get()
        sensor = None
        if sensor_str == 'Touch Sensor':
            sensor = TouchSensor(self.robot)
        elif sensor_str == 'Color Sensor':
            sensor = ColorSensor(self.robot)
        elif sensor_str == 'Ultrasound Sensor':
            pass

        self.robot.add_component(sensor, self.port.get())

    def check_file_name(self):
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
        global file_name_prefix, file_name_suffix
        if self.check_file_name():
            self.message_label.config(text='')
            file_name = self.name_textbox.get(1.0, END)
            file_name = file_name_prefix + file_name[:-1] + file_name_suffix
            if exists(file_name):
                self.message_label.config(text='Robot name already taken!')
            else:
                self.saved = True
                self.robot.save(file_name)
                from menu.main_menu import MainMenuFrame
                self.frame.destroy()
                self.master.switch_frame(MainMenuFrame)
        else:
            self.message_label.config(text='Invalid robot name!')

    def __init__(self, master, display, frame):
        MindstormFrame.__init__(self, master, display, frame)
        self.saved = False

        Label(self, text='Robot Name:').grid(column=0, row=0)
        self.name_textbox = Text(self, width=25, height=1)
        self.name_textbox.grid(column=1, row=0)
        self.name_textbox.insert(INSERT, 'Robot')

        Label(self, text='Add Component:').grid(column=0, row=1)
        Label(self, text='Port:').grid(column=0, row=2)
        ports = []
        for i in range(0, 17):
            ports.append(i)
        self.port = IntVar(self)
        self.port.set(1)
        self.port_dropdown = OptionMenu(self, self.port, *ports)
        self.port_dropdown.grid(column=1, row=2)
        Label(self, text='Sensor:').grid(column=0, row=3)
        sensors = ['', 'None', 'Touch Sensor', 'Color Sensor', 'Ultrasound Sensor']
        self.sensor = StringVar(self)
        self.sensor.set(sensors[1])
        self.sensor_dropdown = OptionMenu(self, self.sensor, *sensors)
        self.sensor_dropdown.grid(column=1, row=3)
        Button(self, text='Add', command=self.add_component).grid(column=1, row=4)

        Button(self, text='Save', command=self.save).grid(column=0, row=5)
        self.message_label = Label(self, text='', fg='#ff0000')
        self.message_label.grid(column=1, row=5)

        self.robot = Base(325, 325)

        self.pack()
        self.run()

    def run(self):
        pygame.init()
        py_display = pygame.display.set_mode((800, 800))
        py_display.fill((0, 0, 0))
        py_clock = pygame.time.Clock()
        while not self.saved:
            self.display.update()
            py_clock.tick(100)
            py_display.fill((0, 0, 0))
            py_display.blit(self.robot.surf, (self.robot.x, self.robot.y))
            pygame.display.update()
        pygame.display.quit()
        print('done')

