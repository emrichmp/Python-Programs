#ProcessTemps.py
#Compute the average temperature and the high temperature
#for a month  from data stored in a file.
#Record the answers on the console. 

def computeAvg():
        #open the input file
    infile=open("Jan05temps.txt","r")
    count = 0
    sum = 0
    temp = int(infile.readline())
    count=count+1
    sum=sum+temp
    
    for line in infile:
        temp=int(line)
        count=count+1
        sum=sum + temp
    infile.close()
    average=sum/count
    return average

def findHigh():
    infile=open("Jan05temps.txt","r")
    temp = int(infile.readline())
    high = temp
    
    for line in infile:
    
        temp=int(line)
        if temp>high:
            high = temp
    infile.close()
    return high

def findLow():
    infile=open("Jan05temps.txt","r")
    temp = int(infile.readline())
    low = temp
    
    for line in infile:
    
        temp=int(line)
        if temp<low:
            low = temp
    infile.close()
    return low
    
def printResults(average, high, low):
    print("Average temperature: {0:.2f}".format(average))
    print("High temperature:", high)
    print("Low temperature:", low)

def main():
    avg = computeAvg()
    high = findHigh()
    low = findLow()
    printResults(avg, high, low)
    
main()