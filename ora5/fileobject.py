fileobject1= print("hatványok", "r")
fileobject2= print("hatványok2", "r")
line1 = fileobject1.readline()
line2 = fileobject2.readline()
while line1 != "" or line2 != ""
    output_fileobject.write(line1)
    output_fileobject.write(line2)
    line1 = fileobject1.readline()
    line2 = fileobject2.readline()
fileobject1.close()
fileobject2.close()
#Tanárnő jegyzete