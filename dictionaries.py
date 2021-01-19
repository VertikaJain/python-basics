# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

employee = {
    "name": "abc",
    "age": 37
}

print(employee, type(employee))
print(employee["name"])  # abc
print(employee.get("age"))  # 37
print(employee.get("profile"))  # None

# add new key-value pair to dictionary
employee["phone"] = 123456789
print(employee)
print(employee.items())
print(employee.keys())
print(employee.values())
# copy dictionary
emp2 = employee.copy()
emp2["city"] = "delhi"
print(emp2)
print(employee)
# remove item
del employee["age"]
print(employee)
employee.pop("phone")
print(employee)

employee.clear()
print(employee)
print(len(employee))
print(len(emp2))

team = [
    {"name": "xyz", "age": 12},
    {"name": "pqr", "age": 21},
]
print(team[1]["name"])