# If/ Else conditions are used to decide to do something based on something being true or false
x = 5
y = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
if(x > y):
    print(f"{x} is > {y}")
elif(x == y):
    print(f"{x} is = {y}")
else:
    print(f"{x} is < {y}")

# Logical operators (and, or, not) - Used to combine conditional statements
if(x > 2 and x <= 10):
    print(f"{x}>2 and {x}<10")
if(x > 2 or x < 10):
    print(f"{x}>2 or {x}<10")
if not(x==y):
    print(f"{x} = {y}")

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
a=[1,2,3,4,5]
print(x in a)
print(x not in a)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
print(x is y)
print(x is not y)