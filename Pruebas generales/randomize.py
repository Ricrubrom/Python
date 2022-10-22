import random


class dice:
    def roll(self):
        roll = (random.randint(1, 6), random.randint(1, 6))
        return roll


d = dice()
print(d.roll())
