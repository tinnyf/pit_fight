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

    def right(self,position):
        return self.get_minus_one(self.position)