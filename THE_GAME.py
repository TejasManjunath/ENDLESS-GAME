import random

print("PLay this game at your own risk")

while True:
    number = random.randint(1,1000000000000)
    guess = int(input("GUess the number between 1 and 1000: "))
        
    if guess == number:
        print("COngratulation! YOU WIN")
        break
    elif(guess != number):
        print("Nope, Try again!")
    else:
        print("Invalid input")