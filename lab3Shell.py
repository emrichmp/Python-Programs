Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # lab3StepThru.py
# You be the computer.
# Record the output on the next page.
# Tear out this page.
# What is the output?
def main():
     x=3+4*5
     print("x=",x)
     x=x+1
     print("x=",x)
     state1="New"
     state2="York"
     print(state1,state2)
     print(state1+state2)
     print()
     for i in range(3):
         print("Ha")

     # Enter 19
     q=eval(input("Enter a whole number from 10 to 20: "))
     q
     # Enter 17
     r=input("Enter another whole number: ")
     r
     print(q, r)
     name = input("Enter your family name: ")
     print("Your nmame is "+name+"!!")

main() 

SyntaxError: invalid syntax
>>> 
============= RESTART: H:/App-SU/Python Programs/lab3StepThru.py =============
x= 23
x= 24
New York
NewYork

Ha
Ha
Ha
Enter a whole number from 10 to 20: 19
Enter another whole number: 17
19 17
Enter your family name: emrich
Your nmame is emrich!!
>>> length
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    length
NameError: name 'length' is not defined
>>> for i in range(4):
	print(i)

	
0
1
2
3
>>> for i in range(4):
	print(i, end=" ")

	
0 1 2 3 
>>> for i in range(4):
	print(i, end+"grams")

	
Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    print(i, end+"grams")
NameError: name 'end' is not defined
>>> for i in range(4):
	print(i, end+\"grams")
	      
SyntaxError: unexpected character after line continuation character
>>> for i in range(4):
	print(i, end="grams")

	
0grams1grams2grams3grams
>>> for i in range(5):
	print(i, end=" ")

	
0 1 2 3 4 
>>> for i in range(10):
	print(i, end=" ")

	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(0):
	print(i, end=" ")

	
>>> for i in range(-2):
	print(i, end=" ")

	
>>> list(range(4))
[0, 1, 2, 3]
>>> list(range(1))
[0]
>>> list(range(0))
[]
>>> for i in range(5):
	print(i, end=" ")

	
0 1 2 3 4 
>>> for i in range[2, 4, 6, 23]:
	print(i, end=" ")

	
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    for i in range[2, 4, 6, 23]:
TypeError: 'type' object is not subscriptable
>>> for i in[2, 4, 6, 23]:
	print(i, end=" ")

	
2 4 6 23 
>>> for i in range(5):
	print(2*i, end=" ")

	
0 2 4 6 8 
>>> for i in range(6):
	print(2*i, end=" ")

	
0 2 4 6 8 10 
>>> for i in range[100, 110]:
	print(2*i, end=" ")

	
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for i in range[100, 110]:
TypeError: 'type' object is not subscriptable
>>> for i in range [100, 102, 104, 106, 108, 110]
SyntaxError: invalid syntax
>>> for i in range [100, 102, 104, 106, 108, 110]:
	print(i, end=" "0
	      
SyntaxError: invalid syntax
>>> for i in range [100, 102, 104, 106, 108, 110]:
	print(i, end=" ")

	
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    for i in range [100, 102, 104, 106, 108, 110]:
TypeError: 'type' object is not subscriptable
>>> for i in [100, 102, 104, 106, 108, 110]:
	print(i, end=" ")

	
100 102 104 106 108 110 
>>> for i in range(6):
	print(99+i, end=" ")

	
99 100 101 102 103 104 
>>> for i in range(6):
	print(2*i+100\, end=" ")
	
SyntaxError: unexpected character after line continuation character
>>> for i in range(6):
	print(2*i+100, end=" ")

	
100 102 104 106 108 110 
>>> for i in range(6):
	print(2*i+1, end=" ")

	
1 3 5 7 9 11 
>>> x=eval(input("Give me X"))
Give me X5
>>> x=eval(input("Give me X "))
Give me X 5
>>> for i in range (x-1)
SyntaxError: invalid syntax
>>> x=eval(input("Give me X "))
Give me X 5
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> x=eval(input("Give me X "))
Give me X 5
>>> for i in range (x):
	print(i, end=" ")

	
0 1 2 3 4 
>>> 
x, y = 3, 4
>>> x
3
>>> y
4
>>> x, y, e, z = 1, 2, 3, 4
>>> 
>>> x
1
>>> y
2
>>> e
3
>>> z
4
>>> len, wid = eval(input("Enter length and width, seperated by a comma"))
Enter length and width, seperated by a comma 5, 7
>>> len
5
>>> wid
7
>>> 
