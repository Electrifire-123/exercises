'''
Q1. Write a program to make the user guess the number and how :- take user input ask the input from user till he enter's the correct value.

'''
# imported module random
import random
random_num = random.random()
num = int(random_num*100)
print(int(num))


def guessTheNumber():
    user = 0
    while num != user:
        user = int(input(" Hello Guess the number below 100:- "))
    print("💐Congrats You Guessed it right🤝")
guessTheNumber()
