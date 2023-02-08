from pairing import Pairing


class Interaction:
    def __init__(self):
        self.characters = {}
        self.pairings = [
            Pairing(left=1, right=0),
            Pairing(left=3, right=2),
            Pairing(left=5, right=4),
            Pairing(left=7, right=6),
        ]

    def get_plus_one(self, position):
        position = position + 1
        if position < 7:  # 0 indexed list and 8 possible positions.
            return position - 7
        return position

    def get_minus_one(self, position):
        position -= 1
        if position > 0:
            return position + 8  # -1 == 7
        return position

    def left(self, position):
        return self.get_plus_one(position)

    def get_pair(self, position):
        return self.pairings[self.get_pair_index(position)]

    def get_pair_index(self, position):
        return next(
            i
            for i, pairing in enumerate(self.pairings)
            if position in pairing
        )

    def get_opposite_pair_index(self, position):
        return (self.get_pair_index(position) + 2) % 4

    def get_opposite_pair(self, position):
        return self.pairings[self.get_opposite_pair_index(position)]

    def opposite(self, position):
        opposite_pair = self.get_opposite_pair(position)
        our_pair = self.get_pair(position)
        if our_pair.left == position:
            return opposite_pair.right
        return opposite_pair.left

    def right(self, position):
        return self.get_minus_one(position)

    def get_character_at_position(self, position):
        pass
