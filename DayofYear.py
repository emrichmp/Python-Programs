# Emrich-Michael Perrier
# Emrich
# eperrier@syr.edu
# Assignment 3, problem 1
# 2/20/19
# Program determines what day of the year and day of the week a specific date is

def main():
    monthLengths=[31, 28, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday"]
    #prompt
    dateinput = input("Enter date as mm/dd/yyyy: ")
    #for loop to calc day of the year
    dn, mn=0,0
    for i in range(int(dateinput[0:2])):
        dn=monthLengths[i]+dn
        mn=monthLengths[i]
    doy=(dn-mn)+int(dateinput[3:5])
    print(dateinput, "is day ", doy ,"of the year.")
    #for loop to print weekday number list
    for i in range(1,8,1):
        print(i, "for", weekdays[i-1])
    #input for the day of jan first
    jan=input("What day of the week is January 1st? (Enter the number) ")
    #calculations
    weekremainder=int(doy%7)
    ydow=weekremainder+int(jan)-2
    yearweekday=weekdays[ydow]
    #Print day of week
    print(dateinput, "falls on a", yearweekday)
main()