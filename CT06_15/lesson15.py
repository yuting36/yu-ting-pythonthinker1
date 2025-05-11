# print("Hello from lesson 14")

# counter = 0

# def increment_counter():
#     global counter
#     counter += 1

# for i in range (3):
#     increment_counter()

# print(counter)
import random

def isEven(num):
    return num % 2 == 0

def randNum():
     random.randint(1, 10)

numbers = [randNum,randNum,randNum,randNum,randNum,randNum,randNum]

for number in numbers :
    if isEven(number):
        print(str(number) + " is even :D")
    else :
        print(str(number) + " is odd  :D")