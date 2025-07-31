class Rover:
    def __init__(self, x, y, direction):
        self.position = (x, y)
        self.direction = direction

    def execute_commands(self, commands):
        for command in commands:
            match command:
                case "F":
                    self.move_forward()
                case "B":
                    self.move_backward()
                case "R":
                    self.turn_right()
                case "L":
                    self.turn_left()
                
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
