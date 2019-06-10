def lines():
    print("-----")

def leftW(turn):
    if turn == 1:
        color = "W"
    elif turn == -1:
        color = "B"
    print("{0}----".format(color))
    
def rightW(turn):
    if turn == 1:
        color = "W"
    elif turn == -1:
        color = "B"
    print("----{0}".format(color))

def middle():
    print("|   |")
    print("|   |")

def box(player, corner):
    if corner == 'A':
        #1st box
        leftW(player)
        middle()
        lines()
    elif corner == 'B':
        #2nd box
        rightW(player)
        middle()
        lines()
    elif corner == 'C':
        #3rd box
        lines()
        middle()
        leftW(player)
    elif corner == 'D':
        #4th box
        lines()
        middle()
        rightW(player)

def main():
    #box(1,'D')
    #box(-1, 'C')
    box(1,'A')
    box(1,'B')
    box(1,'C')
    box(1,'D')
    box(-1,'A')
    box(-1,'B')
    box(-1,'C')
    box(-1,'D')
main()