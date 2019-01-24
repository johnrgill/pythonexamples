#!/usr/local/bin/python3
sum = 0
for i in range (0, 10):
    sum += i
    if (sum > 15):
        break

print(sum)

sum = 0
for i in range(0, 10):
    if (i > 7): continue
    sum += i

print(sum)

list2 = ["homer", "marge", "bart", "lisa", "maggie"]
for i in list2:
    print(i)


for i in range(0, len(list2)):
    print(list2[i])

sum = 0
while (sum < 100):
    sum += i
    i += 1
    print(sum)