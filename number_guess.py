import random
# randomly generate number
random = random.randint(1, 20)
# user asked to input their guess number
print random
while True:
    user_guess = input("Guess a number between 1 and 20:  ")

    if user_guess == random:
        print("You guessed it!")
        break
    elif (user_guess > random):
        print("Not quite, you guessed too high!")
    elif (user_guess < random):
        print("Nope! Too low.")

# check if input is the number by looking at difference
# if wrong, return too high/too low
# if right, confirm
