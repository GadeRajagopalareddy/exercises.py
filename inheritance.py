class person:
    def __init__ (self,fname,lname):
     self.firstname=fname
     self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

x=person(input(),input())
x.printname()
y=person("cse","pfsd")
y.printname()