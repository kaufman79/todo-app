from parser14 import parse
from converters14 import convert

feet_inches = input("enter feet and inches: ")




parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet, {parsed['inches']} inches is {result} meters")

if result < 1:
    print("kid is too small to ride.")
else:
    print("kid can use the slide.")