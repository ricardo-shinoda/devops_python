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
