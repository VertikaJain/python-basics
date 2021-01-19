# A List is a collection which is ordered and changeable. Allows duplicate members.

nums = [1, 2, 3, 4, 5]
fruits = ["orange", "apple", "banana", "grapes"]
print(fruits[2])
print(len(fruits))
fruits.append("mango")
print(fruits)
print(len(fruits))
fruits.remove("grapes")  # give existing value only
print(fruits)
fruits.insert(3, "berries")
print(fruits)
fruits.pop(1)
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True) #descending
print(fruits)
fruits[1] = "blueberry" #Changeable
print(fruits)
