import os
from jeux.allumette import allumette
from jeux.devinette import devinette
from jeux.morpion import morpion
from score.score_menu import score_menu

if __name__ == "__main__":
    choix:int
    bo:bool

    os.system('clear||cls')
    choix = 0
    while choix != 5:
        bo = True
        os.system('clear||cls')
        print("-------------------------------------------------------------")
        print("Bienvenue dans le menu du jeu : ")
        print("1- Jeu de la devinette")
        print("2- Jeu des allumettes")
        print("3- Jeu du morpion")
        print("4- Score")
        print("5- Quitter")
        print("-------------------------------------------------------------")
        while bo:
            try:
                bo = False
                choix = int(input("faite votre choix : "))
                while choix < 1 or choix > 6:
                    print ("Erreur dans le choix, choisier un choix proposé")
                    choix = int(input("faite votre choix : "))
            except ValueError:
                bo = True
                print("erreur de saisie de valeur !")



        if choix == 1:
            devinette()
        elif choix == 2:
            allumette()
        elif choix == 3:
            morpion()
        elif choix == 4:
            score_menu()
        elif choix == 5:
            print("Au revoir")