print("Hello from lesson 14")

counter = 0

def increment_counter():
    global counter
    counter += 1

for i in range (3):
    print(increment_counter)