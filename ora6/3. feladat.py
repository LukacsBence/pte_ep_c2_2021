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

if sides[0] + sides[1] > sides[2] or sides[2] + sides[1] > sides[0] or sides[1] + sides[2] > sides[0]
k = side[0] + side[1] + side[2]
d = k / 2
t = (d*(d - sides[0])) * (d*(d - sides[1])) * (d*(d - sides[2])) * 0.5