"""
Name: Thomas Scola
lab3.py

"""

def average():
    quantity = eval(input("How many grades do you have? "))
    total = 0
    for num in range(quantity):
        hw_grade = eval(input("Enter your homework grade: "))
        total = total + hw_grade


    average = total / quantity
    print("your average homework grades are", average)

average()


def tip_jar():
    total = 0
    for num in range (5):
        coins = eval(input("Input your change amount: "))
        total = total + coins
    print("The total amount of change is: $ ", total)

tip_jar()


def newton():
    x = eval(input("Enter your x value: "))
    n = eval(input("Enter how many times to improve the guess: "))
    total = 0
    for num in range (n):
        guess = ((n) + (x/n)) / 2
        total = total + guess
    print(" Your approximation is: ", guess)
newton()

def sequence():
    terms = int(input("Input the number of terms you would like to do."))
    top = 1
    for num in range(terms):
        remainder = num % 2
        top = (top + 2 * remainder)
        print(top, end = " ")

sequence()

"""
def pi():
pi()

the reason why I have not finished or started the pi problem is becuase I have a 5pm class that is located
at harborwalk east and I am walking there. 
"""
