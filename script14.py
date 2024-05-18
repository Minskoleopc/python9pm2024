

first_name = "chinmay"
q1 = first_name.upper()
print(q1)


last_name = "Deshpande"
q2 = last_name.lower()
print(q2)

last_name = "snehal"
q3 = last_name.capitalize()
print(q3)


# program 1

city = "PUNE"
q4 = city.isupper()
print(q4)

city2 = "Nagpur"
q5 = city2.islower()
print(q5)

info = "1232a43243244"
q6 = info.isdigit()
print(q6)

info = "abc"
q7 = info.isalpha()
print(q7)

info = "a"
q8  = info.isalnum() # 'a','12,'a234'
print(q8)

# program 3
city = "i am learning js"
q9 = city.replace("js","python")
print(q9)


info = ["chinmay","deshpande","7709192441"]
q10 = "@".join(info)
print(q10)

fruit = "apple"
q11 = fruit.endswith('le')
q12 = fruit.endswith('e')
q13 = fruit.startswith('a')
q14 = fruit.startswith('ap')
print(q11)
print(q12)
print(q13)
print(q14)

str = " goa "
print(len(str))

# q15 = str.lstrip()
# print(q15)
# print(len(q15))

# q16 = str.rstrip()
# print(q16)
# print(len(q16))

q17 = str.strip()
print(q17)
print(len(q17))

city = "wardha"
# 0  1  2  3  4   5
# w  a  r  d  h   a
q18 = city.index("d")
print(q18)

city3 = "chandrapur"

# 0  1  2   3  4  5  6  7  8  9
# c  h  a   n  d  r  a  p  u  r

#city3[:len(city3)]


first_name = "chinmay"

# 0  1  2  3  4  5  6
# c  h  i  n  m  a  y
#-7 -6 -5 -4 -3 -2 -1

#print(first_name[startIndex:Endindex(included):steps])
print(first_name[1::])
print(first_name[1:len(first_name):])
print(first_name[0:6:2])
print(first_name[1:-1:1])
print(first_name[-5:-1])
print(first_name[-1:-7:-2])
print(first_name[::-1])
