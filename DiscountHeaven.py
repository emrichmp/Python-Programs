# Emrich-Michael Perrier
# Emrich
# eperrier@syr.edu
# Assignment 2, problem 1.
# February 7, 2019
# Discount heaven thing

def main():
    #Get the data
    print("Discount Heaven, where the prices will make you smile!")
    print("For each item, enter the number, then press enter.")
    t = eval(input("Tire: "))
    s = eval(input("soup bowls: "))
    h = eval(input("hats: "))
    sb = eval(input("Skate boards: "))
    p = eval(input("Pillows: "))
    #do computations
    ti = t//4
    tm = t%4
    ti = ti * 420.00
    tm = tm * 139.99
    tt = ti + tm
    si = s//6
    sm = s%6
    si = si * 10.00
    sm = sm * 1.88
    st = si + sm
    hi = h//2
    hm = h%2
    hi = hi * 10.50
    hm = hm * 7.00
    ht = hi + hm
    sbi = sb//3
    sbm = sb%3
    sbi = sbi * 120.00
    sbm = sbm * 49.99
    sbt = sbi + sbm
    pi = p//4
    pm = p%4
    pi = pi * 80.00
    pm = pm * 21.00
    pt = pi+pm
    mt = tt+st+ht+sbt+pt
    it = t+s+h+sb+p
    #print output
    print("tires \t $", tt,"\t", t)
    print("soup bowls \t $", st,"\t", s)
    print("hats \t $", ht,"\t", h)
    print("skateboards \t $", sbt,"\t", sb)
    print("pillows \t $", pt,"\t", p)
    print("-------------------------------------------")
    print("total \t $", mt,"\t", it)
    print("Come Again!")
main()