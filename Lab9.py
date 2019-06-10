#Lab 9.py
#Emrich-Michael Perrier
#Program computes average word length

def main():
    #infile=open("Seasons.txt","r")
    f = input("Enter input file name: ")
    infile=open(f)
    #of = input("Enter the output file name: ")
    #outfile=open(of,"w+")
    #Get phrase
    #p = input("Enter a phrase: ")
    for line in f:
        p = infile.readline()
        print(p)
    #Compute data with phrase
        w = p.split()
        wn = len(w)
        s = ""
        l = len(s.join(w))
        mean = round((l/wn),3)
        #print(mean)
        print(mean)
    infile.close()
    #outfile.close()
    #print the average
    #print("'", p,"'", "has an average word length of ", mean)
main()