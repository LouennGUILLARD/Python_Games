import os
from jeux.module_pour_jeux.joueur import nomjoueur
from score.score import ajout
from jeux.module_pour_jeux.partie_class import partie
from datetime import datetime


def allumette() -> None:
    j1:str
    j2:str
    val:int
    changer_nom:str
    compt: int
    allu:int
    reco:str
    ajout_sc:partie
    bo:bool

    reco=""
    #suppre sion de se qui est écrit sur le terminal et mise en place du nom des joueurs
    os.system('clear||cls')
    j1 = nomjoueur(1)
    j2 = nomjoueur(2)
    while j1 == j2 :
        print("vous avez choisie le même pseudo")
        j1 = nomjoueur(1)
        j2 = nomjoueur(2)
        os.system('clear||cls')
    os.system('clear||cls')
    #boucle principale pour recommencer le jeux ou non
    while reco != "n":
        os.system('clear||cls')
        #menu de présentation duu jeux
        print("-------------------------------------------------------------------")
        print("Le principe du jeu est simple, il y a 20 allumettes sur la table.")
        print("A chaque tour, vous pouvez retiré 1,2 ou 3 allumettes.")
        print("Celui qui retire la dernière allumette à perdu !")
        print("-------------------------------------------------------------------")
        allu = 20
        compt = 0

        #boucle pour une partie en cours
        while allu > 1:
            #verification pour savoir quel joueur doit jouer
            if compt % 2 == 0:
                print("Au tour de",j1)
            else:
                print("Au tour de",j2)
            
            #affichage des des allumettes à chaque tour
            if allu > 1:
                compt += 1
                print(allu*"|")
                print("il reste ",str(allu),"allumettes .")
            
            #saisie de la valeur par les joueur
            bo = True
            while bo:
                try:
                    bo = False
                    val = int(input("saisir le nombre d'allumettes à elever : "))
                    while val < 1 or val > 3:
                        print("erreur, les valeur disponible sont 1, 2 ou 3.")
                        val = int(input("saisir le nombre d'allumettes à elever : "))
                except ValueError:
                    bo = True
                    print("vous n'avez pas utiliser de valeur numérique !")

            if  allu - val < 0: # type: ignore
                bo = True
                while bo:
                    bo = False
                    try:
                        print("erreur, les valeurs disponible sont 1 ou 2")
                        val = int(input("saisir le nombre d'allumettes à elever : "))
                        while val < 1 or val > 2:
                            print("erreur, les valeur disponible sont 1 ou 2.")
                            val = int(input("saisir le nombre d'allumettes à elever : "))
                    except ValueError:
                        bo = True
                        print("vous n'avez pas utiliser de valeur numérique !")
            allu -= val # type: ignore


            #supprésion de se qui est écrit sur le terminal
            os.system('clear||cls')

        #vérification résultat
        compt += 1
        if allu == 0:
            if compt % 2 == 0:
                print( j2,"a Gagné !")
                print(j1,"a Perdu !")
                ajout_sc = partie(datetime.now(),"alumette",j2,j1,10)
                ajout(ajout_sc,"./score/tableau_score/score_allumette.txt")

            else:
                print(j1,"a Gagné !")
                print(j2,"a Perdu !")
                ajout_sc = partie(datetime.now(),"alumette",j1,j2,10)
                ajout(ajout_sc,"./score/tableau_score/score_allumette.txt")
        elif allu == 1:
            if compt % 2 == 0:
                print(j1,"a Gagné !")
                print(j2,"a Perdu !")
                ajout_sc = partie(datetime.now(),"alumette",j1,j2,10)
                ajout(ajout_sc,"./score/tableau_score/score_allumette.txt")
            else:
                print(j2,"a Gagné !")
                print(j1,"a Perdu !")
                ajout_sc = partie(datetime.now(),"alumette",j2,j1,10)
                ajout(ajout_sc,"./score/tableau_score/score_allumette.txt")
        else:
            print("il y a une erreur !!!")
            
        reco = str(input("La partie est fini, voulez-vous recommencer ? o/n :  "))
        while reco != "o" and reco !="n":
            print("erreur dans la réponse, les réponses possibles sont o ou n")
            reco = str(input("La partie est fini, voulez-vous recommencer ? o/n : "))

        #demande chagement de nom
        if reco == "o":
            changer_nom = str(input("Voulez vous changer de nom ? o/n : "))
            while changer_nom != "o" and changer_nom != "n":
                print("la réponse donnée n'est pas bonne, vous ne pouvez mettre que o pour oui et n pour non !")
                changer_nom = str(input("Voulez vous changer de nom ? o/n : "))
            if changer_nom == "o":
                j1 = nomjoueur(1)
                j2 = nomjoueur(2)