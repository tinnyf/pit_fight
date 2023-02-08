from characters.character import Character


class Vlad(Character):
    def __init__(self, interaction):
        super().__init__(interaction)
        self.hp = 3
        self.init = 7

    def on_one(self):
        self.interaction.opposite(self.position).is_attacked(1, self)

    def on_four(self):
        self.interaction.left(self.position).is_attacked(1, self)
        self.heal(1,self)

    def on_six(self):
        self.interaction.left(self.position).is_attacked(1, self)
        self.interaction.opposite(self.position).is_attacked(1,self)

    def on_die(self):
        self.interaction.replace_character(self.position, Coffin(self.interaction)),
        self.active = False