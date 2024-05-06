# program 1
#           0     1       2        3        4
names =  ["ram","sham","satish","poorva","shivani"]
print(names)
print(names[0])


# program 2
# value retrive 
print(names[2])
# value add 
names.append("amol")
print(names)

# value update 
names[0] = "abhisha"
print(names)

# ['abhisha', 'sham', 'satish', 'poorva', 'shivani', 'amol']
# value delete
names.pop() # last element
names.pop(3) # delete element at index 3

# # program 3

# fruits = ["apple","banana","grapes","papaya"]
# print(fruits[0])
# fruits[0] = "berry"
# fruits.append("chikoo")
# fruits.pop()
# fruits.pop(2)

# program 4
# any particular element available in list

vegetables = ["onion","potato","tomato","brinjal","carrot"]
# in 
print("Onion" in vegetables)

if("onion" in vegetables):
    print('vegetable is available')
else:
    print("vegetable not available")

# program 5
#        0       1        2         3
city = ["pune","mumbai","bangalore","wardha"]
# for - range
for x in range(4):
    #print(x)
    print(city[x])

# for without range 

for c in city:
    print(c)

#            0         1          2        3
country = ["india","pakistan","srilanka","japan"]
# range(start,end ,step)
# range(4) # by default - 0
for x in range(4):
    #print(x)
    print(country[x])

for cntry in country:
    print(cntry)


# while loop



