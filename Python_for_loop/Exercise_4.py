"""
Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message

"""

km = ["1km","2km","3km","4km","5km"]


ans =" "
for k in km :
    user = input(f" till now {k} done are you tired?:")
    if user == "no" and k == "5km":
        print("congratulations race completed")
    elif user == "yes":
        print("Sorry you didn't finish the race")
        break

