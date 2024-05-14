
# listA = ["chinmay","shirish","sarika"]
# print(listA)
# print(type(listA))

# # program 2

# first_name = "chinmay"
# print(first_name)
# print(type(first_name))

# # string stores the value by index
# print(first_name[0])

# # can we update list 
# # can we update char of string

# names = ["poorva","shraddha","minal",'raj',"sarika"]
# print(names)
# names[0] = "sameer"
# print(names)

# last_name = "deshpande"
# last_name[0] = "s"
# print(last_name)


# program 3

# fruits = "apple"

# # range()
# for x in range(len(fruits)):
#     #print(x)
#     print(fruits[x])

# # without range()

# for ch in fruits:
#     print(ch)


# # while
# i1 = 0 
# while(i1 < len(fruits)):
#     #print(i1)
#     print(fruits[i1])
#     i1 = i1 + 1


# # program 4
city = "pune"
# # enup
# rev = "" 
# for char in city:
#     rev =  char + rev
#             #p   + ""  ------> p
#             #u   + p   ------> up
#             #n   + up  -------> nup
#             #e   + nup -------> enup
# print(rev)


# program 4
city3 = "chandrapur"

#   0   1    2    3   4  5   6   7   8   9
#   c   h    a    n   d  r   a   p   u   r
#  -10  -9  -8   -7  -6 -5   -4 -3  -2  -1
#city3[startIndex:endIndex(not included):steps]

print(city3[1::])
print(city3[1:6:])
print(city3[:len(city3):])
print(city3[9:0:-1])
print(city3[::-1])
print(city3[0:10:3])
print(city3[9::-3])
print(city3[-10:8:1])
print(city3[-10:-2:1])
print(city3[2:-2:1])
print(city3[-2:2])


# string methods











