#Emrich-Michael Perrier
#Lab 23 Recursion

def power(a,n):
    if n == 1:
        return a
    else:
        ans = a*power(a,n-1)                                                
    return ans

def sumIterative(n):
    sum=0
    for i in range(n+1):
        sum = sum+i
    return sum

def sumRecursive(n):
    if n == 1:
        ans = n
    else:
        ans = n + sumRecursive(n-1)
    return ans

def square(n):
    if n ==1:
        ans = n
    else:
        ans = n+sumRecursive(n-1)
    return ans

def main():
    a=(eval(input("a: ")))
    n=(eval(input("n: ")))
    ans = power(a,n)
    print(ans)
    for i in range(21,30):
        i = i /10
        ans = power(i,5)
        print(ans)
    s = sumIterative(n)
    print(s)
    s2 = sumRecursive(n)
    print(s2)
    sqr = square(5)
    print(sqr)
    
main()