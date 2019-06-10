# Emrich-Michael Perrier
# Emrich
# eperrier@syr.edu
# Assignment 2, problem 2.
# February 7, 2019
# Comparing stupid values that actually make no sense

def main():
    #collect data
    a = eval(input("Enter a value for a: "))
    print("x \t 1000+ax \t x^a \t a^x")
    #do calculations
    for x in range (0,31,5):
        #Print data
        print(x,"\t", 1000+a*x,"\t", x**a,"\t", a**x)
main()