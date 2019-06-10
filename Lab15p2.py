#Lab 15 P2
#Emrich-Michael Perrier

def getRecipe1():
    moredata = "yes"
    total = 0
    ingredientNum = 0
    while moredata == "yes":
        input("Name of ingredient: ")
        weight = eval(input("Weight of ingredient in grams: "))
        total = total + weight
        ingredientNum += 1
        moredata = input("Are there more ingredients: ")
        if moredata == "no":
            return total, ingredientNum
        
def getRecipe2():
    moredata = ""
    total = 0
    ingredientNum = 0
    print("write 'no' when there are no more ingredients to input")
    while moredata == "":
        input("Name of ingredient: ")
        weight = eval(input("Weight of ingredient in grams: "))
        total = total + weight
        ingredientNum += 1
        moredata = input("")
        if moredata == "no":
            return total, ingredientNum
        
def main():
    total, i = getRecipe2()
    print("Total grams of ingredients:", total)
    print("Total number of ingredients:", i)
    
main()