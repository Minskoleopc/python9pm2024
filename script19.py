names = ["chinmay","nirnay","poorva","sachin"]
print(names)
print(type(names))

cities  = ('pune',"nagpur")
print(type(cities))
cities = "mumbai",
print(type(cities))

# program 3
#cities[0] = "nagpur"
print(cities[0])
cities = ("nagpur","nanded",'wardha')
print(cities)

# program 4
cities = ("nagpur","nanded",'wardha')
for i in range(len(cities)):
    print(cities[i])
for i  in cities:
    print(i)

i1 = 0
while(i1 < len(cities)):
    print(i1)
    print(cities[i1])
    i1 = i1 + 1


# program 5
languages  = ("marathi","hindi","sankrit","telgu","punjabi","english")
a,b,c,e,d,f= languages
print(a)

# program 6
city  = ["pune","mumbai","bangalore"]
def addCity(lst):
    lst.append("wardha")
    return tuple(lst)

a,b,c,d = addCity(city)
print(a)

# program 7
k  = (11,22,33,11)
k  = list(k) # [11,22,33]
k.append(44)
k = tuple(k)
print(k)

e = k.count(11)
print(e)
f = k.index(22)
print(f)
