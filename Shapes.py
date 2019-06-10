#  Shapes:  
#<Insert your name here>


# import the graphics package
from graphics import *
def main():

#####################################################################
# Part A:
#   Create/open a single graphics window:
#   1.  Its title is:  Shapes
#   2.  The window is 500 pixels wide and 250 pixels high
#   3.  The window's background is: tan
#   4.  The coordinate system goes from 0 to 5 in the x direction
#       and 0 to 2.5 in the y direction.
#
# All items created in the rest of the program should be placed in this window.
 win=GraphWin("Shapes",500,250)
 win.setBackground("tan")
 win.setCoords(0,0,5,2.5)
 
 
#####################################################################
# Part C:
#   Create a green circle (with radius of .3),
#              centered at the point (1.25,1.25)
#   Have the circle draw itself in the window.
 upperRight=Circle(Point(1.25,1.25),.3)
 upperRight.setFill("green")
 upperRight.draw(win)


#####################################################################
# Part D:
#   Draw a purple rectangle (height of .5, width of .2)
#           whose top-left corner is at point (.5,1)
 upperLeft=Rectangle(Point(0.5,1),Point(0.7,0.5))
 upperLeft.setFill("purple")
 upperLeft.draw(win)


#####################################################################
# Part E:
#   Draw a cyan triangle, whose vertices are at the points
#               (4.00,.05), (4.95,2.45), and (3.05,2.00)
 bottomLeft=Polygon(Point(4.00,.05), Point(4.95,2.45), Point(3.05,2.00))
 bottomLeft.setFill("cyan")
 bottomLeft.draw(win)


#####################################################################
# Part F:
#   Create and draw 10 points, starting at (.10,2.00),
#   with the x coordinates spaced 0.5 apart,
#   all with y coordinate 2.00.
#   Use a for loop with range(something in here)
 for i in range(40):
     T = (i+0.5)
#####################################################################
# Part G:
#   In addition to drawing the points in part F,
#   create and draw red circles of radius 0.3,
#   centered at each of the points from part F.
     middleRight=Circle(Point(T,2.00),.3)
     middleRight.setFill("red")
     middleRight.draw(win)

#####################################################################
# Part B;
#   Close the window with a mouse click
 win.getMouse()
 win.close()
main()