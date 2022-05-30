import converters
# from converters import files_function
# modules is used to break up our files
from converters import find_max
import random

print(find_max([1, 4, 6, 7, 56, 3]))
members = ['wilson', 'john']
leader = random.choice(members)
print(leader)
for i in range(4):
    print(random.random())
    print(random.randint(10, 20))


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice)
