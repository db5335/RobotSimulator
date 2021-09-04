from os.path import exists
from tkinter import Button, Label, Text, INSERT, END

import pygame

from map.map_grid import MapGrid
from menu.mindstorm_frame import MindstormFrame

file_name_prefix = 'files/maps/'
file_name_suffix = '.txt'

class MapCreatorFrame(MindstormFrame):
    def update_color(self):
        self.color = (self.red, self.green, self.blue)

    def update_brush_size(self):
        try:
            num = int(self.size_textbox.get(1.0, END))
            if num > 0 and num < 101:
                self.brush_size = num
        except:
            return

    def increase_brush_size(self):
        try:
            num = int(self.size_textbox.get(1.0, END))
            if num + 1 > 0 and num + 1 < 101:
                self.brush_size = num + 1
                self.size_textbox.delete(1.0, END)
                self.size_textbox.insert(INSERT, str(self.brush_size))
            elif num + 1 <= 0:
                self.brush_size = 1
                self.size_textbox.delete(1.0, END)
                self.size_textbox.insert(INSERT, str(self.brush_size))
            else:
                self.brush_size = 100
                self.size_textbox.delete(1.0, END)
                self.size_textbox.insert(INSERT, str(self.brush_size))
        except:
            self.brush_size = 100
            self.size_textbox.delete(1.0, END)
            self.size_textbox.insert(INSERT, str(self.brush_size))

    def decrease_brush_size(self):
        try:
            num = int(self.size_textbox.get(1.0, END))
            if num - 1 > 0 and num - 1 < 101:
                self.brush_size = num - 1
                self.size_textbox.delete(1.0, END)
                self.size_textbox.insert(INSERT, str(self.brush_size))
            elif num - 1 <= 0:
                self.brush_size = 1
                self.size_textbox.delete(1.0, END)
                self.size_textbox.insert(INSERT, str(self.brush_size))
            else:
                self.brush_size = 100
                self.size_textbox.delete(1.0, END)
                self.size_textbox.insert(INSERT, str(self.brush_size))
        except:
            self.brush_size = 1
            self.size_textbox.delete(1.0, END)
            self.size_textbox.insert(INSERT, str(self.brush_size))

    def increase_red(self):
        try:
            num = int(self.red_textbox.get(1.0, END))
            if num + 1 >= 0 and num + 1 <= 255:
                self.red = num + 1
                self.red_textbox.delete(1.0, END)
                self.red_textbox.insert(INSERT, str(self.red))
            elif num + 1 < 0:
                self.red = 0
                self.red_textbox.delete(1.0, END)
                self.red_textbox.insert(INSERT, str(self.red))
            else:
                self.red = 255
                self.red_textbox.delete(1.0, END)
                self.red_textbox.insert(INSERT, str(self.red))
        except:
            self.red = 255
            self.red_textbox.delete(1.0, END)
            self.red_textbox.insert(INSERT, str(self.red))
        self.update_color()

    def decrease_red(self):
        try:
            num = int(self.red_textbox.get(1.0, END))
            if num - 1 >= 0 and num - 1 <= 255:
                self.red = num - 1
                self.red_textbox.delete(1.0, END)
                self.red_textbox.insert(INSERT, str(self.red))
            elif num - 1 < 0:
                self.red = 0
                self.red_textbox.delete(1.0, END)
                self.red_textbox.insert(INSERT, str(self.red))
            else:
                self.red = 255
                self.red_textbox.delete(1.0, END)
                self.red_textbox.insert(INSERT, str(self.red))
        except:
            self.red = 0
            self.red_textbox.delete(1.0, END)
            self.red_textbox.insert(INSERT, str(self.red))
        self.update_color()

    def increase_green(self):
        try:
            num = int(self.green_textbox.get(1.0, END))
            if num + 1 >= 0 and num + 1 <= 255:
                self.green = num + 1
                self.green_textbox.delete(1.0, END)
                self.green_textbox.insert(INSERT, str(self.green))
            elif num + 1 < 0:
                self.green = 0
                self.green_textbox.delete(1.0, END)
                self.green_textbox.insert(INSERT, str(self.green))
            else:
                self.green = 255
                self.green_textbox.delete(1.0, END)
                self.green_textbox.insert(INSERT, str(self.green))
        except:
            self.green = 255
            self.green_textbox.delete(1.0, END)
            self.green_textbox.insert(INSERT, str(self.green))
        self.update_color()

    def decrease_green(self):
        try:
            num = int(self.green_textbox.get(1.0, END))
            if num - 1 >= 0 and num - 1 <= 255:
                self.green = num - 1
                self.green_textbox.delete(1.0, END)
                self.green_textbox.insert(INSERT, str(self.green))
            elif num + 1 < 0:
                self.green = 0
                self.green_textbox.delete(1.0, END)
                self.green_textbox.insert(INSERT, str(self.green))
            else:
                self.green = 255
                self.green_textbox.delete(1.0, END)
                self.green_textbox.insert(INSERT, str(self.green))
        except:
            self.green = 0
            self.green_textbox.delete(1.0, END)
            self.green_textbox.insert(INSERT, str(self.green))
        self.update_color()

    def increase_blue(self):
        try:
            num = int(self.blue_textbox.get(1.0, END))
            if num + 1 >= 0 and num + 1 <= 255:
                self.blue = num + 1
                self.blue_textbox.delete(1.0, END)
                self.blue_textbox.insert(INSERT, str(self.blue))
            elif num + 1 < 0:
                self.blue = 0
                self.blue_textbox.delete(1.0, END)
                self.blue_textbox.insert(INSERT, str(self.blue))
            else:
                self.blue = 255
                self.blue_textbox.delete(1.0, END)
                self.blue_textbox.insert(INSERT, str(self.blue))
        except:
            self.blue = 255
            self.blue_textbox.delete(1.0, END)
            self.blue_textbox.insert(INSERT, str(self.blue))
        self.update_color()

    def decrease_blue(self):
        try:
            num = int(self.blue_textbox.get(1.0, END))
            if num - 1 >= 0 and num - 1 <= 255:
                self.blue = num - 1
                self.blue_textbox.delete(1.0, END)
                self.blue_textbox.insert(INSERT, str(self.blue))
            elif num + 1 < 0:
                self.blue = 0
                self.blue_textbox.delete(1.0, END)
                self.blue_textbox.insert(INSERT, str(self.blue))
            else:
                self.blue = 255
                self.blue_textbox.delete(1.0, END)
                self.blue_textbox.insert(INSERT, str(self.blue))
        except:
            self.blue = 0
            self.blue_textbox.delete(1.0, END)
            self.blue_textbox.insert(INSERT, str(self.blue))
        self.update_color()

    def color_to_hex(self):
        hex_str = '#'
        red = hex(self.red)[2:]
        if len(red) == 1:
            hex_str = hex_str + '0'
        hex_str = hex_str + red
        green = hex(self.green)[2:]
        if len(green) == 1:
            hex_str = hex_str + '0'
        hex_str = hex_str + green
        blue = hex(self.blue)[2:]
        if len(blue) == 1:
            hex_str = hex_str + '0'
        return hex_str + blue

    def update_color_label(self):
        try:
            self.red = int(self.red_textbox.get(1.0, END))
            self.green = int(self.green_textbox.get(1.0, END))
            self.blue = int(self.blue_textbox.get(1.0, END))

            self.color_label.config(bg=self.color_to_hex())
            self.message_label.config(text='')
        except:
            self.message_label.config(text='Invalid color!')

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
                self.message_label.config(text='Map name already taken!')
            else:
                self.saved = True
                self.map.open_file(file_name)
                self.map.compress(0, 0, self.map.size)
                self.map.close_file()
                from menu.main_menu import MainMenuFrame
                self.frame.destroy()
                self.master.switch_frame(MainMenuFrame)
        else:
            self.message_label.config(text='Invalid map name!')

    def __init__(self, master, display, frame):
        MindstormFrame.__init__(self, master, display, frame)
        self.brush_size = 2
        self.red = 255
        self.green = 255
        self.blue = 255
        self.color = (self.red, self.green, self.blue)
        self.saved = False

        Label(self, text='Map Name:').grid(column=0, row=0)
        self.name_textbox = Text(self, width=25, height=1)
        self.name_textbox.grid(column=1, row=0)
        self.name_textbox.insert(INSERT, 'Map')

        Label(self, text='Brush Size:').grid(column=0, row=1)
        Button(self, text='  -  ', command=self.decrease_brush_size).grid(column=0, row=2)
        self.size_textbox = Text(self, width=3, height=1)
        self.size_textbox.grid(column=1, row=2)
        self.size_textbox.insert(INSERT, str(self.brush_size))
        Button(self, text='  +  ', command=self.increase_brush_size).grid(column=2, row=2)

        Label(self, text='Paint Color:').grid(column=0, row=3)
        Button(self, text='  +  ', command=self.increase_red, bg='#ff0000').grid(column=0, row=4)
        Button(self, text='  +  ', command=self.increase_green, bg='#00ff00').grid(column=1, row=4)
        Button(self, text='  +  ', command=self.increase_blue, bg='#0000ff').grid(column=2, row=4)
        Button(self, text='  -  ', command=self.decrease_red, bg='#ff0000').grid(column=0, row=6)
        Button(self, text='  -  ', command=self.decrease_green, bg='#00ff00').grid(column=1, row=6)
        Button(self, text='  -  ', command=self.decrease_blue, bg='#0000ff').grid(column=2, row=6)
        self.red_textbox = Text(self, width=3, height=1)
        self.red_textbox.grid(column=0, row=5)
        self.red_textbox.insert(INSERT, '255')
        self.green_textbox = Text(self, width=3, height=1)
        self.green_textbox.grid(column=1, row=5)
        self.green_textbox.insert(INSERT, '255')
        self.blue_textbox = Text(self, width=3, height=1)
        self.blue_textbox.grid(column=2, row=5)
        self.blue_textbox.insert(INSERT, '255')

        self.color_label = Label(self, width=25, bg=self.color_to_hex())
        self.color_label.grid(column=1, row=7)
        Button(self, text='Update Color', command=lambda: self.update_color_label()).grid(column=0, row=7)

        Button(self, text='Save Map', command=self.save).grid(column=0, row=9)

        self.message_label = Label(self, text='', fg='#ff0000')
        self.message_label.grid(column=1, row=9)

        self.map = MapGrid()
        self.pack()
        self.done = False
        self.run()
        self.done = True

    def run(self):
        pygame.init()
        py_display = pygame.display.set_mode((800, 800))
        py_display.fill((0, 0, 0))
        py_clock = pygame.time.Clock()
        count = 1
        mouse = pygame.mouse
        while not self.saved:
            self.update_color()
            self.update_color_label()
            self.update_brush_size()
            size = 2 * (self.brush_size + 1) // 2
            self.display.update()
            py_clock.tick(100)
            if mouse.get_pressed()[0]:
                pygame.draw.rect(py_display, self.color,
                                 pygame.Rect(mouse.get_pos()[0] - size / 2, mouse.get_pos()[1] - size / 2, size, size))
                for i in range(-1 * size // 2, size // 2 + 1):
                    for j in range(-1 * size // 2, size // 2 + 1):
                        if mouse.get_pos()[0] + i >= 0 and mouse.get_pos()[0] + i <= 799 and mouse.get_pos()[
                            1] + j >= 0 and mouse.get_pos()[1] + j <= 799:
                            count += 1
                            self.map.grid[mouse.get_pos()[0] + i][mouse.get_pos()[1] + j] = self.color
            pygame.display.update()
        pygame.display.quit()
