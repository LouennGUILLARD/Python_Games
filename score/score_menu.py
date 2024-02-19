from score.score import afficher_score
import os
def score_menu() -> None:
    """
    Proccédure menu score

    Entrée : rien
    Sortie : rien

    Cette procédure permet le fonctionnement des scores des jeux
    """
    bo:bool
    choix:int
    validation:str

    choix = 0
    os.system("clear||cls")
    while choix != 4:
        os.system("clear||cls")
        print("-------------------------------------------------------------")
        print("Choisissez le score du jeu que vous désirez: ")
        print("1- Score de devinette")
        print("2- Score des allumettes")
        print("3- Score du morpion")
        print("4- Quitter")
        print("-------------------------------------------------------------")
        bo = True
        validation = "0"
        while bo:
            try:
                bo = False
                choix = int(input("faite votre choix : "))
                while choix < 1 or choix > 4:
                    print("Le choix entré n'est pas dans la liste")
                    choix = int(input("faite votre choix : "))
            except ValueError:
                bo=True
                print("La valeur entrée n'est pas correcte !")

        if choix == 1:
            while validation != "":
                afficher_score("./score/tableau_score/score_devinette.txt")
                validation = input("appuyer sur ENTRER pour quitter")
        elif choix == 2:
            while validation != "":
                afficher_score("./score/tableau_score/score_allumette.txt")
                validation = input("appuyer sur ENTRER pour quitter")
        elif choix == 3:
            while validation != "":
                afficher_score("./score/tableau_score/score_morpion.txt")
                validation = input("appuyer sur ENTRER pour quitter ")