#  Lab 5:  Emrich-Michael Perrier
#  Draw 4 circles in a window

# import the graphics package
from graphics import *

#Greate a graphic window
win=GraphWin("Four Corners",400,200)

#Place a green circle in the upper right corner
upperRight=Circle(Point(370,30),10)
upperRight.setFill("green")
upperRight.draw(win)

#Place a yellow circle in the uppler left corner
upperLeft=Circle(Point(30,30),10)
upperLeft.setFill("yellow")
upperLeft.draw(win)
#Place a red circle in the lower right corner
lowerRight=Circle(Point(370,170),10)
lowerRight.setFill("red")
lowerRight.draw(win)
#Place a blue circle in the lower left corner
lowerLeft=Circle(Point(30,170),10)
lowerLeft.setFill("blue")
lowerLeft.draw(win)
#Click the mouse to close the window.
win.getMouse()
win.close()