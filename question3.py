'''
Q3:- Write a code in which you have to input the person country:
you have to ask please enter only:-
1. South Africa
2. India
3.Saudi arab
you have to code in such a way:
when you will make input for country you  have to match them with these 3 country, and ask for age and SEX(male/female) then if:

1. south Africa :- Male and above 18 then he can vote and female above 21 then she can vote:
2. Saudi arabia:- Male above 21 can vote and female cant vote.
3. India :- Both male and female can vote above 18.


Note:- Please try to use concepts that has been used and taught in classes till now the code having advance concepts will be disqualified .

'''
print(" Please Enter only this countries codename :\n Saudi Arabia-KSA\n South Africa-SA\n India-IN")
country = input("Enter your Country name:- ")
if country == "Saud Arabia" or "India" or "South Africa":
    print("Ok, So your from ",country,"\nnow please provide following details")
    userDetails = {
        "country" : country,
        "sex" : input("Enter Gender (male/femail):- "),
        "age" : int(input("Enter your Age:- "))
    }
if country == "SA" and userDetails["sex"] == "male" and userDetails["age"] >= 18:
    print("You can vote in South Africa",country)
elif country == "SA" and userDetails["sex"] == "female" and userDetails["age"] >= 21:
    print("You can vote in South Africa",country)
elif country == "KSA" and userDetails["sex"] == "male" and userDetails["age"] >= 21:
    print("You can vote in Saudi Arabia",country)
elif country == "KSA" and userDetails["sex"] == "female":
    print("You can't vote in Saudi Arabia",country)
elif country == "IN" and userDetails["age"] >= 18:
    print("You can vote in India",country)
else:
    print("You can't vote")