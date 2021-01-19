# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = "abc"
age = 37
# Concatination
# print("my name is "+name + " of " + age + " years ") #TypeError: can only concatenate str (not "int") to str
# print("my name is "+name + " of " + str(age) + " years ")

# String Formatting
# 1. arguements by position
# print("hey, my name is {name} of {age} years".format(name=name, age=age))

# 2. F-strings
# print(f"hey there, my name is {name} of {age} years.")

# String Methods
s = "fake world"
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print(s.replace("world", "geek"))
print(s.count('k'))
print(s.startswith("fa"))
print(s.startswith("qwe"))
print(s.endswith("qwe"))
print(s.split())
print(s.find('r'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())
