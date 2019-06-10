#SimplisticCardDealer.py
#Simulate dealing a hand of cards.  (May have repeats)
#Emrich-Micahel Perrier
#Lab 16

#import library so we can use randrange
from random import randrange
#Return a random rank for a card, that is
#returns a random character from "A23456789TJQK"
#Notice the use of T for ten
def chooseRank():
    ranks="A23456789TJQK"
    r = randrange(13)
    return ranks[r]

#Return a random suit for a card, that is
#return a random character from "CDHS"
def chooseSuit():
    suits="CDHS"
    s = randrange(4)
    return suits[s]
    

#Create a hand of 7 cards.
def main():
    #initialize hand as an empty list
    hand = []
    
    # repeat 7 times, once for each card
    for i in range(7):
        r = chooseRank()
        s = chooseSuit()

        #pick a random rank and suit
        

        #append a string with that rank and suit 
        #to the list hand
        hand.append(r+s)
 
    #print the hand
    print(hand)
    #sort the hand and print it again
    hand.sort()
    print(hand)
     
        
               
main()
