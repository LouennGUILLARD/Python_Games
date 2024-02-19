import os
from datetime import datetime
from score.score import ajout
from jeux.module_pour_jeux.joueur import nomjoueur
import jeux.module_pour_jeux.matrice_morpion as m
from jeux.module_pour_jeux.partie_class import partie


def morpion() -> None :
    """
    Procédure du jeu du morpion

    Entrée : rien
    Sortie : rien

    Cet procédure fait démarer le jeux morpion
    """
    mat:list[list[int]]
    j1:str
    j2:str
    bo:bool
    ver:int
    changer_nom:str
    commence:int
    li:int
    col:int
    reco:str


    reco = ""
    #supprésion de se qui est écrit sur le terminal
    os.system('clear||cls')
    #menu de présentation duu jeux
    print("------------------------------------------------------------------------------")
    print("Le Morpion")
    print("Le principe du jeu est simple, vous devez alligne trois fois le meme symbole.")
    print("Chaque joueur a qu'un seule symbole.")
    print("Une fois q'un symbole est placer, il ne peut pas être remplace.")
    print("------------------------------------------------------------------------------")

    j1 = nomjoueur(1)
    j2 = nomjoueur(2)
    while j1 == j2 :
        print("vous avez choisie le même pseudo")
        j1 = nomjoueur(1)
        j2 = nomjoueur(2)

    while reco != "n":
        bo = True
        while bo:
            try:
                bo = False
                print(j1,": joueur 1   ",j2,": joueur 2")
                commence = int(input("Qui commence ? "))
                while commence < 1 or commence > 2:
                    print("erreur, utiliser 1 pour joueur 1 et 2 pour joueur 2")
                    commence = int(input("Qui commence ? "))
            except ValueError:
                bo = True
                print("la valeur entrée n'est pas bonne !")


        if commence == 2:   # type: ignore
            j2,j1 = j1,j2
        ver = 0
        mat = m.matrice(3,3)
        while ver < 9:
            os.system('clear||cls')
            m.affiche(mat)
            #verification pour savoir quel joueur doit jouer
            if ver % 2 == 0:
                print("Au tour de",j1)
            else:
                print("Au tour de",j2)
            
            while True:
                bo = True
                while bo:
                    try:
                        bo = False
                        li = int(input("saisir un numero de ligne : "))
                        while li < 0 or li > 2:
                            print("vous n'avez pas donner une valeur correcte, vous pouvez mettre 0 ou 1 ou 2.")
                            li = int(input("saisir un numero de ligne : "))
                    except ValueError:
                        bo = True
                        print("la valeur entrée n'est pas bonne !")

                bo = True
                while bo:
                    try:
                        bo = False       
                        col= int(input("saisir un numero de colonne : "))
                        while col < 0 or col > 2:
                            print("vous n'avez pas donner une valeur correcte, vous pouvez mettre 0 ou 1 ou 2.")
                            col = int(input("saisir un numero de colonne : "))
                    except ValueError:
                        bo = True
                        print("la valeur entrée n'est pas bonne !")
                
                if mat[li][col] == 0:   # type: ignore
                    break
                else:
                    print("vous ne pouvez pas le mettre ici !")

            if ver % 2 == 0:
                mat[li][col] = 1    # type: ignore
            elif ver % 2 != 0:
                mat[li][col] = 2    # type: ignore

            if m.verification(mat) == 1:
                os.system('clear||cls')
                m.affiche(mat)
                print(j1,"a Gagne !")
                ver = 10
                ajout_sc = partie(datetime.now(),"morpion",j1,j2,(10//ver))
                ajout(ajout_sc,"./score/tableau_score/score_morpion.txt")
            elif m.verification(mat) == 2:
                os.system('clear||cls') 
                m.affiche(mat)
                print(j2,"a Gagne !")
                ajout_sc = partie(datetime.now(),"morpion",j2,j1,(10//ver))
                ajout(ajout_sc,"./score/tableau_score/score_morpion.txt") # type: ignore
                ver = 10
            else:
                ver = m.controle(mat)


        if ver == 9:
            os.system('clear||cls')
            m.affiche(mat)
            print("Egalite !")

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