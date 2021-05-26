### 'try', 'except' and 'finally' block of codes
# They work like the if and else block -

# I would like to declare a method called greeting

# def greetings():
#     pass

# name = "devops"
# year = 2021
# print(name + year)
# # Type Error
#
# #There is a method called open
# file =open("order.txt")
# No such file or directory found

# There are different types of errors that we see in our codes
# We use try, except and finally to deal with these errors for the user

# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     # raise
# # there is something called creating aliases which means short form (rather than calling it with the full message, you can shorten it").
#     print("order.txt not found")
# finally:
#     print("Thank you for vising, hope to see you again")


# Second Iteration
# def open_using_with_and_print(file):
#
#     try:
#         with open("order.txt", "r") as file:
#             for line in file.readlines():
#                 print(line.rstrip('\n')) # prints it on separate lines
#     # try code block ends
#     except FileNotFoundError as errmsg:
#         print("Sorry, file not found :(")
#
#     finally:
#         return "Thank you for visiting, hope to see you again"

# print(open_using_with_and_print("order.txt"))
# create a function to called open_with_to_write_to_file write/add/append

# create a new function to call open_with_to_write_to_file write/add/append
# display the date with the added items - item name - pizza, cakes , avacados, biriyani, pasta

def open_with_to_write_to_file(file):

    try:
        with open("order.txt", "r+") as file_object: #read and append = r+
            file_object.write("\nPizza")
            file_object.write("\nCakes")
            file_object.write("\nAvacados")
            file_object.write("\nBiriyani")
            file_object.write("\nPasta")
            for line in file_object.readlines():
                print(line.rstrip('\n'))
    # try code block ends
    except FileNotFoundError as errmsg:
        print("Sorry, file not found :(")

    finally:
        return "Thank you for visiting, hope to see you again"

print(open_with_to_write_to_file("order.txt"))







