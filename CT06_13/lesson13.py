# print("Hello from lesson 13")

# Amt_acc = 1000

# while True: 
#     print("what would you like to do?:  (insert the number)")
#     print("1) withdraw")
#     print("2) deposit")
#     print("3) account balance")
#     print("4) exit")
#     user_choice = int(input("what would you like to do?  "))

#     if user_choice == 1:
#         user_amt = int(input("amount to withdraw?  "))
#         if Amt_acc < user_amt:
#             print("LOL U too broke get a job XD")
#         else:
#             Amt_acc = Amt_acc - user_amt # check syntax
#             print("you now have this amt in ur account : $" + str(Amt_acc))

#     if user_choice == 2:
#         user_amt = int(input("amount to withdraw?  "))
#         Amt_acc += user_amt
#         print("you now have this amt in ur account : $" + str(Amt_acc))

#     if user_choice == 3:
#         print("you now have this amt in ur account : $" + str(Amt_acc))

#     if user_choice == 564603311760073:
#         user_amt = int(input("HOW MUCH DO YOU WANT TO HAVE IN UR ACCOUNT?  "))
#         Amt_acc = user_amt
#         print("you now have this amt in ur account : $" + str(Amt_acc))

#     if user_choice == 4:
#         break


buy_items = [
    "Apples",
    "Bread",
    "Carrots",
    "Dates",
    "Eggs",
    "Flour",
    "Grape",
    "Honey"
]
# print (buy_items)
# buy_items[6] = "herbs"
# print (buy_items)
# buy_items.append("ice")
# buy_items.insert(1, "banana")
# print (buy_items)
# buy_items.pop(2)
# print (buy_items)

# 


pizza_top = [
    "Mushrooms",
    "tomatos",
    "peperoni",
    "pineapple"
]

while True:
    print("Toppings:")
    for i in pizza_top:
        print(i)