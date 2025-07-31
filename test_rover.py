from rover import Rover

def test_starting_position():
    """
    Test that the rover starts at the correct initial position.
    """
    rover = Rover(0,0,"N")
    assert rover.position == (0, 0), "Rover should start at position (0, 0)"
    assert rover.direction == "N", "Rover should face North"