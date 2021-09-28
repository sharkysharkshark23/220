import math
"""
Name: Thomas Scola
lab5.py
"""

from graphics import *



def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", 500, 500)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

    p1x = p1.getX()
    p1y = p1.getY()
    p2x = p2.getX()
    p2y = p2.getY()
    p3x = p3.getX()
    p3y = p3.getY()

    #calculations
    length1 = math.sqrt(((p2x - p1x)**2) + ((p2y - p1y)**2))
    length2 = math.sqrt(((p2x - p3x)**2) + ((p2y - p3y)**2))
    length3 = math.sqrt(((p3x - p1x)**2) + ((p3y - p1y)**2))

    perimeter = length1 + length2 + length3
    s = perimeter / (2)
    area = math.sqrt(s*(s - length1)*(s - length2)*(s - length3))

    print(perimeter)
    print(area)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()
triangle()
def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    strng = input("enter your string")
    print(strng[0])
    print(strng[10])
    print(strng[2:5])
    print(strng[0]+strng[-1])
    print(strng[0:3]*10)
    for char in strng():
        print(strng)
    print(len(strng))

process_string()

def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1,3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2, 3, 4]
    print(x)
    x = values[2, 3, 0]
    print(x)
    x = values[2, 0, 5]
    print(x)
    x = values[0] + values[2] + values[5]
    print(x)
    print(len(x))
process_list()

def main():
    # target()
    # triangle()
    # color_shape()
    #process_string()
    #process_list()
    pass


main()
