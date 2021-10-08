filepath = "lorem"
fileobject = open(filepath, "r+")
print("pozíció:", fileobject.tell())
line = fileobject.readline()
print("pozíció:", fileobject.tell())
while line != "":
    print(line, end = "")
    line = fileobject.readline()
    print("pozíció:", fileobject.tell())
fileobject.close()

