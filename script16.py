#           0         1       2   3
info = ["chinmay","deshpande",33,45]

# retrive 
print(info[0])
# update
info[0]= 'rahul'
# add 
info.append('pune')
# delete
info.pop()
info.pop(2)
info.remove("deshpande")
# available ?
print("chinmay" in info)

# dict 
# dictionary does not stores the value by index

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":33,
    "rollNo":45
}
#print(info[0])

# retrive 
e = info['firstName']
print(e)

# update 
info['firstName'] = "tanmay"
print(info)

# add
info['age'] = 34
print(info)
info['city'] = "pune"
print(info)

# delete prop
info.pop('age')
print(info)

# delete complete dictionary
#del info
#print(info)
# len
e = len(info)
print(e)
print("city2" in info)


vehicle = {
    "color":"red",
    "type":"sedane"
}

print(vehicle['color'])
# update
vehicle['color'] = "green"
print(vehicle)

#add
vehicle['regNo'] = 123
print(vehicle)

#{'color': 'green', 'type': 'sedane', 'regNo': 123}
vehicle.pop('type')
print(vehicle)

# property available or not
#{'color': 'green', 'regNo': 123}
print('Color' in vehicle)

# how many properties
print(len(vehicle))

del vehicle