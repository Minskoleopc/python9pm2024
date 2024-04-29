# program 1

# one input and multiple outcome
# numT > 0 and numT <= 5   -------> 10 % discount
# numT > 5 and numT <= 10  -------> 20 % discount
# numT > 10                -------> 30 % discount


# if condition:
#     statement

# program  1

numT = 19
if numT > 0 and numT <= 5:
    print("10 % discount") 
if numT > 5 and numT <= 10:
    print("20 % discount")
if numT > 10:
    print("30 % discount")

# program 2

numT2 = -10
if numT2 > 0 and numT2 <= 5:
    print("5 % discount")
elif numT2 > 5 and numT2 <= 10:
    print("10 % discount")
elif numT2 >10:
    print("20 % discount")
else:
    print("incorrect input no discount")

# program 3
marks = 92
if marks > 90:
    print("Grade A")
if marks >= 75:
    print("Grade B")
if marks >= 65:
    print("Grade C")

# program 4
marks = 50
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 65:
    print("Grade C")
else:
    print("please try again....")

# program 5

a = 10
b = 5
if a > b:
    print("a is greater")
else:
    print('b is greater')

# program 6

a1 = 10
a2 = 5 
a3 = 2

if a1 > a2 and a1 > a3:
    print("a1 is greater")
elif a2 > a1 and a2 > a3:
    print("a2 is greater")
else:
    print("a3 is greater")

# program 7

a11 = 10
a22 = 5

if a11 > a22:
    print("a11 is greater")
else:
    print("a22 is greater")

print("a11 is greater") if a11 > a22 else print("a22 is greater")

















