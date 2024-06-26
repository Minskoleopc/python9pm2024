# program 1

# ousite the class 
# using constructor 
# using get and set method

 
# instance method  class level method   static method
# class Person:
#     # class level variable
#     country = "india"

#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln 

#     # instance method 
#     def addCity(self,cty):
#         self.city = cty
    
#     #instance method 2
#     def updateLastName(self,ln):
#         self.lastName = ln

#     @classmethod
#     def updateCountry(cls,updateCountry):
#         cls.country = updateCountry


# amol = Person("amol","rao")
# chinmay = Person("chinmay","deshpande")
# print(amol.firstName)
# print(amol.lastName)
# print(amol.country)

# amol.country = "bharat"
# print(amol.country)

# Person.updateCountry("bharat")
# print(chinmay.country)


# program 2
# Total number of objects 

class Emp:
    Count = 0
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
        Emp.Count = Emp.Count + 1
        
    @staticmethod
    def  countObj():
        return Emp.Count
    
emp1 = Emp("amol","rao")
emp2 = Emp("chinmay","deshpande")
emp3 = Emp("sarika","pansare")
e = Emp.countObj()
print(e)







