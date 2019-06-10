#squaresAndCubes.py
#Emrich-Michael Perrier
m, k = eval(input("Enter 2 positive integers, seperated by a comma"))
for i in range(m):
    print(i*i, end=" ")
print()
for j in range(k):
    print(j*j*j, end=" ")
    
