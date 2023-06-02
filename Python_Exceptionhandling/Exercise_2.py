"""
Handling Multiple Exception

"""

a = input("please eneter first number :")

b = input("please eneter second number :")

try:
    r = a / int(b)

except ZeroDivisionError as e:
    print("Zero Division Exception")
    r=None


except TypeError as e:
    print("Exception is TypeError")
    r=None

print(r)