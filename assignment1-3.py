#!/usr/local/bin/python3
num1 = input("please enter the first number")
num2 = input("please enter the second number")
num1 = int(num1)
num2 = int(num2)
def addThem(x, y):
    print("add: ", x + y)
def subtractThem(x, y):
    print("subtract: ", x - y)
def multiplyThem(x,y):
    print("multiply: ", x * y)
def divideThem(x,y):
    print("divide: ", x / y)
addThem(num1, num2)
subtractThem(num1, num2)
multiplyThem(num1, num2)
divideThem(num1, num2)
