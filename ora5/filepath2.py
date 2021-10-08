filepath = "lorem"
fileobject = open(filepath, "r+")
for line in fileobject:
    print(line, end="")
fileobject.close()
