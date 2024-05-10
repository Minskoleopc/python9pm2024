
# string
# index starts from 0
# program 1
first_name = "snehal"
# 0  1  2  3  4 5
# s  n  e  h  a  l
print(first_name[0])
print(first_name[1])


# program 2
# loop using for - range

city = "pune"

# 0   1    2    3
# p   u    n    e
# range(startIndex , endIndex(not included), steps)
print(len(city))
for c in range(len(city)):
    #print(c)
    print(city[c])

#        012345
city2 = "nagpur"


# program 2
for x in range(len(city2)):
    #print(x)
    print(city2[x])

# for without using range

city3 = "wardha"
for c in city3:
    print(c)

# while loop
city4 = "chandrapur"
i = 0 
while(i < len(city4)):
    print(city4[i])
    i = i + 1

# loop
# program 4
city5 =  "mumbai"
for x in range(len(city5)):
    print(x)
    print(city5[x])

for x in city5:
    print(x)

x  = 1
while x < len(city5):
    print(x)
    print(city5[x])
    x = x + 1

city = "wardha"
print(city[0])
# 0   1   2  3  4  5
# w   a   r  d  h  a 

for x in range(len(city)):
    #print(x)
    print(city[x])


# program 5
city = "pune"
names = ["shraddha","amol","sarika"]
for x in range(len(city)):
    print(city[x])

for char in city:
    print(char)

for name in names:
    print(name)




i1 = 0
while(i1 < 4):
    #print(i1)  # 0 # 1 # 2 # 3
    print(city[i1])
    i1 = i1 + 1   # 1 # 2 # 3 # 4

# proram 6
# particular character or substring available or not 
fruits = "apple mango banana grapes chikoo"
print("k" in fruits)
print("mango" in fruits)
print("Mango" in fruits)

