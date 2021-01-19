# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1
name = "abc"
pie = 3.14
isEmployeed = True
print(x)

# Multiple assignment
x, name, pie, isEmployed = (2, "xyz", 3.13, False)
print(x, name, pie, isEmployed)

print(type(x))

# Casting..
x = str(x)
print(type(x))

y = int(pie)
print(type(y), y)

z = float(y)
print(type(z), z)  # 3.0 and not 3.13
