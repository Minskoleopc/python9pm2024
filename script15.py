# birthYear = [1999,2000,2001,2002]
# ages = [] # [25,24,23,22]

# for x in birthYear:
#     #print(2024 - x)
#     age = 2024 - x
#     ages.append(age)

# print(ages)

# program 2
marks = [66,77,88,33,44,55,55,66]
#[66,77,88,66]
above60= []

# program3
for x in marks:
    if x >= 60 and x % 2 == 0:
        above60.append(x)
print(above60)

# program 4
sum = [11,22,33]
total = 0
for x in sum:
    total = total + x
    #     =   0   + 11  #  11
    #     =   11  + 22  #  33
    #     =   33  + 33  #  66

print(total)


# program 5
cities = ["pune","nagpur","wardha"]
for x in cities:
    print("welcome "+x)









