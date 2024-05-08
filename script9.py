
# methods 
names = ["sarika","poorva","ram","sham"]
print(names)
names2 = names
names2[0] = "abhisha"
print(names2)
print(names)

# program 2
cities = ["pune","mumbai","banglore","kolkata"]
citiesB = cities.copy()
citiesB[0] = "wardha"
print(cities)
print(citiesB)

# program3 

country = ["india","srilanka","china","cuba"]
country.pop()
country.pop(2)
country.remove("india")
print(country)
print(country)

# program 4
numbers = [11,22,33,44]
numbers.append(444)
print(numbers)

numbers.insert(2,9999)
print(numbers)

# program 5
# marks = [55,66,77,88,99]
# marks.clear()
# print(marks)

marks = [55,66,77,88,99]
marks.extend([88,99,55,66])
print(marks)


# program 5
#           0        1         2       3        4         5
fruits = ["apple","banana","grapes","papaya","apple" , "berry"]
y = fruits.count("apple")
print(y)
g = fruits.index("grapes")
print(g)


fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

