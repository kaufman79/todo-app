print("this app checks your password to see whether it is strong from a security standpoint."
      " A strong password will fulfill three conditions:\n"
      "1. have 8 characters or more\n"
      "2. have at least one digit\n"
      "3. have at least one uppercase letter")

password = input("enter a password to test: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

contains_digit = False
for i in password:
    if i.isdigit():
        contains_digit = True
        break

result.append(contains_digit)

contains_cap = False
for i in password:
    if i.isupper():
        contains_cap = True
        break

result.append(contains_cap)

if all(result) == True:
    print("strong password")
else:
    print("weak password")
