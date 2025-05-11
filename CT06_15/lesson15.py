# print("Hello from lesson 14")

# counter = 0

# def increment_counter():
#     global counter
#     counter += 1

# for i in range (3):
#     increment_counter()

# print(counter)
import random

# def isEven(num):
#     return num % 2 == 0

# numbers = [1,2,4,3,6,8,9,]

# for number in numbers :
#     if isEven(number):
#         print(str(number) + " is even :D")
#     else :
#         print(str(number) + " is odd  :D")

def num():
    random.randint(1, 6)

def isEven(num):
    return num() % 2 == 0


for number in range (6) :
    if isEven(num()):
        print(str(number) + " is even :D")
    else :
        print(str(number) + " is odd  :D")