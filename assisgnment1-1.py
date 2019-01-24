#!/usr/local/bin/python3
import math
check = True
num = input("please enter a number")
while check:
    if not num.isalpha():
        #had to wrap this in a try/except because it was trying to convert strings to floats. 
        try:
            num = float(num)
            print("ceil: " , math.ceil(num))
            print("floor: " , math.floor(num))
            print("round: " , round(num))
            check = False
            break
        except ValueError:
            num = input("please enter a number")
    else:
        num = input("please enter a number")