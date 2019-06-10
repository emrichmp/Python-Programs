# Scoper.py
# Baruch
# Observing global and local scope.



def first():
    print("in first a=",a)
    
def second():
    a=22
    print("in second a=", a)
    
def third():
    a=a+1
    print("in third a=", a)
    
a=1
print("global: a=",a)
first()
print("global: a=",a)
second()
print("global: a=",a)
third()