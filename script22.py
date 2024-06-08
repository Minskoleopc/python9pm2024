# function

# program 

#int 
# int as param and inter as a return type
def add(x,y):
    return x + y
r = add(12,3)
print(r)


# float 
# float as a parameter and float as return type 
def add(x,y):
    return x + y
t = add(23.5,5.9)
print(t)

# string 
# string as parameter and string a return 
def greet(name):
    return "hello "+name
e  = greet("chinmay")
print(e)

#boolean 
#boolean as parameter and boolean as return type 
def canDrive(above18):
    if  above18:
        return True
    else:
        False
e = canDrive(True)
if(e):
    print("Allowed to drive ....!")
else:
    print("Not allowed to drive")
    

# list
#list as parameter and list as return type 
city = ["pune","mumbai","banglore","kolkata"]
def addCity(lst):
    lst.append("wardha")
    return lst
e = addCity(city)
print(e)
print(city)


# dict
# dict as parameter and dictionary as return type 

dict = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}

def addCityToInfo(info):
    info['city'] = "pune"
    return info
f = addCityToInfo(dict)
print(f)

# tuple as parameter and tuple as return type 
def addNum(tupA):
    tupA = list(tupA)
    tupA.append(555)
    tupA = tuple(tupA)
    return tupA
a,b,c = addNum((2,3))
print(a)
print(b)
print(canDrive)
# set as parameter and set as return type 

setA = {11,12,13}
def addToSetA(ss):
    ss.add(44)
    return ss
f = addToSetA(setA)
print(setA)













