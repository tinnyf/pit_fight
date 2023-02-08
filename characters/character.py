class Character():

    def __init__(self, interaction, hp_max = 3, init =7):
        self.ally = None
        self.position = None
        self.interaction = interaction
        self.hp_max = hp_max
        self.hp = self.hp_max
        self.init = init
        self.armour = 0
        self.active = False

    def on_one(self):
        pass

    def on_two(self):
        pass

    def on_three(self):
        pass

    def on_four(self):
        pass

    def on_five(self):
        pass

    def on_six(self):
        pass

    def on_enter(self):
        pass

    def on_die(self):
        pass

    def passive(self):
        pass

    def on_heal(self, heal):
        self.hp += heal
        if self.hp > self.hp_max:
            self.hp = self.hp_max

    def heal(self, healer, heal):
        self.on_heal(heal)

    def is_attacked(self, attacker, damage):
        self.on_damage(damage)

    def takes_damage(self, damage):
        self.on_damage(damage)

    def on_damage(self, damage):
        if self.armour > damage:
            self.armour -= damage
        elif self.armour > 0:
            damage = damage - self.armour
            self.armour = 0
            self.on_damage(damage)
        else:
            self.lose_hp(damage)

    def lose_hp(self, loss):
        self.hp -= loss
        if self.hp <= 0:
            self.die

    def die(self):
        self.on_die()
        self.active = False

    def on_select(self):
        self.active = True

    def on_roll(self, dice):
        rolldict = {
            1: self.on_one,
            2: self.on_two,
            3: self.on_three,
            4: self.on_four,
            5: self.on_five,
            6: self.on_six
        }
        return rolldict[dice]

    def on_select(self, position, ally):
        self.position = position
        self.ally = ally

    def on_round_end(self):
        self.armour = 0