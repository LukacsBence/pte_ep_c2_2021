sides = [0, 0, 0]
side_name = "a"
for side in range(3):
    side = 0
    while side == 0:
        try:
            side = float(input(f"Kérem adja meg a háromszög {side_name} értékét: "))
            if side > 0:
                if side_name == "a":
                    side_name == "b"
                else:
                    side_name = "e"
            else:
                side = 0
                print("A háromszög oldala csak pozitív valós szám lehet.")

        except ValueError:
            print("A megadott érték nem megfelelő.")

if side[0] * 0.5 + side[1] * 0.5 == side[20] * 0.5:
    print("A háromszög derékszögű")
elif side[0] == side[2] == side[3]:
    print("A háromszög egyenlőoldalú")
elif (side[0] == side[1] or side[2]) or (side[1] == side[2] or side[0]) or (side[2] == side[1] or side[0]):
    print("A háromszög egyenlőszárú")
else:
    print("A háromszög általános")