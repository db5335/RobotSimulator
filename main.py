'''
Main program for robot simulator.

:author: Dominick Banasik
'''

from tkinter.ttk import Frame
from menu.mindstorm_app import MindstormApp

def main():
    '''
    Main function starts the application.

    :return: None
    '''
    tk_root = MindstormApp()
    tk_display = Frame(tk_root)
    while (True):
        tk_display.update()

if __name__ == '__main__':
    main()