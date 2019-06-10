# lab17.py
#
#  This file contains the definition of a new class (Employee),
#     plus a few instances of that class.

################################################################
class Employee:
    
    # if not specified, an employee is considered non-exempt
    def __init__ (self,name,pay,exempt=False):
        self.name = name
        self.payrate = pay
        self.exempt = exempt
 
 
    def display (self):
        if self.exempt:
            status = "Exempt"
        else:
            status = "Non-exempt"
        print ("{0}: {1}, paid ${2:.2f} per hour".format(self.name,
                                                        status,
                                                        self.payrate))
    def payraise(amt):
        m = amt
        self.payrate = self.payrate + m

        
##  here ends the definition of the Employee class
################################################################
    
# some sample instances of Employee, for testing purposes
#
#   Because of indentation, we can see that these are *not*
#      part of the class definition.  They are globally scoped,
#      which means you can access them in the shell.

zeke = Employee ("Ezekial Frekial",20.00,False)
yancey = Employee ("Yanciford Royale",20.00,True)
joule = Employee ("Joule Zooms", 17.00)
    