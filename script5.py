# ternary operator
# program 1 
g = 10
t = 5

if g > t:
    print("g is greater")
else:
    print("t is greater")
print("g is greater") if g > t else print("t is greater")

# program 2
age = 16
f = "can drive" if age >= 17 else "cannot drive"
print(f)

# program 3
# loops

print(1)
print(2)
print(3)
print(4)
print(5)

# for with range()
# range(startIndex,EndIndex,StepSize)
# by default  startValue - 0
# endValue not included

# print 0 to 9
for x in range(10):
    print(x)

# print 1 to 9
for x in range(1,10):
    print(x)

# print 1 to 5
for x in range(1,6):
    print(x)

# print 1 to 10
for x in range(1,11):
    print(x)

# table of 2
for x in range(1,11):
    print(x * 2)

# table of 2
for x in range(2,21,2):
    print(x)

# table of 5 in reverse
for x in range(50,4,-5):
    print(x)

for x in range(30,2,-3):
    print(x)

# program 
# break statment and continue statment with for
# break immediately halt the loop

for a in range(1,11):
    if a == 5:
        break
    print(a)

for a in range(1,11):
    print(a) # 1 # 2 #3 #4 #5
    if a == 5:
        break
  
# 20 , 18 , 16, 14,12,10,8,6,4,2,0
for x in range(20,0,-2):
    print(x)

# 2,4,6,8,10,12,14,16,18
for x in range(2,21,2):
    print(x)

for a in range(5):
    if a == 3:
        continue
    print(a)






