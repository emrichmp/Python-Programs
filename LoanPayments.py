# Emrich-Michael Perrier
# Emrich
# eperrier@syr.edu
# Assignment 3 problem 2
# 2/19/19
# Program prints out a chart that shows all details of loan payments, interest, and balance as the payments are made

def main():
    #Get information for loan details
    p = eval(input("Principal: "))
    ai = eval(input("Annual interest rate: "))
    
    #convert from percent to float
    mai = ai/100
    m = eval(input("How many months is the loan? "))
    
    #formula to compute monthly payment
    payment = ((mai/12)*p)/((1-(1+(mai/12))**-m))
    
    #Print loan details
    print("{:.2f}".format(payment))
    print("Principal", "{:20.2f}".format(p), "{:>27}".format("Monthly payment"), "{:20.2f}".format(payment))
    print("Annual Interest", "{:11.2f}".format(float(ai)),"%", "{:>17}".format("Term"), "{:23}".format(m), " months")
    print()
    print("Payment", "{: >20}".format("interest"), "{: >30}".format("Pay to principal"), "{:>20}".format("Balance"))
    #for loop to print payments and details on each payment
    b = p
    for i in range(1,m+1,1):
        interest = (mai/12)*b
        ptp = payment-interest
        b = b-payment
        print(i, "{: >26.2f}".format(interest), "{:>20.2f}".format(ptp), "{:>30.2f}".format(b))  
    print("Due: $", "{:.2f}".format(b))
main()