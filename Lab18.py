#Lab 18
#Emrich-Michael Perrier

from graphics import *

class Bball:
    def __init__(self, color, center, dir=1):
        self.circle = Circle(center,1)
        self.direction = dir
        self.circle.setFill(color)
        
    def draw(self, win):
        self.circle.draw(win)
        
    def move(self,win):
        dy = self.circle.getCenter().getY()
        if dy<=9:
            self.circle.move(0, self.direction)
        elif dy >= -9:
            self.circle.move(0, -(self.direction))
        dy = self.circle.getCenter().getY()
        return dy
    
def win():
    win=GraphWin("Lab18",1000,1000)
    win.setBackground("black")
    win.setCoords(-10,-10,10,10)
    return win

def main():
    w = win()
    c = Point(0,-9)
    d = Point(5,9)
    ball = Bball("red",c, 1)
    ball.draw(w)
    downBall = Bball("blue",d,1)
    downBall.draw(w)
    while win.checkKey()!='q':
        y = ball.move(win)
        #y = downBall.move(win)
        if y >= 9:
            ball.direction = -1
        elif y <= -9:
            ball.direction = 1
    win.close()
main()