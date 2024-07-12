pile = []
while cmd != "exit":
    
    cmd = input("cmd: ")

    if cmd == "exit":
        break

    elif cmd == "afficher" or cmd == "a":
        print(pile[::-1])

    elif cmd == "taille" or cmd  == "t":
        print(len(pile))

    elif cmd == "empiler" or cmd == "e":
        if len(pile) == 10:
            print("Buffer overflow")

        else:
            assiette = input("assiette: ")
            pile.append(assiette)

    elif cmd == "retirer" or cmd == "r":
        if not pile:
            print("Buffer underflow")

        else:
            assiette = pile.pop()
            print(f"assiette: {assiette}")
    else:
        print("Commande inconnue")