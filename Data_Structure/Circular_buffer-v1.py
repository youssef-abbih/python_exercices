buffer = [-2, -1, 0, +1, +2]
index = 2

while True:
    cmd = input("cmd: ")

    if cmd == "exit":
        break

    elif cmd == "gauche" or cmd == "g":
        index = (index - 1) % len(buffer)
        print("Position actuelle:", buffer[index])

    elif cmd == "droite" or cmd == "d":
        index = (index + 1) % len(buffer)
        print("Position actuelle:", buffer[index])

    else:
        print("commande inconnue")
