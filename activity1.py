import random
playing=True
number=str(random.randint(0,9))
print("I will generate a random number from 0-9 and you have to guess the number")
while playing:
    guess=input("Enter your guess:")
    if guess==number:
        print("You win")
        print("The number was:",number)
        break
    else:
        print("Not quite. Try again")