#Recursor.py
#Computing factorial
#   Draw memory

#compute n! recursively
def factorial( n ):
    if n==1:
        ans = 1
    else:
        ans = n * factorial (n-1)
    return ans

def main():
    k = int(input("Enter k for k! "))
    kfac = factorial (k)
    print(k, '\t', kfac)
main()