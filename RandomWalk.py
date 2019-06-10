#Emrich-Michael Perrier
#Emrich
#eperrier@syr.edu
#Assignment 8 part 1
#April 4 2019
#Making Graph Paper and plot circles that will randomly walk on the graph paper

from graphics import *
from random import randrange

def win():
    #Set up graphics window
    win=GraphWin("Graph",600,600)
    win.setCoords(-5,-5,5,5)
    win.setBackground("White")
    return win
    
def linepaper(win):
    #makes the window into a graph plot
    for i in range(-5,5):
        i=i+1
        v1=Line(Point(i,-5),Point(i,5))
        v1.draw(win)
    for i in range(-5,5):
        i=i+1
        h=Line(Point(-5,i),Point(5,i))
        h.draw(win)

def random():
#function to call random for either case 0,1,2 or 3
    num = randrange(0,4)
    return num

def walk(win):
    #draws green circle in origin
    green = Circle(Point(0,0),0.5)
    green.setFill("green")
    green.draw(win)
    #establishes variables
    stepCount = 0
    x,y = 0,0
    #while loop to keep randomly drawing circles until it gets to the edge of the graph
    while -4<x<4 and -4<y<4:
        m = random()
        if m == 0:
            x -= 1
        elif m == 1:
            x += 1
        elif m == 2:
            y -= 1
        elif m ==3:
            y += 1
        red = Circle(Point(x,y),0.5)
        red.setFill("red")
        red.draw(win)
        stepCount+=1
    return stepCount

def main():
    w = win()
    linepaper(w)
    steps = walk(w)
    #writes the amount steps taken
    count = "Count = ",steps
    msg = Text(Point(0,4.5),count)
    msg.draw(w)
main() 