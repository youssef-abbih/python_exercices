queue = []

while True:
    cmd = input("cmd: ")

    if cmd == "exit":
        break
    elif cmd == "afficher" or cmd == "a":
        print(queue)

    elif cmd == "taille" or cmd  == "t":
        print(len(queue))

    elif cmd == "enqueue" or cmd == "e":
        if len(queue) == 10:
            print("Buffer overflow")
        else:
            personne = input("personne: ")
            queue.append(personne)

    elif cmd == "retirer" or cmd == "r":
        if not queue:
            print("Buffer underflow")
        else:
            personne = queue.pop()
            print(f"assiette: {personne}")
    else:
        print("Commande inconnue")
