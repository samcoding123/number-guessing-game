import random
print("number guessing name")

number = random.randint(1, 9)
chances = 0

while chances < 5:

    guess = int(input("enter your guess: "))

    if guess == number:

        print ("You won")

        break

    elif guess < number:

        print ("your guessed number was to low, type a higher number")

    else: 

        print("your guess was to high, bye bye.")

    chances += 1

    if not chances < 5:

            print("you lose, the number is", number)
    