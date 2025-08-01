from rover import Rover
import pytest

def test_starting_position():
    """
    Test that the rover starts at the correct initial position.
    """
    rover = Rover(0,0,"N")
    assert rover.position == (0, 0), "Rover should start at position (0, 0)"
    assert rover.direction == "N", "Rover should face North"

test_command_data = [(0, 0, "S", "F", 0, 1, "S"),
                     (0, 1, "N", "F", 0, 0, "N"),
                     (0, 0, "E", "F", 1, 0, "E"),
                     (1, 0, "W", "F", 0, 0, "W"),
                     (0, 0, "N", "RR", 0, 0, "S"),
                     (0, 0, "N", "RFL", 1, 0, "N"),
                     (0, 0, "N", "RFLB", 1, 1, "N"),
                     (0, 0, "N", "RFFL", 2, 0, "N"),
                     (0, 0, "N", "RFRFFLF",	2, 2, "E"),
                     (0, 0, "N", "RRFFLFFFRF", 3, 3, "S"),
                     (1, 2, "W", "FLF",	0, 3, "S"),
                     (1, 2, "E", "FFFRFFFRBBBLFFLFFL", 9, 7, "N"),
                     (0, 0, "N", "2R", 0, 0, "S"),
                     (0, 0, "N", "R2FL", 2, 0, "N"),
                     (0, 0, "N", "RRFFL3FRF", 3, 3, "S"),
                     (1, 2, "E", "3FR3FR3BL2FLFFL",	9, 7, "N"),
                     (1, 2, "E", "R15FL12F", 13, 17, "E")]

@pytest.mark.parametrize(("start_x", "start_y", "start_direction", "commands", "end_x", "end_y", "end_direction"), test_command_data)
def test_command_execution(start_x, start_y, start_direction, commands, end_x, end_y, end_direction):
    """
    Test the execution of a series of commands.
    """
    rover = Rover(start_x, start_y, start_direction)
    rover.execute_commands(commands)
    assert rover.position == (end_x, end_y), f"Rover should end at position ({end_x}, {end_y})"
    assert rover.direction == end_direction, f"Rover should face {end_direction} after executing commands"


test_command_data_with_grid = [(2, 2, 0, 0, "E", "FF", 0, 0, "E"),
                               (2, 2, 0, 0, "N", "F", 1, 0, "S"),
                               (4, 4, 0, 0, "N", "FLFLF", 1, 0, "S")]

@pytest.mark.parametrize(("grid_x", "grid_y", "start_x", "start_y", "start_direction", "commands", "end_x", "end_y", "end_direction"), test_command_data_with_grid)
def test_command_execution_with_grid(grid_x, grid_y, start_x, start_y, start_direction, commands, end_x, end_y, end_direction):
    """
    Test the execution of a series of commands in a grid.
    """
    rover = Rover(start_x, start_y, start_direction)
    rover.set_gridsize(grid_x, grid_y)
    rover.execute_commands(commands)
    rover.wrap()
    assert rover.position == (end_x, end_y), f"Rover should end at position ({end_x}, {end_y})"
    assert rover.direction == end_direction, f"Rover should face {end_direction} after executing commands"

test_command_data_with_obstacles = [((2, 2), [(0,1),(1,1)], (0, 0), "N", "RFRF", (1, 0), "S", False)]

@pytest.mark.parametrize(("gridsize", "obstacle_locations","start", "start_direction", "commands", "end", "end_direction", "completed_route"), test_command_data_with_obstacles)
def test_command_execution_with_grid(gridsize, obstacle_locations, start, start_direction, commands, end, end_direction, completed_route):
    """
    Test the execution of a series of commands in a grid considering obstacles.
    """
    grid_x, grid_y = gridsize
    start_x, start_y = start
    end_x, end_y = end

    rover = Rover(start_x, start_y, start_direction)
    rover.set_gridsize(grid_x, grid_y)
    rover.set_obstacles(obstacle_locations)
    rover.execute_commands(commands)
    rover.wrap()
    assert rover.last_route_status == completed_route, f"Route should be {completed_route}"
    assert rover.position == (end_x, end_y), f"Rover should end at position ({end_x}, {end_y})"
    assert rover.direction == end_direction, f"Rover should face {end_direction} after executing commands"


