feet_inches = input("enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet, {parsed['inches']} inches is {result} meters")

if result < 1:
    print("kid is too small to ride.")
else:
    print("kid can use the slide.")