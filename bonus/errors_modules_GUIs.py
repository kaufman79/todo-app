# ERRORS
# console does a lot to help usually. But should try to predict errors with try, except
import time

current_year = int(time.strftime("%Y"))

try:
    year_of_birth = int(input("enter year of birth: "))
    age = current_year - year_of_birth
    print(f"the age is {age}")
except ValueError:
    print("invalid entry. Enter a number (YYYY)")

# impt to note tho that try, except cant catch syntax errors.

# comments and doc strings
# see my functions module for examples of custom functions with docstrings. Basically, theyre triple quotes explaining the function.
# comments shouold not be overused in code. Put them in if something will be confusing in two weeks time, but if something is obvious enough, dont comment on it.

# modules are things like my functions module here. But there are also "standard libraries" or standard modules that are preinstalled - glob, time, etc.