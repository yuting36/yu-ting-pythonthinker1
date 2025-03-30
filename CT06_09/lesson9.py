# print("Hello from lesson 9")

import random

# num1 = random.randint(1, 6)
# num2 = random.randint(1, 6)
# num3 = random.randint(1, 6)

# print("number one is : " + str(num1 ))
# print("number two is : " + str(num2 ))
# print("number three is : " + str(num3))


# Even_odd = num1 % 2 == num2 % 2 == num3 % 2 == 0
# print (Even_odd)

# days = int(input("how many days have you borrowed the book? "))
# if days >= 25 :
#     print("return the book")

# RandNum = random.randint(0 , 10)

# guess = int(input("what is the number? "))
# if guess == RandNum :
#     print ("congratulations you got it correct!")
# else : print ("awh wrong answer, the anser was : " + str(RandNum))

# price_apples = 0.60
# price_oranges = 0.90

# num_apples = int(input("how many apples do you want? "))
# num_oranges = int(input("how many oranges do you want? "))

# if num_apples > 5 :
#     price_apples = num_apples * price_apples * 0.9
# else :  price_apples = num_apples * price_apples

# if num_oranges > 5 :
#     price_oranges = num_oranges * price_oranges * 0.9
# else :  price_oranges = num_oranges * price_oranges

# print("Your total is: $" + str(price_oranges + price_apples ))

# poisitive_days = 0

# for i in range (7) : 
#     temp = int(input ('todays temp?? '))
#     if temp > 30 :
#         poisitive_days += 1

# print ("num of positive dayz iz " + str(poisitive_days))

desirable = 0
undesirable = 0

for i in range (10) :
     rate = int(input('rate from 1-5 :'))
     if rate >= 3 :
          desirable += 1
     if rate <= 3 :
          undesirable += 1

print ("desirable rates : " + str(desirable))
print ("undesirable rates : " + str(undesirable))