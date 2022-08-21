'''
Q2. Write a program if user enter some number below 100  if  its odd print .
*
**
***
****

else print inverted in even:

******
****
***
**
*
and you  will ask user to enter the length of the triangle.
'''

def printPattern():
    randomNum = int(input("Enter a number (1 to 100):-"))
    length = int(input("Enter a length of triangle (1 to 100):-"))
    if randomNum%2 != 0:
        temp = 1
        while temp <= length:
         print("* " * temp)
         temp += 1
    else:
        tmp = 1
        while length >= tmp:
         print("* " * length)
         length -= 1

printPattern()
