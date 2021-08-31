"""
Name: Thomas Scola
lab1.py

Problem: This function calculates the area of a rectangle
"""


'''def calc_area():'''
def calc_rec_area():
        length = eval(input("Enter the length: "))
        width = eval(input("Enter the width: "))
        area = length * width
        print("Area =", area)

def calc_rec_vol():
    lengthh = eval(input("Enter the length: "))
    widthh = eval(input("Enter the width: "))
    heighth = eval(input("Enter the height: "))
    volume = lengthh * widthh * heighth
    print("Volume =", volume)

def shot_percentage():
    shotm = eval(input("enter the shots made: "))
    shott = eval(input("enter the total shots: "))
    shotper = shotm / shott
    print("Shot percentage = ", shotper)

def coffee():
    pound = eval(input("enter the amount of pounds purchased: "))
    cost = (pound * 10.50) + (pound * 0.86) + 1.50
    print("The total cost of coffee are", cost)

def kilometers_to_miles():
    """1 mile = 1.61 kilometers"""
    miles = eval(input("enter the amount of miles driven: "))
    driven = miles * 1.61
    print("The amount of kilometers driven are: ", driven)
