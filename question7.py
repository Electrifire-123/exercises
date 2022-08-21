'''
Q1. you have to create a health management system where you have to enter the 3 things :-
1. The name of the user.
2. Then you have to enter wheather he has to enter the log diet or the log the exercise.
3. If enters the he want to enter log diet then create a file with "name_diet.txt" and if exercise then "name_exercise.txt".
4. If he enters the log  and the user has already entered the diet log and you want to enter the second time then it should open that file and log the diet.
5. The format should be use the date time the current time ":"after that what you will append  that should be there.



diet log should look like.
11/08/2022 10:00 : 4 Apple with bowl of green salad



exercise log should look like.



11/08/2022 10:00 : bench press.



if there is any confusion you can drop your query below.

'''
import os
import time
# 📚 👋
def gymLogBook():
    #message
    print("               👋 Hi welcome To Diet🥗 And Exercise💪 Log Book 📚")

    # new user
    newuser = input("Plese enter Your Name:- ")

    # user choice
    newUsersChoice = int(input("Make your choice :-\n    1.Log '1' for Diet 🥗\n    2.Log '2' for Exercise 💪\n    note: please enter numbers only:- "))

    # diet/exercise log
    newLog = None

    # file name
    file_name = None
    if(newUsersChoice == 1):
        # file name
        file_name = f"{newuser}_diet.txt"

        # log
        newLog = input("Enter what to log in Diet:- \nExample:-'Skimmed Milk Paneer (100 grams)':- ")
    elif newUsersChoice == 2: 
        # file name
        file_name = f"{newuser}_exercise.txt"

        # log
        newLog = input("Enter what ot log in Exercise:-\nExample: 'bench press':- ")
    else :
        # if error occurs
        print("please provide a valid details")
    isFile = os.path.isfile(f"{file_name}")
    times = time.ctime(time.time())
    if isFile :
        file = open(f"{file_name}",'a')
        file.write(f"{times}-{newLog}\n")
        print("Successfully Updated your log \n Thank You 🙏")
    else:
        file = open(f"{file_name}", "x")
        file.write(f"{times}-{newLog}\n")
        print("Successfully created your log \n Thank You 🙏")
gymLogBook()
