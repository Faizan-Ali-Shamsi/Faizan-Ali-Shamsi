import random

score = 10
randomNumber = random.randint(1, 10)
print("Guess the correct number!!")
while True:
    userInput = int(input("Guess: "))
    if userInput == randomNumber:
        print(f"Congrats, you won. Your score is {score}")
    else:
        print("Try again!")
        score -= 1
