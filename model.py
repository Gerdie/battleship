
class Player(object):

    def __init__(self, name):
        self.name = name
        self.gameboard = self.create_gameboard(5, 5)

    def lay_ships(self, ship_length, start_pt, end_pt):
        if start_pt.x == end_pt.x:
            points = [(start_pt.x, y) for y in range(min([start_pt.y, end_pt.y]), max([start_pt.y, end_pt.y]))]

    @staticmethod
    def create_gameboard(width, length):
        return [['?'] * width for l in xrange(length)]
