'''
Q2:- You will enter 2 value between 0 to 9 
if the entered value isaddition is greater than  5 then you will subtract the number with 5:
and if the value is lesser than the 5 then you will multiply that.
'''
firstval = int(input("Enter a number(0-9):- "))
secondval = int(input("Again Enter a number(0-9):- "))

sum = firstval + secondval
print(sum)
if sum > 5 :
    print("The sum is greater than 5 which is =",sum,"\nSo subtracting 5 from sum ans is ",sum-5)
else:
    print("The sum is less than 5 which is =",sum,"\nSo multiplying the sum with 5 ans is ",sum*5)
2