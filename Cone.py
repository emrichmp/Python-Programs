#Cone.py
#Emrich-Michael Perrier
#This program finds the surface area and volume of a cone given the height and radius
import math
def main():
    #Asks for the height and radius of the cone
    h = eval(input("Enter height of the Cone: "))
    r = eval(input("Enter Radius of the Cone: "))
    #Computes volume
    v = math.pi*(r**2)*h*(1/3)
    #Computes Surface area
    SA = math.pi*r*(r+math.sqrt((h**2)+(r**2)))
    #Prints the results
    print(v," Cubic units")
    print(SA," Square units")
main()
