import pygame

class MapNode():
    '''
    Node representing the compressed map. Each node may have a color associated with
    it, meaning it is a uniform square, or multiple child nodes.
    '''

    def __init__(self, lines, x, y, size):
        '''
        Create a map node from lines in a map file.

        :param lines: lines from the map file
        :param x: the x coordinate
        :param y: the y coordinate
        :param size: size of the box the node represents
        '''
        self.x = x
        self.y = y
        self.size = size

        self.children = []
        if lines[0] != '-1\n':
            color = lines.pop(0)
            color_stripped = color.strip('()\n ')
            color_fields = color_stripped.split(',')
            r = int(color_fields[0])
            g = int(color_fields[1])
            b = int(color_fields[2])
            self.value = (r, g, b)
            self.children = None
        else:
            lines.pop(0)
            self.value = -1
            if size != 25:
                self.children.append(MapNode(lines, x, y, size // 2))
                self.children.append(MapNode(lines, x + size // 2, y, size // 2))
                self.children.append(MapNode(lines, x, y + size // 2, size // 2))
                self.children.append(MapNode(lines, x + size // 2, y + size // 2, size // 2))
            else:
                self.children.append(MapNode(lines, x, y, 16))
                self.children.append(MapNode(lines, x + 16, y, 8))
                self.children.append(MapNode(lines, x + 16, y + 8, 8))
                self.children.append(MapNode(lines, x + 16, y + 16, 8))
                self.children.append(MapNode(lines, x + 8, y + 16, 8))
                self.children.append(MapNode(lines, x, y + 16, 8))
                for i in range(0, 25):
                    self.children.append(MapNode(lines, x + 24, y + i, 1))
                for j in range(0, 24):
                    self.children.append(MapNode(lines, x + j, y + 24, 1))

    def draw(self, display):
        '''
        Draw the part of the map this node represents.

        :param display: the display on which to draw
        :return: None
        '''
        if self.value != -1:
            pygame.draw.rect(display, self.value, (self.x, self.y, self.size, self.size))
        else:
            for child in self.children:
                child.draw(display)

    def write(self, grid):
        '''
        Convert the compressed map to a regular grid.

        :param grid: the grid to write to
        :return: None
        '''
        if self.value != -1:
            for i in range(self.x, self.x + self.size):
                for j in range(self.y, self.y + self.size):
                    grid[i][j] = self.value
        else:
            for child in self.children:
                child.write(grid)
