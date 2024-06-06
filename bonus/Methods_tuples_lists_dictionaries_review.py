# these things are called arrays or sequence types

# methods
"hello there".upper() # returns "HELLO THERE"

"hello there".capitalize() # returns "Hello there"

"hello there".title() # returns "Hello There"

# can also apply these functions to variables storing strings. This is more common when programming programs
greeting = "hello there"
greeting.title() # returns "Hello There". But the method doesnt actually change the original variable.

# methods applied to lists do change the object though. methods change the object when the object is mutable (like a list)
groceries = ["vinegar", "olives", "bread"]
groceries.append("apples") # this changes the list, but doesnt return anything.

# lists are used for homogenous items, and you use a list when the list/items may be changed
# TUPLES are better for heterogenous items. Like strings, Tuples have no methos that modify the original
values = (1920, 1080, "grayscale", "JPG")

# indexing
# ecce:
groceries[0] # returns/refers to 1st item in list
values[2] # returns/refers to 3rd item in tuple

# can even do this for a string
string = "tomato"
string[2] # returns/refers to "m", the 3rd letter of tomato

# negative indexing is helpful if you're referring to something that comes close to the end of an array/sequence
string[-2] # retruns t, the second to last letter.

# index slicing
values[1:3] # returns index 1 and 2 of that tuple (not index 3, the 2nd number is not inclusive)


# dictionaries
# dictionaries are good when your values are heterogenous. and its impt to have labels on them, ie KEYS
john = {"first name":"John", "last name": "smith", "age": 40}
# so they are {KEY: VALUE}

john["last name"] #returns "smith"


# can have an array of arrays. ie, dictionaries inside of a list