class MapGrid():
    '''
    Class for the grid on which the robot will run.
    '''

    def __init__(self):
        '''
        Initialize an empty, black grid.
        '''
        self.grid = []
        self.size = 800
        for i in range(0, self.size):
            self.grid.append([])
            for j in range(0, self.size):
                self.grid[i].append((0, 0, 0))

    def open_file(self, file_name):
        '''
        Open the map file.

        :param file_name: name of the file
        :return: None
        '''
        self.file = open(file_name, 'w')

    def close_file(self):
        '''
        Close the map file.

        :return: None
        '''
        if self.file is None:
            return

        self.file.close()

    def compress(self, row, col, size):
        '''
        Compress the map and write it to the file.

        :param row: the current row
        :param col: the current column
        :param size: the size of the box to compress
        :return: None
        '''
        size = int(size)
        row = int(row)
        col = int(col)
        same = True
        color = self.grid[row][col]
        for i in range(0, size):
            for j in range(0, size):
                if self.grid[row + i][col + j] != color:
                    same = False
                    break
            if not same:
                self.file.write('-1\n')
                if size != 25:
                    self.compress(row, col, size / 2)
                    self.compress(row + size / 2, col, size / 2)
                    self.compress(row, col + size / 2, size / 2)
                    self.compress(row + size / 2, col + size / 2, size / 2)
                else:
                    self.compress(row, col, 16)
                    self.compress(row + 16, col, 8)
                    self.compress(row + 16, col + 8, 8)
                    self.compress(row + 16, col + 16, 8)
                    self.compress(row + 8, col + 16, 8)
                    self.compress(row, col + 16, 8)
                    for k in range(0, 25):
                        self.compress(row + 24, col + k, 1)
                    for l in range(0, 24):
                        self.compress(row + l, col + 24, 1)
                break
        if same:
            self.file.write(str(self.grid[row][col]) + '\n')