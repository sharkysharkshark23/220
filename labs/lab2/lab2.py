import math
"""
Name: Thomas sCOLA
Arithmetic.py
collaborated with Jessica, Kristina, Jonathan
"""

def sum_of_threes():
    number = eval(input("what will be your upper bound?"))
    total = 0
    for num in range(3,number,3):
        total = total + num

    print("your total output", total)
        #ended for-loop
#sum_of_threes()

def multiplication_table():
    for row
        multiin range(1, 11):
        for column in range(1,11):
      print(rowcolumn, end="")
    print()
multiplication_table()

def triangle_area():
    a = eval(input("enter lenght a: "))
    b = eval(input("enter lenght b: "))
    c = eval(input("enter lenght c: "))

    s = (a+b+c)/(2)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("This is the area for a triangle", area)
#triangle_area()

def sumSquares():
    number = eval(input("what will be your lower bound?"))
    number_two = eval(input("what will be your upper bound?"))
    for num in range (number, number_two):
        calculations = (number**2)+(num**2)+(number_two**2)

    print(calculations)
    #enofcalcualtions
#sumSquares()

def power():
    base = eval(input("what will be your base?"))
    exponent = eval(input("what will be your power?"))
    total = 1
    for num in range(exponent):
        total *= base

    print("your total output", total)
power()

