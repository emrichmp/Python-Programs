#Emrich-Michael Perrier
#Emrich
#eperrier@syr.edu
#Assignment 3 part 3
#Feb 12 2019
#Making Graph Paper

from graphics import *

def main():
    #Set up graphics window
    win=GraphWin("Graph",700,600)
    win.setCoords(-4,-3,3,3)
    win.setBackground("White")
    #Draw the grid
    v=Line(Point(-3,-3),Point(-3,3))
    v.draw(win)
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
    #Fill ins
    #Number of points
    n=Text(Point(-3.5,2.5),"Number of Points")
    n.setSize(7)
    n.draw(win)
    pointBox=Entry(Point(-3.5, 2.2), 3)
    pointBox.setText("0")  #default value will be 0
    pointBox.draw(win)
    #X Value
    Text(Point(-3.5,1),"X").draw(win)
    xBox=Entry(Point(-3.5, 0.7), 3)
    xBox.setText("0")  #default value will be 0
    xBox.draw(win)
    #Y Value
    Text(Point(-3.5,0),"Y").draw(win)
    yBox=Entry(Point(-3.5, -0.3), 3)
    yBox.setText("0")  #default value will be 0
    yBox.draw(win)
    #Draw points
    win.getMouse()
    pn=int(pointBox.getText())
    for i in range(pn):
        x=float(xBox.getText())
        y=float(yBox.getText())
        xt=Text(Point(x,y),i+1).draw(win)
        xt.setFill("Red")
        xBox.setText("0")
        yBox.setText("0")
        win.getMouse()
    #click mouse to close window
    win.getMouse()
    win.close()
main()