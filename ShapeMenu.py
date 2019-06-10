#Emrich-Michael Perrier
#Emrich
#eperrier@syr.edu
#Assignment 7, Part 1
#3/25/19
#Program draws shapes with stars, not in the graphics window

#Function to draw the rectangle
def drawRect(width, height, pictureFile):
    w = width
    h = height
    for i in range(h):
        for i in range(w):
            print("*", end="",file=pictureFile)
        print(file=pictureFile)
#Function to draw the square        
def drawSquare(side, pictureFile):
    s = side
    drawRect(s,s,pictureFile)
#Function to draw the triangle
def drawTriangle(side, pictureFile):
    s = side
    for i in range(s):
        print("*"*(i+1),file=pictureFile)
    print(pictureFile)
#Asks for what shape you want or if you want to quit and returns it
def menu():
    print("Enter a Choice: ")
    print("r for rectangle")
    print("s for square")
    print("t for triangle")
    print("q to quit")
    c = input("")
    return c

#Main opens file, calls menu(), runs the while loop and depending on your choice will draw the shapes and when the user chooses q it will close the file and tell you the file is ready
def main():
    file = open("pictureFile.txt","w")
    c = menu()
    while c != "q":
        if c == "r":
            w, h = eval(input("Enter width, height: "))
            drawRect(w,h,file)
        elif c == "s":
            s = eval(input("Enter side length: "))
            drawSquare(s, file)
        elif c == "t":
            s = eval(input("Enter the base of Triangle (is equal to height): "))
            drawTriangle(s, file)
        c = menu()
        if c == "q":
            file.close()
            print("your picture is available in 'pictureFile.txt'")
main()
    