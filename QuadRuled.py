#Emrich-Michael Perrier
#Emrich
#eperrier@syr.edu
#Assignment 3 part 2
#Feb 12 2019
#Making Graph Paper

from graphics import *

def main():
    #Set up graphics window
    win=GraphWin("Graph",600,600)
    win.setCoords(-3,-3,3,3)
    win.setBackground("White")
    #Draw the grid
    for i in range(-3,3):
        i=i+0.5
        v1=Line(Point(i,-3),Point(i,3))
        v1.draw(win)
    for i in range(-3,3):
        i=i+0.5
        v2=Line(Point(i+0.5,-3),Point(i+0.5,3))
        v2.draw(win)
    for i in range(-3,3):
        i=i+0.5
        h=Line(Point(-3,i),Point(3,i))
        h.draw(win)
    for i in range(-3,3):
        i=i+0.5
        h=Line(Point(-3,i+0.5),Point(3,i+0.5))
        h.draw(win)
    #Label Coordinates
    Text(Point(-2,-0.1),"-2").draw(win)
    Text(Point(2,-0.1),"2").draw(win)
    Text(Point(0.2,-2),"-2").draw(win)
    Text(Point(0.2,2),"2").draw(win)
    Text(Point(0,0),"0").draw(win)
    
main()