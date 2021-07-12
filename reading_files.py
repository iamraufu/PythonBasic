employee_file = open("person.txt", "r")

# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readline())

# print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
