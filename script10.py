# # loop
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# # for and while 
# # break and continue
# #range(startIndex, endIndex (not included),steps )
# # by default start index is 0

# for x in range(5):
#     print(x)

# for x in range(1,11):
#     print(x)

# for x in range(3):
#     print("hello") # hello

# for x in range(1,11):
#     print(x*2)

# for x in range(2,21,2):
#     print(x)

# for x in range(5,0,-1):
#     print(x)

# for x in range(50,4,-5):
#     print(x)

# for x in range(5):
#     if x == 2:
#         break
#     print(x)

# for x in range(5,1,-1):
#     if x == 3:
#         break
#     print(x)

# for x in range(1,5):
#     if x == 3:
#         continue
#     print(x) #1 # 2 #4

# for x in range(10,5,-1):
#     if x == 6:
#         continue
#     print(x)

# program 2

i1 = 1
while(i1 <= 3):
    print("hello")
    i1 = i1 + 1


i2 = 1
while(i2 <= 5):
    print(i2) # 1 # 2 # 3 # 4 #5
    i2 = i2 + 1 # 2 # 3 # 4 # 5 #6

i3 = 2
while(i3 <= 20):
    print(i3)
    i3 = i3 + 2

i4 = 20
while(i4 >= 2):
    print(i4)
    i4 = i4 - 2

i5 = 50
while(i5 >= 5):
    print(i5)
    i5 = i5 - 5



# break and continue with while loop

i6 = 1

while(i6 <= 5):
    print(i6) # 1 # 2
    if i6 == 2:
        break
    i6 = i6 + 1 # 2


i6 = 1
while(i6 <= 5):
    if i6 == 2:
        break
    print(i6) #1
    i6 = i6 + 1 # 2

i7 = 5
while(i7 >= 1):
    print(i7) # 5 # 4 # 3  # 2
    if i7 == 2:
        break
    i7 = i7 - 1 # 4 # 3 # 2


i8 = 1
while(i8 <= 5):
    if i8 == 3: 
        i8 = i8 + 1 # 4
        continue
    print(i8) # 1 # 2 # 4 #5
    i8 = i8 + 1 # 2 # 3 # 5 # 6

