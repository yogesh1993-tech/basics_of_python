"""

## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
# Write a program that asks user to enter a city name and it should tell which country the city belongs to

"""

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

cuser =input("Please Enter City Name :")

user=cuser.lower()

if user in india:
    print("User belongs to india ")
elif user in bangladesh:
    print("user belongs to bangladesh")
elif user in pakistan:
    print("user belongs to pakistan")
elif user not in india and bangladesh and pakistan :
    print("Invalid city name")
