# How to open a file with python
# The function is: open()
# parsing: is a process of converting data into a more readable format
# .split convert a string into a list

with open("/home/ricardo/codes/devops_python/src/login_attempts.txt", "r") as file:
    file_text = file.read()
usernames = file_text.split()


def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if i == current_user:
            counter = counter + 1
    if counter >= 3:
        return "You have been blocked for more than 3 tentatives"
    else:
        return "You can login"


print(login_check(usernames, "lucas"))
