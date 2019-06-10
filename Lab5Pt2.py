import math
oneDegreeInRadians = math.pi/180

print("Degrees","\tsin","\tcos")

for i in range (0,181,10):
    print(i,math.sin(i*oneDegreeInRadians),"\t",math.cos(i*oneDegreeInRadians))