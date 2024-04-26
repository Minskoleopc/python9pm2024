# conditional statments 


# one input and multiple outcome

# numT > 0  and  numT <= 5   ----- 10 % discount
# numT > 5   and numT <= 10  ----- 20 % discount
# numT > 10                  ----- 30 % discount

# numT = 17
# if numT > 0 and numT <=5 :
#     print("10 % discount")
# if numT > 5 and numT <=10:
#     print("20% discout")
# if numT > 10:
#     print("30 % discount")

# program 2
numT = -17
if numT > 0 and numT <=5 :
    print("10 % discount")
elif numT > 5 and numT <=10:
    print("20% discout")
elif numT > 10:
    print("30 % discount")
else:
    print('please provide correct input')

# program 3
marks = 33

# if marks > 90:
#     print("Grade A")
# if marks >= 75:
#     print("Grade B")
# if marks >= 65:
#     print("Grade C")
if marks > 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 65:
    print("Grade C")
else:
    print("incorrect input")

# program 4
a = 10 
b  = 15
if a > b:
    print("a is greater")
else:
    print("b is greater")

#program 5

a = 10
b = 50
c = 400

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")








