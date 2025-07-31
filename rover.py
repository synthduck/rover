class Rover:
    def __init__(self, x, y, direction):
        self.position = (x, y)
        self.direction = direction

    def set_gridsize(self, x, y):
        self.gridsize = (x, y)  
    
    def wrap(self):
        x, y = self.position
        grid_x, grid_y = self.gridsize
        self.position = (x % grid_x, y % grid_y)

    def _repeat(self, multiplier, command):
        if multiplier == "":
            multiplier = 1
        else:
            multiplier = int(multiplier)
    
        for _ in range(multiplier):
            command()

    def execute_commands(self, commands):
        multiplier = ""
        for command in commands:
            match command:
                case "F":
                    self._repeat(multiplier, self.move_forward)
                    multiplier = ""
                case "B":
                    self._repeat(multiplier, self.move_backward)
                    multiplier = ""
                case "R":
                    self._repeat(multiplier, self.turn_right)
                    multiplier = ""
                case "L":
                    self._repeat(multiplier, self.turn_left)
                    multiplier = ""
                case _:
                    multiplier += command
    
    def move_forward(self):
        x, y = self.position
        if self.direction == "N":
            self.position = (x, y - 1)
        elif self.direction == "S":
            self.position = (x, y + 1)
        elif self.direction == "E":
            self.position = (x + 1, y)
        elif self.direction == "W":
            self.position = (x - 1, y)

    def move_backward(self):
        x, y = self.position
        if self.direction == "N":
            self.position = (x, y + 1)
        elif self.direction == "S":
            self.position = (x, y - 1)
        elif self.direction == "E":
            self.position = (x - 1, y)
        elif self.direction == "W":
            self.position = (x + 1, y)
    
    def turn_right(self):
        directions = ["N", "E", "S", "W"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4] 

    def turn_left(self):
        directions = ["N", "W", "S", "E"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
