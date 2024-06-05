#set 

# list stores duplicate values
names = ["chinmay","poorva","ram","sham","chinmay"]
print(names)

# set does not allow to store duplicate values
names = {"chinmay","poorva","ram","sham","ravi"}
print(names)


# program 2
# list stores the value by index 

names2 = ["ninad", "vijeet","sanket","ram"]
print(names2[2])
names2 = {"ninad", "vijeet","sanket","ram"}
#print(names2[2])

# program 3
for item in names2:
    print(item)

# program 4
print("ninad" in names2)

# collections  --> list , string , tuple , dictionary ,set

# s = "chinmay"
# t = ("ninad","sachin")
# l = ["poorva","sarika"]
# d = {
#     "firstName":"chinmay",
#     "lastName":"deshpande"
# }
# s2 = {"chinmay","snehal"}

# print(len(s))
# print(len(t))
# print(len(l))
# print(len(d))
# print(len(s2))

# listA = [11,22,33]
# print(max(listA))
# print(min(listA))

# del s
# del t
# del d
# del s2
# del l


# set 

number = {11,22,3,3,4,44,55}
number.add(666)
print(number)

# number.clear()
# print(number)

number.pop()
print(number)

number.remove(666)
print(number)

setA = {11,22,33}
# setB = setA
# setB.remove(22)

# print(setA)
# print(setB)
setB = setA.copy()
print(setB)
setB.remove(22)
print(setA)
print(setB)











