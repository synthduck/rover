from rover import Rover

def test_starting_position():
    """
    Test that the rover starts at the correct initial position.
    """
    rover = Rover(0,0,"N")
    assert rover.position == (0, 0), "Rover should start at position (0, 0)"
    assert rover.direction == "N", "Rover should face North"

def test_forward_north():
    """
    Test moving the rover forward when facing North.
    """
    rover = Rover(0, 0, "N")
    rover.execute_commands(['f'])
    assert rover.position == (0, 1), "Rover should move to position (0, 1) when moving forward from (0, 0) facing North"
    assert rover.direction == "N", "Rover should still face North after moving forward"

def test_forward_south():
    """
    Test moving the rover forward when facing South.
    """
    rover = Rover(0, 0, "S")
    rover.execute_commands(['f'])
    assert rover.position == (0, -1), "Rover should move to position (0, -1) when moving forward from (0, 0) facing South"
    assert rover.direction == "S", "Rover should still face South after moving forward"

def test_forward_east():
    """
    Test moving the rover forward when facing East.
    """
    rover = Rover(0, 0, "E")
    rover.execute_commands(['f'])
    assert rover.position == (1, 0), "Rover should move to position (1, 0) when moving forward from (0, 0) facing East"
    assert rover.direction == "E", "Rover should still face East after moving forward"

def test_forward_west():
    """
    Test moving the rover forward when facing West.
    """
    rover = Rover(0, 0, "W")
    rover.execute_commands(['f'])
    assert rover.position == (-1, 0), "Rover should move to position (-1, 0) when moving forward from (0, 0) facing West"
    assert rover.direction == "W", "Rover should still face West after moving forward"