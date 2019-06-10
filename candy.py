#Emrich-Michael Perrier
#Emrich
#eperrier@syr.edu
#Assignment 3 problem 1
#2/10/19
#Program draws a table with 10 choclate bars on it with a title above the table
from graphics import *

def main():
    #Draw Graphics Window
    win=GraphWin("Candy",500,500)
    win.setBackground("LightBlue")
    #Draw Table
    table = Oval(Point(50,100),Point(450,300))
    table.setFill("Tan")
    table.draw(win)
    #Draw Candy bars
    for i in range(120,420,30):
        bars=Rectangle(Point(i,150),Point(i-20,200))
        bars.setFill("Green")
        bars.draw(win)
    #Title
    Text(Point(200,400),"Candy Bars on a Table").draw(win)
main()