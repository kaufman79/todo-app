#CODE BLOCKS
# WHILE LOOPS are an example of a code block. With things indented under it and such.
while True:
    password = input("Enter password: ")

while password != "pass1":
    password = input("Enter password: ")
# this will run until the user inputs the correct password cause the != (doesnt equal)
print("Password is correct")

# FOR LOOPS
# for loops iterate over sequences - they run through each item in a sequence/array executing the code
usernames = ["john", "sally", "sam"]
for username in usernames:
    print (username.capitalize())
    # prints each name in terminal

# MATCH CASE
# match case is a "control flow code block"
username = input("enter a username: ")
match username:
    case "john":
        print("welcome admin")
    case "sally":
        print("welcome user")
    case "sam":
        print("welcome guest")
    case _:
        print("invalid username")

# F-STRINGS
# they let you put dynamic code into a string...you know this already.