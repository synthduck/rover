class Rover:
    def __init__(self, x, y, direction):
        self.position = (x, y)
        self.direction = direction

    def execute_commands(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
                
    def move_forward(self):
        x, y = self.position
        if self.direction == "N":
            self.position = (x, y + 1)
        elif self.direction == "S":
            self.position = (x, y - 1)
        elif self.direction == "E":
            self.position = (x + 1, y)
        elif self.direction == "W":
            self.position = (x - 1, y)