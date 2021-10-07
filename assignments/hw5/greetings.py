"""
Name:Thomas Scola
greetings.py
Problem: to make a greeting card for grandma
Certification of Authenticity: I certify that this is entirely my own work.

"""
import time
from graphics import GraphWin, Point, Line, Circle, Polygon

def main():
    win = GraphWin("Happy Valentine's Day!", 400, 400)
    #arrow
    p1 = Point(-200, 300)
    p2 = Point(-60, 150)
    arrow = Line(p1, p2)
    arrow.draw(win)

    #circles
    a = Circle(Point(225,150), 35)
    a.setFill("red")
    a.setOutline("red")
    a.draw(win)
    b = Circle(Point(175,150), 35)
    b.setFill("red")
    b.setOutline("red")
    b.draw(win)
    #GEt and draw three vertices of triangle
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)
    p5 = win.getMouse()
    p5 .draw(win)
    triangle = Polygon(p3, p4, p5)
    triangle.setFill("red")
    triangle.setOutline("red")
    triangle.draw(win)

    #arrow move
    for num in range(50):
        arrow.move(60, -10)
        time.sleep(.25)
    win.getMouse() # pause for click in window
    win.close()

if __name__ =='__main__':
    main()
