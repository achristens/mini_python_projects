import random

# randomly choose number 1-6
dice = random.randint(1, 6)

# print the number
print(dice)

# ask to roll agaiin y/n
while True:
    roll_again = raw_input("Would you like to roll again? Y/n    ")

    if roll_again == 'Y':
        new_roll = random.randint(1, 6)
        print(new_roll)
    elif roll_again == 'n':
        print("Thank you for playing!")
        break
