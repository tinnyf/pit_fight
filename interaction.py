class Interaction:
    def __init__(self):
        self.characters = {}
        self.pairings = [
            {
                'left': 1,
                'right': 0,
            },
            {
                'left': 3,
                'right': 2,
            },
            {
                'left': 5,
                'right': 4,
            },
            {
                'left': 7,
                'right': 6,
            },
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

    def in_pairing(self, position, pairing):
        return position in pairing.values()

    def get_pair_index(self, position):
        return next(
            i
            for i, pairing in enumerate(self.pairings)
            if self.in_pairing(position, pairing)
        )

    def get_opposite_pair_index(self, position):
        return (self.get_pair_index(position) + 2) % 4

    def get_opposite_pair(self, position):
        return self.pairings[self.get_opposite_pair_index(position)]

    def opposite(self, position):
        opposite_pair = self.get_opposite_pair(position)
        our_pair = self.get_pair(position)
        if our_pair['left'] == position:
            return opposite_pair['right']
        return opposite_pair['left']

    def right(self, position):
        return self.get_minus_one(position)

    def get_character_at_position(self, position):
        pass
