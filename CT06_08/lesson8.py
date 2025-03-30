print("Hello from lesson 8")

# import random
# num1 = random.randint(1,50)
# num2 = random.randint(1,50)
# question = "what is " + str(num1) + " + " + str(num2) +"?  "
# ans = int(input(question))
# hidden_ans = num1 + num2
# print( ans == hidden_ans )
        # or 
# if ans == hidden_ans :
#     print ("true")
# else
#     print ("false")


# import random
# num1 = random.randint(1,101)
# start  = int(input("start number? "))
# end = int(input("end number? "))
# print ("start number is " +)
# print( start <= num1 <= end )


# num = int(input("give me a number: "))
# print ( num % 2 == 0 )

# num1 = int(input("first number? "))
# num2 = int(input("second number? "))

# print (num1 / num2 == 0 )

import random
num = random.randint(1,10)
ans = int(input("Guess a number from 1 - 10: "))
if ans == num:
    print ("Good job you got it :)")
else:
      print("Awh you did not get it correct")
