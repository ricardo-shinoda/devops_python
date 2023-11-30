# For loop
for i in range(10):
    print("Cannot connect to the destination")


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
    print(i)

fruits = ["apple", "pinaple", "banana", "avocado"]
for i, fruits in enumerate(fruits):
    print(f'Index {i}: {fruits}')

# While loop

max_devices = 5
i = 1

while i < max_devices:
    print(f"Your number of devices registered is {i}")
    i = i + 1
print("User has reached max number os connected devices")
