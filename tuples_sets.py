# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

fruits = ("apple", "orange", "banana", "grape")
fruits1 = ("apple")  # string
fruits2 = ("apple",)  # tuple
print(type(fruits),  type(fruits1), type(fruits2))
print(fruits, fruits1, fruits2)
# fruits[1]="berries" -> error: unchangeable
del fruits2
# print(fruits2) #will result in an error
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.
fruits_set = {"apple", "orange", "banana", "grapes"}

print("apple" in fruits) 
print("apple" in fruits_set) 
fruits_set.add("strawberry")
fruits_set.remove("banana")
print(fruits_set)
fruits_set.add("orange") #no error on adding duplicate value, it just does not add it.
print(fruits_set)

fruits_set.clear()
print(fruits_set) #empty set
del fruits_set
# print(fruits_set) #undefined error
