import random
is_winner = False
while not is_winner:
    try:
        player = int(input("Kérem adja meg, hogy melyiket mutatja: 1 - kő, 2 - papír, 3 - olló: \n"))
        bot = random.randint(1, 3)
        if player == bot:
            print("Döntetlen")
        elif(player == 2 and bot == 1) or (player == 3 and bot == 2) or (player == 1 and bot == 3):
            print("Gratulálok, győztél!")
            is_winner = True
        elif(player == 1 and bot == 2) or (player == 2 and bot == 3) or (player == 3 and bot == 1):
            print("Sajnálom, vesztettél.")
            is_winner = True
    except ValueError:
        print("Nem megfelelő a szám.")