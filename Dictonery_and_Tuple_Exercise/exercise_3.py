''' Write circle_calc() function that takes radius of a
circle as an input from user and then it calculates and returns area,
 circumference and diameter. You should get these values in your
main program by calling circle_calc function and then print them'''



def cal_circle():
    radius = int(input("Please enetr radius  : "))
    area = 3.14 * radius * radius
    print(f"Area of the circle is {area}")

def cal_rect():
    length = int(input("Please enetr length  : "))
    width = int(input("Please enetr width  : "))
    area = length * width
    print(f"Area of the Rectangle is {area}")
def main():
    op = input("Which area you want to calculate circle,square,rectangle :")
    if op == "circle":
        cal_circle()
    elif op == "rectangle":
        cal_rect()


if __name__=='__main__':
    main()