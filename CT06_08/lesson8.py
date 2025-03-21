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


import random
num1 = random.randint(1,50)
start  = int(input("start number? "))
end = int(input("end number? "))
print( start <= num1 <= end )
