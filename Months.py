#Emrich-Michael Perrier
#Months
def main():
    longMonth=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    dayMonth=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num=eval(input("Enter Number of Month: "))
    month=longMonth[num-1]
    days=dayMonth[num-1]
    print(month, "has ",days, "days")
main()