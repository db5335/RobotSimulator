import os
from tkinter import StringVar, Label, Button
from tkinter.ttk import OptionMenu

import pygame
from pygame.surface import Surface

from code.block_sequence import BlockSequence
from map.map_grid import MapGrid
from map.map_node import MapNode
from menu.mindstorm_frame import MindstormFrame
from robot.base import Base

maps_path = 'files/maps'
robots_path = 'files/robots'
programs_path = 'files/programs'
suffix = '.txt'

class SelectionFrame(MindstormFrame):
    '''
    Selection Frame is where the user can pick a robot, map, and program to execute.
    '''

    def go(self):
        '''
        Start the execution of the chosen program with the robot and map.

        :return:
        '''
        pygame.init()
        py_display = pygame.display.set_mode((800, 800))

        lines = []
        with open(maps_path + '/' + self.map.get() + suffix) as file:
            for line in file:
                lines.append(line)
        root = MapNode(lines, 0, 0, 800)
        self.map_surf = Surface((800, 800))
        self.grid = MapGrid().grid
        root.draw(self.map_surf)
        root.write(self.grid)

        self.robot_base = Base(325, 325)
        self.robot_base.init_from_file(robots_path + '/' + self.robot.get() + suffix)
        self.robot_base.set_background(self.map_surf)
        self.robot_base.set_grid(self.grid)

        self.sequence = BlockSequence()
        self.sequence.create_from_file(py_display, self.robot_base, programs_path + '/' + self.program.get() + suffix)
        self.sequence.execute()


        while(True):
            py_display.blit(self.map_surf, (0, 0))
            py_display.blit(self.robot_base.surf, (self.robot_base.x, self.robot_base.y))
            pygame.display.update()

    def __init__(self, master, display, frame):
        '''
        Initialize the frame.

        :param master: the app that controls the frames
        :param display: the Tkinter display
        :param frame: the Tkinter frame
        '''
        MindstormFrame.__init__(self, master, display, frame)

        maps = ['']
        for map in os.listdir(maps_path):
            maps.append(map[:-4])
        self.map = StringVar(self)
        self.map.set(maps[1])
        Label(self, text='Select Map:').grid(column=0, row=0)
        OptionMenu(self, self.map, *maps).grid(column=1, row=0)

        robots = ['']
        for robot in os.listdir(robots_path):
            robots.append(robot[:-4])
        self.robot = StringVar(self)
        self.robot.set(robots[1])
        Label(self, text='Select Robot:').grid(column=0, row=1)
        OptionMenu(self, self.robot, *robots).grid(column=1, row=1)

        programs = ['']
        for program in os.listdir(programs_path):
            programs.append(program[:-4])
        self.program = StringVar(self)
        self.program.set(programs[1])
        Label(self, text='Select Program:').grid(column=0, row=2)
        OptionMenu(self, self.program, *programs).grid(column=1, row=2)

        Button(self, text='Go!', command=self.go).grid(column=0, row=3)

        self.pack()