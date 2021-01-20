# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# simple
def myFunc(name="jain"):
    print(f"hey {name}")

# myFunc()

# return values
def mySum(a, b):
    return a+b

sum = mySum(3, 4)
print(sum)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum=lambda a,b: a+b
print(getSum(1,2))