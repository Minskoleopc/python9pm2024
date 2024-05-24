info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":34
}

# retrive
print(info['firstName'])
# update
info['firstName'] = "tanmay"
# add
info['city'] = "pune"
# remove the lastName property
info.pop('lastName')
# remove the last ordered property od 
info.popitem()
# check whether the property exist on dictionary
print("rollNo" in info)

# program 2

vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}

#print(vehicle[0])
for key in vehicle:
    print(key,vehicle[key])


# program 3

vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}

for x in vehicle.keys():
    print(x)

for x in vehicle.values():
    print(x)

for k,v in vehicle.items():
    print(k,v)

# keys(), values() ,items()


# program 3

animal = {
    "name":"tiger",
    "legs":4,
    "color":"red"
}
print(animal['legs'])
x = animal.get('legs')
print(x)

animal.pop('color')
print(animal)

animal.clear()
print(animal)

# program 6
dictOne = {"1":"one","2":"two"}
dictTwo = {"3":"three","4":"four"}

dictOne.update(dictTwo)
print(dictOne)

# program 7 

info2 = {
    "firstName":"amol",
    "lastName":"rao",
    "age":33,
    "city":"nagpur"
}

info2.setdefault("city","pune")
print(info2)

# program 8
q = dict.fromkeys(["one","two","three"])
print(q)

# monday 9pm







