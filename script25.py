# 8 am 
# 8:30 pm

# program 1 

birthYear = [1989,1990,1991,1992]
ages = []
for item in birthYear:
    ages.append(2024-item)
print(ages)

# program 2
e = [2024 - item for item in birthYear]
print(e)

# program3
f = list(map(lambda x :2024 - x,birthYear))
print(f)


# program 2
marks = [89,90,91,34,56]
above50 = []
for i in marks:
    if i > 50:
        above50.append(i)
print(above50)

g = [i for i in marks if i > 50]
print(g)

# filter
e = list(filter(lambda x : x > 50,marks))
print(e)

# program 3
lst = [1,2,3,4,5]
total = 0
for x in lst:
    total = total + x
print(total)

from functools import *
lst = [1,2,3,4,5]
h = reduce(lambda x,y:x+y,lst)
print(h)

lst2 = [11,22,33]
print(sum(lst2))
print(max(lst2))
print(min(lst2))


e = [total := total + x for x in lst]
print(e)







