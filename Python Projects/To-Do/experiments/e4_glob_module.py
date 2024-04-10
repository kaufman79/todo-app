import glob

myfiles = glob.glob("../*.py")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())
