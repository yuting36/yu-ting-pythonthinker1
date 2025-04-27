# print("Hello from lesson 12")

# num = int(input("what is the number? :"))

# if num % 3 == 0 and num % 5 == 0:
#     print ("your number is divisable by 5 and 3 :D")
# else: print ("your number is  not divisable by 5 and 3")

# ppl = 0

# while ppl < 50: 
#     ppl += 1
#     print(ppl)


# ppl = int(input("how many ppl?"))
# maxPpl = int(input("max amt. of ppl?"))
# while ppl < maxPpl: 
#     ppl += 1
#     print(ppl)

# ppl = int(input("how many ppl?"))
# maxPpl = int(input("max amt. of ppl?"))
# while True:
#     Add = input("add person!? ")
#     if Add == "yes" or "YES":
#         ppl += 1
#     if ppl == maxPpl:
#         break
# print("N̶̠̻̰͋͂͘ͅE̴̤̪̼͕̮̙̟̖͋̑̀̀̂͠ͅV̵̛̗̘̊̆͒̓̉̉̚Ě̷̡̛̽̆̇̌͠Ř̷̢̤͎̪̒̆̅ͅ ̵͙͕͙͉̪̮̀̈́c̴̠̦͕̝͇̟̈̌́̏̐́͛͛ó̵̡͙͈̫̘̝m̷͉̭̈́ȩ̷̛͙̠̻̳̫͂ ̴̛̟̎̓̉̓̇̀͛̾b̴̳̓͊͊͆̅̚a̵̡̹̘̳̩̩̿̒̋̋͠č̵̦͕̺̼͖̞̫̓́̏̊̏ḱ̸̨̟͎͓̣͓̳͂͒̈́̂̌̉̆̚")

# order = ""
# skipcomma = True

# while True :
#     item = input ("ORDER WHAT? : ")
#     if item == "end":
#         break
#     else:
#         if skipcomma == True:
#             order += item
#             skipcomma == False
#         else:
#             order = order + ", " + item

# print ("ORDER : " + order)

num = 10

while num != 0:
    print (num)
    num += -1 
else:
    print ("COUNTDOWN IS AT 0 :D")

num = 10

while num != 0:
    print (num)
    num -= 1 # num -= 1 is the same as num = num - 1
    if num == 5 :
        break
else:
    print ("COUNTDOWN IS AT 0 :D")
