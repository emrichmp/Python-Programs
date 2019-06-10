# Emrich-Michael Perrier
# Emrich
# eperrier@syr.edu
# Assignment 2, problem 2.
# February 7, 2019
# Compute distances between points

import math
def main():
    #collect data
    p = eval(input("How many pairs of points? "))
    #do calculations
    for i in range(p):
        sx,sy = eval(input("start point - enter x, y "))
        ex,ey = eval(input("end point - enter x, y "))
        x = ex-sx
        y = ey-sy
        x = abs(x)
        y = abs(y)
        p = x**2 + y**2
        p = math.sqrt(p)
        #print results
        print("Distance :", p)
main()