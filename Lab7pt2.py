from graphics import *

def main():
    #Set up the graphic window
    win=GraphWin("Lab 7",800,600)
    win.setCoords(0,0,4,3)
    
    #Instructions for Circle
    Text(Point(2,2.8),"Click to move circle").draw(win)
    
    pinkCircle=Circle(Point(0.6,2.4),.5)
    pinkCircle.setFill("pink")
    pinkCircle.draw(win)
    
     #Line
    hl=Line(Point(2,0),Point(2,3))
    hl.setWidth(3)
    hl.draw(win)
    
    for i in range(5):
        win.getMouse()
        pinkCircle.move(0.2,0)
    #Draw Blue Rectangle    
    blueRectangle=Rectangle(Point(.5,.5),Point(1.5,1))
    blueRectangle.setFill("Blue")
    blueRectangle.setOutline("Light Blue")
    blueRectangle.draw(win)
    #Make a clone of the rectangle
    rectClone=blueRectangle.clone()
    rectClone.move(1.5,0)
    rectClone.setFill("Green")
    rectClone.setOutline("Dark Green")
    rectClone.draw(win)
    #Close the window
    win.getMouse()
    win.close()
main()