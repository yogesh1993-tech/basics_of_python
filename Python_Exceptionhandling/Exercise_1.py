"""
Genric way to hnadel exception
a = input("please eneter first number :")

b = input("please eneter second number :")

try:

    result = int(a) / int(b)

except Exception as e:
    print("Exception is ",type(e))

print(result)

"""

"""Manual way to handel exception """



a = input("please eneter first number :")

b = input("please eneter second number :")

try:

    result = int(a) / int(b)

except ZeroDivisionError as e:
    print("Zero Division Error Exception")
    result = None
    print("Division is ",result)