# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ["abc", 1, "xyz", 2]
for person in people:  # do not use brackets in python syntax in for loop
    print(person)

# Break statement
for person in people:
    if(person is "xyz"):
        break
    print(person)

# Continue statement
for person in people:
    if(person is "xyz"):
        continue
    print(person)

# Range
for i in range(len(people)):
    print(people[i])

for i in range(0, 6):  # prints 0 to 5.
    print(i)

# While loops execute a set of statements as long as a condition is true.
c = 0
while c < 10:
    print(c)
    c += 1