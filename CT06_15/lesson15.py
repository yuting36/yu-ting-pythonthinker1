# print("Hello from lesson 14")

# counter = 0

# def increment_counter():
#     global counter
#     counter += 1

# for i in range (3):
#     increment_counter()

# print(counter)

# def isEven(num):
#     return num % 2 == 0

# numbers = [1,2,4,3,6,8,9,]

# for number in numbers :
#     if isEven(number):
#         print(str(number) + " is even :D")
#     else :
#         print(str(number) + " is odd  :D")

import random 
def square(num):
    return num * num 

print(square(random.randint(1, 10)))

def sum_o_squares(num1,num2):
    return square(num1) + square(num2)

print(sum_o_squares)