class Alien:
    """
    Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            print("Already dead!")
    def is_alive(self):
        return self.health > 0
    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate += new_x_coordinate
        self.y_coordinate += new_y_coordinate
        return self.x_coordinate, self.y_coordinate
    def collision_detection(self, other):
        pass
def new_aliens_collection(coordinates):
    aliens_collection = []
    for coordinate in coordinates:
        alien = Alien(*coordinate)
        aliens_collection.append(alien)
    return aliens_collection