# program 1


# class Student:

#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def displayName(self):
#         print(self.firstName+self.lastName)


# class Teacher(Student):

#     def __init__(self, fn, ln,sl):
#         super().__init__(fn, ln)
#         self.salary = sl 
#     def displaySalary(self):
#         print(self.salary)


# amol = Teacher("amol","rao",1000)
# print(amol.firstName)
# print(amol.lastName)
# print(amol.salary)
# amol.displaySalary()
# amol.displayName()

# program 2

# class GrandFather:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def displayGName(self):
#         print(self.firstName+ self.lastName)


# class Father(GrandFather):

#     def __init__(self, fn, ln,ffn):
#         super().__init__(fn, ln)
#         self.fname = ffn

#     def displayFName(self):
#         print(self.fname + self.lastName)


# class Son(Father):
#     def __init__(self, fn, ln, ffn,ssn):
#         super().__init__(fn, ln, ffn)
#         self.sname  = ssn

#     def displaySName(self):
#         print(self.sname + self.lastName)
#         super().displayGName()
#         super().displayFName()

# chinmay = Son("chinmay","deshpande","akay","ram")
# print(chinmay.firstName)
# print(chinmay.lastName)
# print(chinmay.sname)
# print(chinmay.fname)

# # chinmay.displayGName()
# # chinmay.displayFName()
# chinmay.displaySName()


# program 3


class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)

class Son(Mother):
    def __init__(self, fn, ln,sn):
        super().__init__(fn, ln)
        self.sname = sn

    def displaySName(self):
        print(self.sname + self.lastName)

class Daughter(Mother):
    def __init__(self, fn, ln,dn):
        super().__init__(fn, ln)
        self.dname = dn

    def displayDName(self):
        print(self.dname + self.lastName)

son = Son("kanchan","deshpande","chinmay")
gauri = Daughter("kanchan","deshpande","gauri")

print(son.firstName)
print(son.lastName)
print(son.sname)

son.displaySName()
    

# program 4
# multiple inheritance

class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called")
        self.fname = fn 
        self.lname = ln

class Father:
    def __init__(self,fn,ln):
        print("father constructor called")
        self.fname = fn 
        self.lname = ln

class Son(Father,Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def Sname(self):
        print(self.sname + self.fname + self.lname)

chinmay = Son("chinmay","shirish","deshpande")
















