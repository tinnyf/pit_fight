from characters.character import Character
from interaction import Interaction


class Piper(Character):

    def __init__(self, interaction):
        super().__init__(interaction)
        self.init = 6
        self.hp = 4
        self.retaliate = 0

    def on_one(self):
        print("Piper's 1st ability triggers, she gets 1 armour and 1 retaliate.")
        self.armour += 1
        self.retaliate += 1

    def on_two(self):
        print("Piper's 2nd ability triggers, she deals 1 damage left and gets 1 retaliate.")
        self.interaction.left(self.position).is_attacked(1, self)

    def on_three(self):
        print("Piper 3 shields for 2")
        self.armour += 2

    def on_four(self):
        print("Piper 4 shields for 2")
        self.armour += 2
