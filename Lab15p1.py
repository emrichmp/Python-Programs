#Lab 15 P1
#Emrich-Michael Perrier

def getCoefs():
    a, b, c = eval(input("Type the coefficient of the x-squared term, the x term, and the constant term in the format x, x, x: "))
    return a, b, c

def computeQuad(a,b,c,x):
    y = (a*x*x) + (b*x) + c
    return y

def main():
    a, b, c = getCoefs()
    for i in range(-10,11):
        x=i*0.1
        y=computeQuad(a,b,c,x)
        print("({0:.1f},{1:.1f})".format(x,y))
        
def main2():
    a, b, c = getCoefs()
    counter = -10
    while counter<11:
        x=counter*0.1
        y=computeQuad(a,b,c,x)
        print("({0:.1f},{1:.1f})".format(x,y))
        counter += 1
        
def main3():
    a, b, c = getCoefs()
    counter = -1
    while counter<1.0:
        x=counter
        y=computeQuad(a,b,c,x)
        print("({0:.1f},{1:.1f})".format(x,y))
        counter += 0.1
        
main3()