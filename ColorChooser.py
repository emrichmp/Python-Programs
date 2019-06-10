# Emrich-Michael Perrier
# Emrich
# eperrier@syr.edu
# Assignment 7, part 2
# 3/27/19
# Color chooser clicks rectangles to change the color of a circle and then quits

from graphics import *
#draws all the shapes and establishes the graphics window

#checks which rectangle the mouse collision is in
def checkButtonClicked(clickedPoint, leftLower, rightUpper):
    x1 = leftLower.getX()
    y1 = leftLower.getY()
    x2 = rightUpper.getX()
    y2 = rightUpper.getY()
    if ClickedPoint.getX >= x1 and clickedPoint.getX()<= x2 and ClickedPoint.getY >= y1 and clickedPoint.getY()<= y2:
        return 1
    else:
        return 0

def main():
# establishes window and coordinates
    win=GraphWin("window",1200,800)
    win.setBackground("black")
    win.setCoords(0,0,12,8)
# draws rectangles and the circle
    red = Rectangle(Point(3,3),Point(2,2))
    red.setFill("red")
    red.draw(win)
    blue = Rectangle(Point(10,3),Point(11,2))
    blue.setFill("blue")
    blue.draw(win)
    green = Rectangle(Point(3,6),Point(2,5))
    green.setFill("green")
    green.draw(win)
    white = Rectangle(Point(10,6),Point(11,5))
    white.setFill("white")
    white.draw(win)
    circ=Circle(Point(6.5,4),1)
    circ.setFill("green")
    circ.draw(win)
    
    clickedPoint = win.getMouse()
    Color = checkButtonClicked(clickedPoint, (2,2), (3,3))
    if Color == 1:
        cirColor = "red"
    else:
        Color = checkButtonClicked(clickedPoint, (10,3), (11,2))
    if Color == 1:
        circColor = "blue"
    else:
        Color = checkButtonClicked(clickedPoint, (2,5), (3,6))
    if Color == 1:
        circColor = "green"
                        

        
main()