def nomjoueur (a:int) -> str:
    """
    fonction pour demmander les pseudos des joueurs

    Entrée : un entier (1,2) pour savoir le joueur qui doit être nommé
    Sortie : une chaîne de caractère

    la fonction retourne le pseudo pour le j1 ou j2 en fonction de la valeur qui est rentrée
    """
    pseudo:str
    pseudo = ""
    if a == 1:
        pseudo = str(input("Qu'elle est le nom du joueur 1 ?  "))
        while pseudo == "":
            print("vous n'avez rien écrit !")
            pseudo = str(input("Qu'elle est le nom du joueur 1 ?  "))
    elif a == 2:
        pseudo = str(input("Qu'elle est le nom du joueur 2 ?  "))
        while pseudo == "":
            print("vous n'avez rien écrit !")
            pseudo = str(input("Qu'elle est le nom du joueur 2 ?  "))

    return pseudo