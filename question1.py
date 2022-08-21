'''
Q1:- Make a program in which you will be entering the name of the person
age of him as well
person will enter the year of birth:
age =
If their name is "Priyanka"or "jhanvi" or "sohail" you will print their false value:{dictionary}  

'''

falseUsers = {
    "1" : "priyanka",
    "2" : "janhnvi",
    "3" : "sohail"
}
input_name = input("Enter Your Name:-")
input_age = int(input("Enter Your Birth Year:- "))
current_year = 2022
if input_name in falseUsers.values() :
    input_age+=5
    print("Your Name is ",input_name,"\nAnd you age is :-",current_year-input_age)
else :
    print("Your Name  is ",input_name,"\nAnd you age is ",2022-input_age)

