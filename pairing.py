class Pairing:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __contains__(self, item):
        return item in (self.left, self.right)
