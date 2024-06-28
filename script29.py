# class Student:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln 

#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Teacher:
#     def __init__(self,fn,ln,salary):
#         self.firstName = fn 
#         self.lastName = ln 
#         self.salary = salary
    
#     def displayName(self):
#         print(self.firstName + self.lastName)

#     def displaySalary(self):
#         print(self.salary)


# shirsh = Student("shirish","deshpande")
# print(shirsh.firstName)
# print(shirsh.lastName)
# shirsh.displayName()

################## INHERITANCE ##################################


# program 1 
# parent constructor and child no constructor 

class Student:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)


class Teacher(Student):
    salary = 10000
    def displaySalary(self):
        print(self.salary)

amol = Teacher("amol","rao")
print(amol.firstName)
print(amol.lastName)
print(amol.salary)

amol.displayName()
amol.displaySalary()


# program 2 # single inheritance 

class Student:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self, fn, ln,sl):
        super().__init__(fn,ln)
        self.salary = sl
    
    def displaySalary(self):
        print(self.salary)

chinmay  = Teacher("chinmay","deshpande",1000)

print(chinmay.firstName)
print(chinmay.lastName)
chinmay.displayName()
chinmay.displaySalary()
        
# program 3 #multi -level
class  GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self, fn, ln,ffn):
        super().__init__(fn, ln)
        self.fname = ffn

    def displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self, fn, ln, ffn,ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn
    def displaySName(self):
        print(self.sname + self.lastName)

chinmay = Son("manohar","deshpande","shirish","chinmay")
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.sname)

chinmay.displayFName()
chinmay.displayName()
chinmay.displaySName()

# program 4
# herarchial interitance
# multiple inheritance








