""" Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should tell
you in which month that expense occurred.
If expense is not found then it should print that as well.
"""

Month_exp = {"Jan":2340,"Feb":2500,"March":2100, "April":3100, "May":2980}

user = int(input("Please Enter Expense Amount : "))

for month ,exp  in Month_exp.items():

    if exp == user:
        print("Month is : " + month)
        break;
        
    if exp != user:
        print("Invalid Month")

