students = [
    {
        "firstName":'chinmay',
        "lastName":"deshpande",
        "age":30,
        "rollNo":45,
        "skills":["python","javascript","sql"]

    }
    ,
    {
        "firstName":'sarika',
        "lastName":"pansare",
        "age":25,
        "rollNo":44,
        "skills":["python","javascript","sql","mongoDb","html","css"]
    },
    {
        "firstName":'rohit',
        "lastName":"barve",
        "age":24,
        "rollNo":44,
        "skills":["sql","mongoDb","html","css"]
    }
]

#print(students[0]['firstName'] + students[0]['lastName'])

for student in students:
    print(student['firstName']+ student['lastName'])


# program 2 for e.g chinmay:3
for student in students:
    #print(student)
    print(student['firstName']+ ":" + str(len(student['skills'])))


# program 3
# average age of all students 
total = 0
for student in students:
    total = total + student['age']
print(total/len(students))

#program 4
# add react skills to every student
for student in students:
    student['skills'].append('reactjs')
print(students)

# program 5
# country:"India"
for student in students:
    student['country'] = "india"
print(students)


#program 6
# names above >= 25
for student in students:
    if(student['age'] >= 25):
        print(student['firstName'])