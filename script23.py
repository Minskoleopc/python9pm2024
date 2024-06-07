# program 1
# setA = {11,22,33}
# setA.add(44)
# print(setA)


# #setA.clear()
# setB = setA.copy()
# setB.add(33)
# print(setB)

# setA = {11,22,33,44}
# setA.pop()
# setA.remove(44)


# program 1  
# setA = {11,22,33}
# setB = {44,55,66}
# setC = setA.union(setB)
# print(setC)

# setN = {11,22,33}
# setM = {22,55,66}
# setP  = setN.intersection(setM)
# print(setP)


# setB1 = {66,77,88}
# setB2 = {55,68,77}

# setB3 = setB1.difference(setB2)
# setB4 = setB2.difference(setB1)

# print(setB3)
# print(setB4)

# print(setB2)
# print(setB1)

# setB1.difference_update(setB2)
# print(setB1)


# setB1 = {66,77,88}
# setB2 = {55,68,77}

# setB1.intersection(setB2)
# setB1.intersection_update(setB2)
# print(setB1)



# setB1 = {66,77,88}
# setB2 = {55,68,77}

# # setB3 = setB1.symmetric_difference(setB2)
# # print(setB3)

# setB1.symmetric_difference_update(setB2)
# print(setB1)

setA = {11,22,33}
setB = {11,22}

e = setB.issubset(setA)
f = setA.issuperset(setB)
print(e)
print(f)

setN = {11,22,33,44}
setM = {11,223,335,446}  
g = setM.isdisjoint(setN)
print(g)




