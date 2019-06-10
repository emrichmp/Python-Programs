# Emrich-Michael Perrier
# Emrich
# eperrier@syr.edu
# Assignment 5, Problem 1
# 2/28/19
# Program takes student names and student test data from infiles and prints them into a file that has name, test scores and averages

def main():
    #User inputs file names to read
    #StudentNames.txt
    NamesIn = input("What's the name of the student file? ")
    #StudentScores.txt
    ScoresIn = input("What's the name of the student score file? ")
    #Open Files
    names = open(NamesIn,"r")
    scores = open(ScoresIn,"r")
    students = names.readlines()
    testscores = scores.readlines()
    
    #seperate all the parts in the files
    s = len(students)
    
    for i in range(s):
        students[i] = students[i].rstrip("\n")
        testscores[i] = testscores[i].rstrip("\n")
        testscores[i] = testscores[i].split()
        print(students[i], testscores[i])

        
main()