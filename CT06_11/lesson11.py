# print("Hello from lesson 11")

# px = int(input("how much $ iz the item? "))

# if px <= 5:
#     print("might be bad quality but fine!")
# elif px <= 50: # <=
#     print("good 2 buy :D")
# elif px <= 500: # <=
#     print("WHERE R U GETTING THIZ MUCH $ !!!????")
# else:
#     print("R.I.P bank account :D")

# r1 = int(input("how tall r you rider 1 ? "))
# r2 = int(input("how tall r you rider 2 ? "))

# result = r1 > 120 and r2 > 120
# print(result)

# num = int(input("give mah a numbah "))

# if num % 3 == 0 and num % 7 == 0:
#     print("the number is divisible by 3 and 7")

# first_name = input("what is ur first name? ")
# last_name = input("what is ur last name? ")

# if first_name == James and first_name == Leong :
#     print ("YOU ARE WANTED")

# r1 = int(input("how old r you rider 1 ? "))
# r2 = int(input("how old r you rider 2 ? "))

# result = r1 >= 18 or r2 >= 18
# if result:
#     print("you can ride :D")
# else: print("you cannot ride :o get a older person 2 come with u :D)")

# age = int(input("how old r you? "))
# if age < 12 or age > 65:
#     print("your ticket iz 15 dollarz")
# else: print("your ticket iz 20 dollarz")

# password_lol = "IAte10HomelessPeopleCuzIThoughtTheyWhereWatermelons"
# userguess = input("what is the password?")
# if not userguess == password_lol:
#     print("Access denied")

# burger = input("want a burger?")
# drink = input("want a drink ?")
# fries = input("want fries ?")

# if burger == "yes" and fries == "yes" and not drink == "yes":
#     print("do u want a drink?")
    
user = "john123"
pw = "pw123"

user_input_user = input("what is the username?")
user_input_pw = input("what is the password?")

if user_input_user == user and user_input_pw == pw:
    print("access granted :D")
elif user_input_user == user or user_input_pw == pw:
    print("user or password is wrong :/")
else: print("access deinied :()")