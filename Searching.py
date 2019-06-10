#Emrich-Michael Perrier
#Searching.py

def binarySearch():
    infile=open("bigList.txt","r").read()
    bigList=[]
    infile=infile.split()
    for line in infile:
        line = int(line)
        bigList.append(line)
    lowIndex = 0
    highIndex=len(bigList)-1
    found=False
    While lowIndex<=highIndex and found == False:
        key=69
        midIndex=(lowIndex+highIndex)//2
        if bigList[midIndex] == key:
            found=True
        elif bigList[midIndex] > key:
            highIndex=midIndex-1
        elif bigList[midIndex] < key:
            lowIndex=midIndex+1
        if found:
            return bigList, midIndex, key
        else:
            return bigList, -1, key
def main():
    bigList, ans, key=binarySearch()
    print("The key is", key,"it's index is: ", ans)

main()