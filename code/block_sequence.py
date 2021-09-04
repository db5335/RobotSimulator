from code.and_condition import AndCondition
from code.color_condition import ColorCondition
from code.conditions import TouchConditions, ColorConditions
from code.loop import Loop
from code.move_block import *
from code.or_condition import OrCondition
from code.simple_move_block import SimpleMoveBlock
from code.simple_turn_block import SimpleTurnBlock
from code.touch_condition import TouchCondition
from code.turn_block import *

class BlockSequence:
    def __init__(self):
        self.actions = []
        self.loop = self

    def create_from_file(self, display, target, file_name):
        self.display = display
        self.target = target
        with open(file_name) as file:
            for line in file:
                fields = line.split(' ')
                if fields[0] == '}\n':
                    self.loop = self.loop.upper_loop
                elif fields[0] == 'move':
                    self.create_move_block(fields)
                elif fields[0] == 'turn':
                    self.create_turn_block(fields)
                elif fields[0] == 'until':
                    loop = Loop(self.display, self.target, self.loop)
                    self.loop.add_action(loop)
                    self.loop = loop
                    self.create_loop(fields, loop, 1)

    def create_move_block(self, fields):
        direction = MoveDirection.FORWARD
        if fields[1] == 'f' or fields[1] == 'forward':
            pass
        elif fields[1] == 'b' or fields[2] == 'backward':
            direction = MoveDirection.BACKWARD
        else:
            return False
        if fields[2] != 'at':
            return False
        try:
            speed = float(fields[3])
            if len(fields) == 4:
                self.loop.add_action(SimpleMoveBlock(self.display, self.target, direction, speed))
            if fields[4] != 'for':
                return False
            duration = float(fields[5])
            self.loop.add_action(MoveBlock(self.display, self.target, direction, speed, duration))
        except:
            return False
        return True

    def create_turn_block(self, fields):
        direction = TurnDirection.COUNTER_CLOCKWISE
        if fields[1] == 'ccw' or fields[1] == 'counterclockwise':
            pass
        elif fields[1] == 'cw' or fields[1] == 'clockwise':
            direction = TurnDirection.CLOCKWISE
        else:
            return False
        if fields[2] != 'at':
            return False
        try:
            speed = float(fields[3])
            if len(fields) == 4:
                self.loop.add_action(SimpleTurnBlock(self.display, self.target, direction, speed))
                return True
            if fields[4] != 'for':
                return False
            duration = float(fields[5])
            self.loop.add_action(TurnBlock(self.display, self.target, direction, speed, duration))
        except:
            return False
        return True

    def create_loop(self, fields, loop, index):
        condition_class = None
        while True:
            if fields[index] == 'touch':
                val = self.create_touch_loop(fields, loop, index + 1, condition_class)
            elif fields[index] == 'color':
                val = self.create_color_loop(fields, loop, index + 1, condition_class)
            if fields[val] == 'or':
                condition_class = OrCondition
                index = val + 1
            elif fields[val] == 'and':
                condition_class = AndCondition
                index = val + 1
            else:
                break

    def word_to_color(self, word):
        if word == 'red':
            return (255, 0, 0)
        if word == 'green':
            return (0, 255, 0)
        if word == 'blue':
            return (0, 0, 255)
        if word == 'black':
            return (0, 0, 0)
        if word == 'white':
            return (255, 255, 255)

    def list_to_color(self, list):
        nums = '1234567890'
        red_str = ''
        for c in list[0]:
            if c in nums:
                red_str = red_str + c
        green_str = ''
        for c in list[1]:
            if c in nums:
                green_str = green_str + c
        blue_str = ''
        for c in list[2]:
            if c in nums:
                blue_str = blue_str + c
        return (int(red_str), int(green_str), int(blue_str))

    def create_color_loop(self, fields, loop, index, condition_class):
        try:
            port = int(fields[index])
            if port not in range(1, 17):
                return False
            sensor = self.target.get_component_by_port(port)
            condition = None
            while True:
                index += 1
                if fields[index] == 'sees':
                    index += 1
                    if fields[index] == 'from':
                        index += 1
                        if fields[index] in ['red', 'green', 'blue', 'black', 'white']:
                            min = self.word_to_color(fields[index])
                            index += 1
                        else:
                            min = self.list_to_color(fields[index:index+3])
                            index += 3
                        if fields[index] != 'to':
                            return False
                        index += 1
                        if fields[index] in ['red', 'green', 'blue', 'black', 'white']:
                            max = self.word_to_color(fields[index])
                            index += 1
                        else:
                            max = self.list_to_color(fields[index:index + 3])
                            index += 3
                        new_condition = ColorCondition(ColorConditions.RANGE, sensor, None, min, max)
                    elif fields[index] in ['red', 'green', 'blue', 'black', 'white']:
                        new_condition = ColorCondition(ColorConditions.EXACT, sensor, self.word_to_color(fields[index]), None, None)
                        index += 1
                    else:
                        new_condition = ColorCondition(ColorConditions.EXACT, sensor, self.list_to_color(fields[index:index+3]), None, None)
                        index += 3
                else:
                    return False

                if condition is None:
                    condition = new_condition
                elif fields[index - 1] == 'or':
                    condition = OrCondition(condition, new_condition)
                elif fields[index - 1] == 'and':
                    condition = AndCondition(condition, new_condition)

                if fields[index] == 'or' or fields[index] == 'and':
                    if fields[index + 1] in ['touched', 'released', 'changed']:
                        continue
                    else:
                        if condition_class is None:
                            loop.add_condition(condition)
                        else:
                            loop.add_new_condition(condition_class, condition)
                        return index
                elif fields[index] == '{\n':
                    if condition_class is None:
                        loop.add_condition(condition)
                    else:
                        loop.add_new_condition(condition_class, condition)
                    return True
        except:
            return False

    def create_touch_loop(self, fields, loop, index, condition_class):
        try:
            port = int(fields[index])
            if port not in range(1, 17):
                return False
            sensor = self.target.get_component_by_port(port)
            condition = None

            while True:
                index += 1
                if fields[index] == 'touched':
                    new_condition = TouchCondition(TouchConditions.TOUCHED, sensor)
                elif fields[index] == 'released':
                    new_condition = TouchCondition(TouchConditions.RELEASED, sensor)
                elif fields[index] == 'changed':
                    new_condition = OrCondition(TouchCondition(TouchConditions.TOUCHED, sensor), TouchCondition(TouchConditions.RELEASED, sensor))
                else:
                    return False

                if condition is None:
                    condition = new_condition
                elif fields[index - 1] == 'or':
                    condition = OrCondition(condition, new_condition)
                elif fields[index - 1] == 'and':
                    condition = AndCondition(condition, new_condition)

                index += 1
                if fields[index] == 'or' or fields[index] == 'and':
                    if fields[index + 1] in ['touched', 'released', 'changed']:
                        continue
                    else:
                        if condition_class is None:
                            loop.add_condition(condition)
                        else:
                            loop.add_new_condition(condition_class, condition)
                        return index
                elif fields[index] == '{\n':
                    if condition_class is None:
                        loop.add_condition(condition)
                    else:
                        loop.add_new_condition(condition_class, condition)
                    return True
        except:
            return False

    def add_action(self, action):
        self.actions.append(action)

    def execute(self):
        for block in self.actions:
            block.execute()