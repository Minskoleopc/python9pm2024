#            0        1         2     3
names = ["chinmay","poorva","sarika","ram"]
print(names)
print(type(names))

# retrive 
print(names[0])

# update
names[0] = "sham"
print(names)

# add
names.append("satish")
print(names)

#    0        1         2        3        4
# ['sham', 'poorva', 'sarika', 'ram', 'satish']
# delete
names.pop()
names.pop(2)


# program 4
cities = ["pune","delhi","bangalore","kolkata"]
print('pune' in cities)


#program 5
#            0          1          2        3     
country = ["india","bangalesh","srilanka","japan"]
for x in range(4):
    print(country[x])

for cntry in country:
    print(cntry)

i1 = 0
while i1 < len(country):
    print(country[i1])
    i1 = i1 + 1


# methods 
# append()
fruits = ["apple","mango","banana","grapes"]
fruits.append("papaya")
print(fruits)


# pop()
#['apple', 'mango', 'banana', 'grapes', 'papaya']#
fruits.pop()
fruits.pop(2)
print(fruits)

# remove()
veg = ["brinjal","cabbage","cauliflower","carrot"]
veg.remove("cabbage")
print(veg)

# append() , pop(),pop(2), remove()

#clear()
numbers = [11,22,33]
numbers.clear()
print(numbers)

numbers.insert(0,99)
numbers.insert(1,999)
numbers.insert(2,9999)
numbers.insert(3,99999)
numbers.insert(4,999999)
numbers.insert(2,1000)
print(numbers)

# extend()

a = [11,22,33]
b  = [44,55,66]
b.extend(a)
print(b)
print(a)