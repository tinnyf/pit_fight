from characters.character import Character
from interaction import Interaction


class Healer(Character):

    def __init__(self, interaction):
        super().__init__(interaction)
        self.init = 2
        self.hp = 3


    def on_one(self):
        for target in Interaction.all():
            target.heal(1, self)

    def on_two(self):
        self.heal(1, self)
        self.ally.heal(1, self)
        self.interaction.left(self.position).heal(1, self)

    def on_four(self):
        self.ally.heal(1, self)
        self.heal(1, self)

    def on_six(self):
        self.ally.heal(2, self)