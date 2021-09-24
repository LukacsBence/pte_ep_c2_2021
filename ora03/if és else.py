import random
raw_input_data= input("Adj meg egy számot: ")
try:
    number = int(raw_input_data)
    number2 = 200
    if number < 10:
        print("Ez a szám kisebb, mint 10")
    else:
        print("Ez a szám nagyobb vagy egyenlő mint 10")

    print("Feladat 1")

    if number > 100:
        print("Ez a szám nagyobb mint 100")
    else:
        print("Ez a szám nem nagyobb mint 100")

    print("Feladat 2")
    if number % 2 == 0:
        print("Ez a szám páros")
    else:
        print("Ez a szám páratlan")

    if number % number2 == 0:
        print("A", number2, "osztója a", number)
    else:
        if number2 % number == 0:
            print("A", number, "osztója a", number2)
        else:
            print("Egyik sem osztója a másiknak")

    if number > 0:
        print("Ez a szám pozitív")
    elif number < 0:
        print("Ez a szám negatív")
    else:
        print("A szám 0")

    string = "alma"
    if string[0] == string[-1]:
        print("A szöveg első és utolsó betűje megegyezik")
    else:
        print("A szöveg első és utolsó betűje nem egyezik meg")

    if string[0].isupper():  # if str[0] == str[0].upper():
        print("Nagybetűvel kezdődik")
    else:
        print("Nem nagybetűvel kezdődik")

    str2 = "almafa"
    string = "almaszar"
    if string[0:5] == str2[0:5]:
        print("Az első 5 karakter azonos")
    else:
        print("Nem azonos az első 5 karakter")

    mynumber = 25
    if 3 <= mynumber < 17:
        print("Beleesik a szám a [3;17] intervallumba")
    else:
        print("Nem esik bele az intervallumba")

    a, b, c = random.randint(0, 1000000), random.randint(0, 10000000), random.randint(0, 100000000)
    if a + b > c and a + c > b and b + c > a:
        print("Lehet ezen oldalhosszokkal hármoszöget szerkezteni")
    else:
        print("Nem lehet az oldalhosszokkal háromszöget szerkeszteni")

    if a > b and a > c:
        print(a, "a legnagyobb szám")
    elif b > a and b > c:
        print(b, "a legnagyobb szám")
    elif c > a and c > b:
        print(c, "a legnagyobb szám")
    if a < b and a < c:
        print(a, "a legkisebb szám")
    elif b < a and b < c:
        print(b, "a legkisebb szám")

    elif c < a and c < b:
        print(c, " a legkisebb szám")

    character = "B"
    maganhangzok = "aáAÁeéEÉiIoOóÓöÖőŐuUúÚüÜűŰ"
    if maganhangzok.find(character) >= 0:
        print("magánhangzó")
    else:
        print("nem magánhangzó")

    number = 32
    if number % 3 == 0 and number % 5 == 0:
        print("osztható 3-mal vagy 5-tel")
    elif number % 3 == 0:
        print("csak 3-mal osztható")
    elif number % 5 == 0:
        print("csak 5-tel osztható")
    else:
        print("nem osztható sem 3-mal sem 5-tel")

    grade = random.randint(0, 1)
    if grade == 5:
        print("kiváló")
    elif grade == 4:
        print("jó")
    elif grade == 3:
        print("közepes")
    elif grade == 2:
        print("elégséges")
    elif grade == 1:
        print("elégtelen")
    else:
        print("érvénytelen jegy")
except ValueError:
    print("De én egy számot kértem")