#Emrich-Michael Perrier
x = 200
y = 5
z = 32
w = 17

t = 8.1
u = 14.0
v = -36.9


# Enter 19
q=eval(input("Enter a whole number from 10 to 20: "))
# Enter 3 and 5
r,s = eval(input("Enter two numbers, separated by a comma:"))
quot=q//r
rem=q%r
divFl=r/s


result = z/y
result = w%y + z//y
result = 2**y
result = w + z*x - r
result = z * y - w // 8
result = y * 2 % 6

outcome = w % t * 10
outcome = t + 20 / 4
outcome = 10 * v-5
outcome = result + 5000

for k in range(2, 40, 10):
    print(k, end=" ")
    print("***", end=' ')
print()    
print("done skipping!")

a = 234 // 10
b = 234 % 10
c = 234 // 100
d = 234 % 100
e = 234 / 10 % 10

#Part II goes here.
#the code to read num
num = eval(input("Enter a three digit number "))
#the code to compute ones
ones = num % 10
#the code to compute tens
#tens = ((num % 100) - ones)/10
tens = (num % 100)//10
#The code to compute hundreds
huns = num // 100
#the code to print ones
print("The ones digit is: ",  ones)
#the code to print tens
print("The tens digit is: ",  tens)
#the code to print hundreds
print("The Hundreds digit is: ", huns)

#Enter a three digit number 938
#The ones digit is:  8
#The tens digit is:  3
#The Hundreds digit is:  9

#Enter a three digit number 258
#The ones digit is:  8
#The tens digit is:  5
#The Hundreds digit is:  2

#Enter a three digit number 158
#The ones digit is:  8
#The tens digit is:  5
#The Hundreds digit is:  1
