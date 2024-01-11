anotherList = ["other item", "test"]
myList = ["apple", "banana", "orange", 2, 4, anotherList ]

myList.append("coconut")


print("actual List:", myList)

myList.pop() #LIFO principle as in stack it will remove the last element in the list

myList.pop(0) #it will remove the first element in the queue

print(myList)

print(len(myList))

element = myList[0]

print(element)

myList.insert(1, "shrimp")

print(myList)

myList.remove("shrimp")

print(myList)

myList.extend(["strawberry", "pear", "pineapple"])

print(myList)

newList = myList[1:4]

print(newList)

endOfList = len(myList)

endList = myList[0:endOfList]
print(endList)

