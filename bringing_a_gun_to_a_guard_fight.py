class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, b):
        return ((self.x - b.x) ** 2 + (self.y - b.y) ** 2) ** 0.5

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)


class Line(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Line({} -> {})".format(self.a, self.b)


epsilon = 10e-5


def is_between(a, b, c):
    crossproduct = (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)
    if abs(crossproduct) > epsilon:
        return False

    dotproduct = (c.x - a.x) * (b.x - a.x) + (c.y - a.y) * (b.y - a.y)
    if dotproduct < 0:
        return False

    squaredlengthba = (b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y)
    if dotproduct > squaredlengthba:
        return False

    return True


def answer(dimensions, your_position, guard_position, distance):
    """
    Beam can't travel more than 1000 units

    :param dimensions:
    :param your_position:
    :param guard_position:
    :param distance:
    :return:
    """
    # just brute force it? by taking all possible shots
    # and finding their length until they hit guard, me or run out
    player = Point(*your_position)
    guard = Point(*guard_position)
    count = 0
    memo = {}
    walls = [
        Line(Point(0, 0), Point(0, dimensions[1])),
        Line(Point(0, 0), Point(dimensions[0], 0)),
        Line(Point(0, dimensions[1]), Point(dimensions[0], dimensions[1])),
        Line(Point(dimensions[0], 0), Point(dimensions[0], dimensions[1]))
    ]

    for w in walls:
        print(w)
    for vec in [[x, y] for x in range(-dimensions[0], dimensions[0]) for y in range(-dimensions[1], dimensions[1])]:
        cur_dist = 0
        # begin firing and check each line for a collision
        # each vec is a bearing from where we are currently

        print vec,
        cur_pos = Point(player.x, player.y)
        while cur_dist <= distance:
            # fire the beam at the direction given,
            # if it hits a corner, negate the beam
            # if me or the guard are along the beam,
            # get the distance to the person


    return count


if __name__ == "__main__":
    print(answer([3, 2], [1, 1], [2, 1], 4))  # 7
    # print(answer([300, 275], [150, 150], [185, 100], 500))  # 5
