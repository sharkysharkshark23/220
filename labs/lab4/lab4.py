"""
Name: Thomas Scola
lab4.py
Problem: To learn how to implement graphics
I certify this is mywork and my work only
"""

from graphics import *
import math
"""  <---  You can use tripled quotes to write a multi-line comment....

Modify the following function to:

Draw squares (20 X 20) instead of circles. Make sure that the center of the square
is at the point where the user clicks. Make the window 400 by 400.

Have each successive click draw an additional square on the screen (rather
than just moving the existing one).

Display a message on the window "Click again to quit" after the loop, and
wait for a final click before closing the window.
"""
"""
def squares():
   # Creates a graphical window
   width = 400
   height = 400
   win = GraphWin("Lab 4", width, height)

   # number of times user can move circle
   num_clicks = 5

   # create a space to instruct user
   inst_pt = Point(width / 2, height - 10)
   instructions = Text(inst_pt, "Click to move circle")
   instructions.draw(win)

   # builds a rectangle
   shape = Rectangle(Point(50, 50), Point(20,20))
   shape.setOutline("red")
   shape.setFill("red")
   shape.draw(win)

   # allows the user to click multiple times to move the circle
   for i in range(num_clicks):
       p = win.getMouse()
       c = shape.getCenter()  # center of circle

       # move amount is distance from center of circle to the
       # point where the user clicked
       dx = p.getX() - c.getX()
       dy = p.getY() - c.getY()
       clone_shape = shape.clone()
       clone_shape.move(dx,dy)
       clone_shape.draw(win)
       shape.move(dx, dy)

   win.getMouse()
   win.close()
squares()
"""
"""
def rectangle() :
    win = GraphWin ("Draw a square")
    win.setCoords (0.0, 0.0 , 10.0 , 10.0 )
    message = Text (Point (5, 0.5 ) , "Click on two points" )
    message.draw (win)
    # Get and draw three vertices of triangle
    P1 = win.getMouse ()
    P1.draw (win)
    P2 = win.getMouse()
    P2.draw(win)
    #cornerPoint = Rectangle.getP1()
    #cornerPoint = Rectangle.getP2()
# Use Polygon object to draw the triangle
    rectangle = Rectangle(P1, P2)
    rectangle.setFill("peachpuff")
    rectangle.setOutline ("cyan")
    rectangle.draw(win)
# Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
rectangle()
"""
def circle():

    circle()

"""
I have to leave early for a class at harbor walk east
"""
