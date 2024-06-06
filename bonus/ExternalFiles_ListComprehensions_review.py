# Files
# creating and reading files
# easist way to creat a file is by using the open function
with open("book.txt", "w") as file:
    file.write("Hello there!")

content = """From a traditional/confessional perspective, it may be that only the writings of the apostle John are 
written after the destruction of the temple. One could argue for a later date for some other books though, such as 
Matthew, Luke, Acts, and Hebrews."""

with open("book.txt", "w") as file:
    file.write(content)

# reading a file
# writelines creates a list of strings, write creates just a string.
with open("book.txt", "r") as file:
    content = file.read()


# list comprehensions
numbers = [1, 2, 3, 4]
squares = [number * number for number in numbers]
print(squares)  # Output: [1, 4, 9, 16]