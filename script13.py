firstName = "chinmay"
lastName  = 'deshpande'
info = """
    my name is chinmay and i am learning js
"""
info = '''
    My name is chinmay and learning python
'''

# program 2
# string stores the value by index


city = "pune"
# 0   1  2   3
# p   u  n   e
print(city[0])

# update
#city[1] = "c"
# string does not support item assignment
# check for sub-string or particular char
# 0 1 2 3 4
# a p p l e

# fruit = "apple"
# print("a" in fruit)
# print("A" in fruit)

# # range()
# for i in range(5):
#     #print(i)
#     print(fruit[i])

# # without range()
# for i in fruit:
#     print(i)

# # while
# i2 = 0
# while(i2 < len(fruit)):
#     #print(i2)
#     print(fruit[i2])
#     i2 = i2 + 1


# len()
country = "india"
e = len(country)
print(e)

# upper()
fruit = 'apple'
q1 = fruit.upper()
print(q1)
# lower()

veg = "Brinjal"
q2 = veg.lower()
print(q2)

# capitalize()
first_name = "chinmay"
q3 = first_name.capitalize()
print(q3)

# startswith()
# boolean --- True or False

last_name  = "Deshpande"
q4 = last_name.startswith("D")
q5 = last_name.startswith("de")
print(q4)
print(q5)

# endswith()
# boolean --- True or False
city = "nagpur"
q6 = city.endswith('r')
q7 = city.endswith('Pur')
print(q6)
print(q7)

# replace()
info = "i am learning js"
q8 = info.replace("js","python")
print(q8)


# join()
info = ["chinmay","deshpande","7709192441"]
q9 = '@'.join(info) # "chinmay@deshpande@7709192441"
print(q9)

# split()














