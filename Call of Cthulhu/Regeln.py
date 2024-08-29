import random

class Character:
    def __init__(self, name, strength, constitution, dexterity, intelligence, power, charisma, size, education, sanity, luck, hit_points):
        self.name = name
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.power = power
        self.charisma = charisma
        self.size = size
        self.education = education
        self.sanity = sanity
        self.luck = luck
        self.hit_points = hit_points
        self.is_alive = True

    def roll_dice(self, sides=100):
        return random.randint(1, sides)

    def make_pow_roll(self):
        roll = self.roll_dice()
        success = roll <= self.power
        return roll, success

    def lose_sanity(self, points):
        self.sanity -= points
        if self.sanity <= 0:
            self.is_alive = False
        return self.sanity

    def restore_sanity(self, points):
        self.sanity += points
        return self.sanity

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.is_alive = False
        return self.hit_points
