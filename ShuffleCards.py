#Emrich-Michael Perrier
#Emrich
#eperrier@syr.edu
#Assignment 8 part 2
#April 4 2019
#Shuffling 'cards' and printing them

from random import randrange

def MakeDeck():
    #Creates a list of cards to make the deck using for loop and chr
    deck = []
    for i in range(65,80):
        deck.append(chr(i))
    return deck
    
    
def Shuffle(deck, show):
    #If case is true it will print all the 'mini-shuffles' and then the output
    if show == True:
        for i in range(15):
            r = randrange(i,15)
            deck[i],deck[r] = deck[r],deck[i]
            print(deck)
    #If case is not true it will print the original deck (A-O) and then the shuffle
    else:
        for i in range(15):
            r = randrange(i,15)
            deck[i],deck[r] = deck[r],deck[i]
        print(deck)
    
#Calls True
def main1():
    d = MakeDeck()
    print(d)
    Shuffle(d, True)
#Calls False    
def main2():
    print()
    d = MakeDeck()
    print(d)
    Shuffle(d, False)
    
main1()
main2() 
