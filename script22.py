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

# lambda functions 

# def add(x,y):
#     return x + y
# add(12,4)


add = lambda a,b:a+b
e = add(1,4)
print(e)

sqr = lambda x : x *  x
r = sqr(4)
print(r)


# program 2
# function as parameter to another function

# add = lambda a,b:a+b
# def addition(fn,a,b):
#     # fn = lambda a,b:a+b
#     e = fn(a,b)
#     return e
# r = addition(add,12,4)
# print(r)

# # function as a parameter to another function
# def subtraction(fn,x,y):
#     # fn = lambda x,y:x-y
#     return fn(x,y)

# s = subtraction(lambda x,y:x-y,12,4)
# print(s)

# # function as a return type

# def greet():
#     return lambda :"hello"
# c = greet()
# print(c())


# program 3
#default
def add(x = 34,y=4):
    print(x+y)
add(12,16)

# positional arguments
def sub(x,y):
    return x-y
r = sub(y = 45,x = 90)
print(r)

#*args
def add(*agrs):
    print(agrs)
    total = 0
    for i in agrs:
        total = total + i
    return total
t = add(234,5,6,3,4,5,5,6,7,3,5,6,7,4,6,7,6,7,8)
print(t)

# **kwargs
def info(**kwargs):
    print(kwargs)
    kwargs['city']= "pune"
    return kwargs
r = info(name = "chinmay",age ="34",roll= 78)
print(r)
















