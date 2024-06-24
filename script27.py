class Person:
    fn = "chinmay"
    ln = "deshpande"

    def displaName(self):
        print(self.fn + self.ln)

chinmay = Person()
amol = Person()

chinmay.displaName()
amol.displaName()
amol.fn = "amol"
amol.ln = "rao"
amol.displaName()

# program 2
# updating the value at the time of object create

class PersonB():
    def __init__(self,fn,ln):
        self.fn = fn 
        self.ln = ln

    def displayName(self):
        print(self.fn + self.ln)

amol = PersonB("amol","rao")
amol.displayName()
chinmay = PersonB("chinmay","deshpande")

chinmay.displayName()
amol.displayName()

# program 3
# getter and setter method
class PersonC:

    def setFn(self,fn):
        self.fn = fn 
    def getFn(self):
        return self.fn
    
    def setLn(self,ln):
        self.ln = ln

    def displayName(self):
        print(self.fn + self.ln)

kunal = PersonC()
kunal.setFn('kunal')
kunal.setLn('sharma')
kunal.displayName()

# program 4
class PersonD:
    # constructor
    country = "india"
    def __init__(self,fn,ln):
        self.fn = fn 
        self.ln = ln

    # class level method
    @classmethod
    def changeCountry(cls):
        cls.country = "bharat"
        
    # instance method
    def displayName(self):
        print(self.fn+self.ln)

amol = PersonD("amol","rao")
chinmay = PersonD("chinmay",'deshpande')
kajal = PersonD("chinmay",'deshpande')

print(amol.country)
print(chinmay.country)
amol.country = "bharat"
print(amol.country)
print(chinmay.country)
print(kajal.country)

PersonD.changeCountry()
print(amol.country)
print(chinmay.country)
print(kajal.country)







    






