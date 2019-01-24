#!/usr/local/bin/python3
#lists are arrays lol
#tuples are weird arrays

list1 = ["cat", "dog", "panda", "will smiff"]
print(list1)
list1[1] = "Barry"
print(list1)

list2 = ["frodo", "sam", "gimli", "legolas", "aragorn", "pip", "merry", "boromir"]
list2.append("gandalf")
list2.append("wendell")
print(list2)
list2.remove("wendell")
print(list2)
list2.sort()
print(list2)
list2.reverse()
print(list2)


myTuple = ("hello", "goodbye", -1, -2, 44.44)
myTuple2 = ("olleh", "eybdoog", 1, 2, .4444)
myTuple3 = (myTuple, myTuple2)
print(myTuple3)
print(myTuple3[0][0][0])
