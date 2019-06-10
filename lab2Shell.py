Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> >>> 34
34
>>> #Emrich Perrier
>>> area = 3*4
>>> area
12
>>> lenth = 7
>>> width = 5
>>> area=length * width

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    area=length * width
NameError: name 'length' is not defined
>>> length = 7
>>> area=length * width
>>> length=7
>>> width=5
>>> area=length * width
>>> area
35
>>> length=10
>>> area
35
>>> area=length * width
>>> area
50
>>> 
=============================== RESTART: Shell ===============================
>>> area

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    area
NameError: name 'area' is not defined
>>> 27
27
>>> "27"
'27'
>>> apples=6
>>> apples
6
>>> "apples"
'apples'
>>> oranges="navel"
>>> oranges
'navel'
>>> 3.14159
3.14159
>>> type(apples)
<type 'int'>
>>> type(oranges)
<type 'str'>
>>> type(3.14)
<type 'float'>
>>> type("something in quotes")
<type 'str'>
>>> print (234)
234
>>> print ("pizza and salad")
pizza and salad
>>> print(apples)
6
>>> print (oranges)
navel
>>> print (123 + 7)
130
>>> print("I like" + oranges)
I likenavel
>>> print(apples + oranges)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(apples + oranges)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(3, 2, 1)
(3, 2, 1)
>>> print(apples, oranges,"plums")
(6, 'navel', 'plums')
>>> print(apples,oranges,"plums")
(6, 'navel', 'plums')
>>> print(apples,	oranges,	"plums")
(6, 'navel', 'plums')
>>> name = input("Enter your name: ")
SyntaxError: invalid syntax
>>> name = input("Enter your name: ")
Enter your name: emrich
>>> name
'emrich'
>>> age = input("Enter your age: ")
Enter your age: 19
>>> age
'19'
>>> age2eval(input("Enter your age "))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    age2eval(input("Enter your age "))
NameError: name 'age2eval' is not defined
>>> age2=eval(input("Enter your age "))
Enter your age 12
>>> age2
12
>>> 
=============================== RESTART: Shell ===============================
>>> name = input("What is your name? ")
What is your name? Emrich
>>> length = input("what is the length for the rectangle?")
what is the length for the rectangle?10
>>> width = input("What is the width for the rectangle?")
What is the width for the rectangle?5
>>> area=length*width
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    area=length*width
TypeError: can't multiply sequence by non-int of type 'str'
>>> area=length * width
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    area=length * width
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============================== RESTART: Shell ===============================
>>> name = input("What is your name? ")
What is your name? Emrich
>>> length=eval(input("What is the rectangles length? "))
What is the rectangles length? 10
>>> width=eval(input("What is the rectangles width? "))
What is the rectangles width? 5
>>> area=length * width
>>> perimeter=length+length+width*width
>>> print("Hi" name"!"
      
SyntaxError: invalid syntax
>>> print("Hi" name"!")
SyntaxError: invalid syntax
>>> print("Hi" name "!")
SyntaxError: invalid syntax
>>> print("hi "name"!")
SyntaxError: invalid syntax
>>> print("Hi ", name "!")
SyntaxError: invalid syntax
>>> print("Hi ",name,"!")
Hi  Emrich !
>>> print("Hi "+name+"!")
Hi Emrich!
>>> print("Your rectangle has area "+area)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print("Your rectangle has area "+area)
TypeError: must be str, not int
>>> print("Your rectangle has area ",area)
Your rectangle has area  50
>>> print("Your rectangle has perimeter ",perimeter)
Your rectangle has perimeter  45
>>> 
=========== RESTART: H:/App-SU/Python Programs/ProcessRectangle.py ===========
What is your name? Emrich
What is the rectangles length? 25
What is the rectangles width? 12
Hi Emrich!
Your rectangle has area  300
Your rectangle has perimeter  194
>>> 
=========== RESTART: H:/App-SU/Python Programs/ProcessRectangle.py ===========
What is your name? 
=============== RESTART: H:/App-SU/Python Programs/mileToKM.py ===============
Enter distance in miles: 10
10 miles equals 16.09 kilometers
>>> 
=============== RESTART: H:/App-SU/Python Programs/mileToKM.py ===============
Enter distance in miles: 20
20 miles equals 32.18 kilometers
>>> miles
20
>>> 
============== RESTART: H:/App-SU/Python Programs/mileToKMV2.py ==============
Enter distance in miles: 10
10 miles equals 16.09 kilometers
>>> main()
Enter distance in miles: 5
5 miles equals 8.045 kilometers
>>> 
============== RESTART: H:/App-SU/Python Programs/mileToKMV3.py ==============
Enter distance in miles: 10
10 miles equals 16.09 kilometers
Enter distance in miles: 5
5 miles equals 8.045 kilometers
Enter distance in miles: 1
1 miles equals 1.609 kilometers
Enter distance in miles: 3
3 miles equals 4.827 kilometers
>>> 
