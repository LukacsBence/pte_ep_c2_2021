menu_command = ""
while menu_command != "0":
  menu_command = input("Kérlek válassz a menüpontok közül: \n\t 1 - összeadás \n\t 0 - kilépés\n")
  if menu_command == "1":
    is_number = False
    a = 0
    b = 0
    while not is_number:
      try:
        a = float(input("Kérlek add meg az első számot: "))
        is_number = True
      except ValueError:
        print("A megadott érték nem szám!")
      while not is_number:
        try:
          b = float(input("Kérlek add meg a második számot: "))
          is_number = True
      except ValueError:
        print("A megadott érték szám!")
    print("A két szám összege: ", a+b)
print("Viszlát")

#valami nem jó