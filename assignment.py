
import datetime

def logBook():
    user = input("Enter you name:- ")
    diet_excercise = int(input("Enter 1 for Diet, 2 for Excercise:- "))
    if(diet_excercise == 1):
        log = input("Enter you diet for today:- ")
        file = open(f"{user}_diet.txt","a")
        print("Diet logged Successfully")
    elif diet_excercise == 2 :
        log = input("Enter your Excercise for today:- ")
        file = open(f"{user}_excercise.txt","a")
        print("Excersice Logged successfully")
    

logBook()