import random
from dice import d6_dice
while True:
    num_dice = int(input("How many dice do you want to roll? "))
    dice = []
    total = []
    for i in range(num_dice):
            dice.append(random.randint(1, 6))
            total.append(dice[i])

    for die in range(num_dice):
            for line in d6_dice.get(dice[die]):
                    print(line)

    print(f"total: {sum(total)}")
    print("Roll again (1) | exit (2)")
    retry = int(input(""))
    if retry == 2:
        break
    else:
        continue
