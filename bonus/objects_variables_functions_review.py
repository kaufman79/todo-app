# objects can be stored in variables
name = "John"
last_name = "John Smith"
id = "10221"

members = 5
height = 1.75

# objects can be produced by functions
name = input("whats your name")


height = input("whats your height")

# but the above would produce a number in a string, so we may want to convert it to work with the number, like so
height = float(input("whats your height"))


# functions

# not all functions return a value
# eg in print function, it doesnt retuen anythin. it may print in console, but doesnt return
x = print("Hello")
# then if I call on x, it doesnt return anytrhing

# custom functions can return or NOT return something. based on if you choose to return something at the end
def foo():
    value = 10
    return value

# the above returns 10, stored in the variable

# functions with paramaters/arguments
def square(number):
    result = number * number
    return result


x = square(number=10)


# and can do multiple arguments too
def add_heights(number1, number2):
    result = number1 + number2
    return result

add_heights(10, 12)

# default arguments
def double_number(number1, number2=2):
    result = number1 * number2
    return result

# in the above code, we can omit the default argument, like so
double_number(5)