# class Person:
#     fn = "chinmay"
#     ln = "deshpande"

#     def display(self):
#         print(self.fn + self.ln)

# chinmay = Person()
# chinmay.display()
# amol = Person()
# amol.display()

# amol.fn = "amol"
# amol.ln = "rao"
# amol.display()

class Person:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName =  ln 

    def display(self):
        print(self.firstName + self.lastName)

ninad = Person("ninad","dani") 
print(ninad.fn)
print(ninad.ln)
ninad.display()

nirnay = Person("nirnay","deshmukh")
nirnay.display()

