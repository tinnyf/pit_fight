class Interaction:

    def __init__(self):
        self.characters = {}


    def get_plus_one(self, position):
        position = position + 1
        if position < 7: #0 indexed list and 8 possible positions.
            return position - 7
        return position


    def get_minus_one(self, position):
        position -= 1
        if position >0:
            return position + 8 # -1 == 7
        return position

    def left(self, position):
        return self.get_plus_one(self,position)

    def opposite(self, position):
        return(position)

    def right(self,position):
        return self.get_minus_one(self.position)


    def get_character_at_position(self, position):
        pass







def tests():
    opposite_tests()


def opposite_tests():
    assert Interaction.opposite(1) == 4, "Output should be 4"
    assert Interaction.opposite(2) == 7, "Output should be 7"
    assert Interaction.opposite(3) == 6, "Output should be 6"
    assert Interaction.opposite(0) == 5, "Output be 5"