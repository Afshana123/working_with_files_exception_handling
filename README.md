# working with files
## Error and Exception Handling 

### `try`, `except` and `finally` block of codes - these are case sensitive
- They work as if and else block - 

```python
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

try:
    file = open("order.txt")
except FileNotFoundError as errmsg:
    # raise
# there is something called creating aliases which means short form (rather than calling it with the full message, you can shorten it").
    print("order.txt not found")
finally:
    print("Thank you for vising, hope to see you again")
```

```python
### Handling files - Reading files



- We have already opened a file and we have begun to handle some of the errors that can come from it but there are many more options to be applied to the opening of a file. The key part is adding a mode to the file opening



`open(file, mode)`



| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|
```

```python
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

```