# Functions in python

def greeting_message():
    print("Hey You, don't help them to burry alive")


greeting_message()

# giving parameters to a function


def calling_name(name, age):
    print(f"Did I stress you out? {name}, I know you are {age} years old")


calling_name("Ricardo", 43)


# Returning statements % function
def calculate_fails(total_attempts, failed_attempts):
    percentage = failed_attempts / total_attempts
    return percentage


result = calculate_fails(10, 4)
if result > 0.5:
    print(f"Account locked, because your result is: {result}")
else:
    print(f"You are good to go, your result is: {result}")
    print(f'the result date type is: {type(result)}')

# max function

a = 2
b = 10
c = 0.5
print(max(a, b, c))
print(min(a, b, c))

# Sort by alphabetical order

username = ["Ricardo", "Ana", "Luísa", "Lucas"]
print(sorted(username))

# Converting integer into string
result = str(123)
print(type(result))
print(len(result))

# string concatenation
print("hello" + "you")

# to apply the upper method for string
result = "Hello World"
print("Hello".upper())

# to applying the lower case to all the letters
print("Hello You".lower())

# to printing specific index
print("hello"[4])

# to slice - specify a period on the index
# Fist number is the index position, the second is considerd index position -1
print("hello"[1:3])

# To search for a caracter index by it's caracter - this is case sensitive
print("hello".index("o"))

# to extract from a list
list = ["a", "b", "c", "d"]
print(list[2])

# to concatenate two lists
second_list = [1, 2, 3, 4]
print(list + second_list)

# to change an element on a list
list = ["a", "b", "c", "d"]
list[1] = 10
print(list)

# to insert an element to a especific position on the list
list = ["a", "b", "c", "d"]
list.insert(0, "Lucas")
print(list)

# to remove a specific element in a list
list = ["a", "b", "c", "d"]
list.remove("a")
print(list)


# to append an item to the end of a list
list = ["a", "b", "c", "d"]
list.append("Luísa")
print(list)
