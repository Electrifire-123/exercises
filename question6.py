#  Write a program for calculating weather the entered year is leap year or not?

def isLeap():
    year = int(input("Enter a random year:- "))
    if ((0 == year % 4) and (0 != year % 100) or (0 == year % 400)):
        return "Leap Year"
    else:
        return "Not a Leap Year"

print(isLeap())
