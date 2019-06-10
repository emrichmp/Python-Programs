#Snowman.py
#Introduction to functions with no parameters
#and no return values

# What does this do?
def snowball():
    s='*'
    print("{0:>11}".format("****"))
    print("{0:>7}{0:>6}".format("**"))
    print("{0:>5}{0:>9}".format(s))
    print("{0:>4}{0:>11}".format(s))
    print("{0:>4}{0:>11}".format(s))
    print("{0:>5}{0:>9}".format(s))
    print("{0:>7}{0:>6}".format("**"))
    print("{0:>11}".format("****"))
    ## end snowball

def hat():
    s='#'
    print("{0:>10}".format("######"))
    print("{0:>4}{0:>7}".format(s))
    print("{0:>4}{0:>7}".format(s))
    print("{0:>4}{0:>7}".format(s))
    print("{0:>11}".format("##############"))

def main():
    hat()
    snowball()
    snowball()
    snowball()
    
    