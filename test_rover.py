from rover import Rover
import pytest

def test_starting_position():
    """
    Test that the rover starts at the correct initial position.
    """
    rover = Rover(0,0,"N")
    assert rover.position == (0, 0), "Rover should start at position (0, 0)"
    assert rover.direction == "N", "Rover should face North"

test_command_data = [(0, 0, "S", ['f'], 0, 1, "S"),
                     (0, 1, "N", ['f'], 0, 0, "N"),
                     (0, 0, "E", ['f'], 1, 0, "E"),
                     (1, 0, "W", ['f'], 0, 0, "W")]

@pytest.mark.parametrize(("start_x", "start_y", "start_direction", "commands", "end_x", "end_y", "end_direction"), test_command_data)
def test_command_execution(start_x, start_y, start_direction, commands, end_x, end_y, end_direction):
    """
    Test the execution of a series of commands.
    """
    rover = Rover(start_x, start_y, start_direction)
    rover.execute_commands(commands)
    assert rover.position == (end_x, end_y), f"Rover should end at position ({end_x}, {end_y})"
    assert rover.direction == end_direction, f"Rover should face {end_direction} after executing commands"
