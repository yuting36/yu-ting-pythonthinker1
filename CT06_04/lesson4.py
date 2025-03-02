# print("Hello from lesson 4")
 
# print("ready")
# for i in range(3,0,-1):
#     print (i)

start = int(input("give meh a start number  "))
stop = int(input("give meh a stop number  "))

if start > stop:
    for r in range(start , stop - 1 ,-1):
        print (r)
else:
     for r in range(start , stop + 1 ,1):
        print (r)

print ("thats cool anyway heres the numbers 1 - 10000")

for r in range(1,10001):
    print(r)