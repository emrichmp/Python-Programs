#Emrich-Michael Perrier
#LAB 10
#The Elf File

#Makes 5x5 E
def E():
    print("*****")
    print("*")
    print("****")
    print("*")
    print("******")

#Makes 5x5 F
def F():
    print("-----")
    print("|")
    print("|--")
    print("|")
    print("|")
    
#Makes 5x5 H    
def H():
    print("*   *")
    print("*   *")
    print("*****")
    print("*   *")
    print("*   *")
    
#Makes 5x5 I
def I():
    print("-----")
    print("  |  ")
    print("  |  ")
    print("  |  ")
    print("-----")

#Makes 5x5 L
def L():
    print("|    ")
    print("|    ")
    print("|    ")
    print("|    ")
    print("-----")

#Makes 5x5 T
def T():
    print("-----")
    print("  |  ")
    print("  |  ")
    print("  |  ")
    print("  |  ")

#Main calls all the functions in the order to write "THE ELF FILE" going down
def main():
    T()
    H()
    E()
    print()
    E()
    L()
    F()
    print()
    F()
    I()
    L()
    E()

main()