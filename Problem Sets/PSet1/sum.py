# Let's test the summation in Python for lists of tuples (name, value)

# for _, value in [('Name1', 9), ('Name2', 8)]:
#     print(f"The value attributed for {_} in {value}")

# print(sum(value for name, value in [('Name1', 9), ('Name2', 8)]))

# # Another test for grades:
# list1 = [('Victor', 10), ('Hugo', 9), ('John', 7)]

# for _, grade in list1:
#     grades = sum(value for name, value in list1)
#     print(f"Student {_} has a grade {grade}")
#     print(f"The total grades for your class is {grades} points")

#     # Let's get the average of your class
#     print(f"The average grades for your class is {grades/len(list1)}")

# Student dictionary to transform into a list of tuples
students = {"Jesse": 6, "Walter": 10, "Gustavo": 6, "Hank": 7}

studentsList = list(students.items())

print(studentsList)

for _, grade in studentsList:
    print(grade)

for name, _ in studentsList:
    print(name)

grades = sum(grade for name, grade in studentsList)

print(f'Total grades is {grades}')