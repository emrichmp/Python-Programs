# processRectangle.py
# by Emrich-Michael Perrier
# Compute the area and perimeter of a rectangle.

# Ask for name.
name = input("What is your name? ")
# Ask for length and width.
length=eval(input("What is the rectangles length? "))
width=eval(input("What is the rectangles width? "))
# compute area and perimeter.
area=length * width
perimeter=length+length+width*width
# print results.
print("Hi "+name+"!")
print("Your rectangle has area ",area)
print("Your rectangle has perimeter ",perimeter)
