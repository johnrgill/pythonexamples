#!/usr/local/bin/python3
myString = 'test'
myString2 = 'test'

#print("My string is %s" % myString2)

#print(myString2.capitalize())
#print(myString2.upper())
#print(myString2.lower())

myString3 = "   Hello!   "
print(myString3.strip())
print(myString3.isalpha())
#isalpha() tells you if ALL CHARS are alpha
print(myString3.isnumeric())
#isnumeric() tells you if ALL CHARS are numbers (takes string as input)

myString4 = "hello. I must be going!"
print(myString4[14:16])
print(myString4.find("be"))
print(myString4.replace("!", " to school"))



s1 = "cat"
s2 = "dog"
s3 = s1.join(s2)
print(s3)
s4 = s1 + s2
print(s4)

myInput = "cat, dog, fish, panda, bieber"
print(myInput.split(', '))
