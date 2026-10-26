# Number Guessing Game

import random
secret_number = random.randint(1, 10)

attempts = 3

while attempts > 0:
    guess = int(input("Enter a number between 1 and 10: "))

    if guess < 1 or guess >10:
        print("Entered number is out of the range")
        continue
    if guess == secret_number:
        print("congratulations! It's a correct guess")
        break

    elif guess < secret_number:
        print("It's too low than the secret number")

    else:
        print("It's too high than the secret number")
    attempts = attempts - 1

else:
    print("Better luck next time!")
    print("The correct number was:", secret_number)

#Multiplication Table Generator

number = int(input("Enter a number between 1 to 10: "))

for i in range(1, 11):
    result = number*i
    print(number, "*", i, "=", result)
else:
    print("Enter a number in between the range")


# BMI Calculator

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))


def calculate_bmi(weight, height):
    if height <= 0:
        print("Height must be greater than 0")
        return

    bmi = weight / (height ** 2)
    print("Your BMI is:", bmi)


calculate_bmi(weight, height)
