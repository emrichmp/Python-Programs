#Emrich-Micahel Perrier
#Lab 16

from random import randrange

def roll():
    num = randrange(1,7)
    return num
    
def main():
    ones = 0
    twos = 0
    threes = 0
    for i in range (30):
        num1 = roll()
        print(num1, end=" ")
        if num1 == 1:
            ones += 1
        elif num1 == 2:
            twos += 1
        elif num1 == 3:
            threes += 1
    print()
    print("You have rolled", ones, "ones")
    print("You have rolled", twos, "twos")
    print("You have rolled", threes, "threes")

def main2():
    counter=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1000):
        red = roll()
        green = roll()
        r = red+green
        counter[r] += 1
    print(counter)
    for i in range(len(counter)):
        print(i, "\t",counter[i])
    
main2()