
from score.score import ajout
from jeux.module_pour_jeux.partie_class import partie
from datetime import datetime
import jeux.module_pour_jeux.module_devinette as module_jeu
from jeux.module_pour_jeux.joueur import nomjoueur
import os


def devinette() -> None :
    devinette: int
    resultat_ver:int
    limite_h:int
    limite_b:int
    reco:str
    bo:bool
    tour:int
    proposition:int
    changer_nom:str
    j1: str
    j2:str
    ajout_sc:partie

    os.system("clear||cls")
    j1 = nomjoueur(1)
    j2 = nomjoueur(2)
    while j1 == j2 :
        print("vous avez choisie le même pseudo")
        j1 = nomjoueur(1)
        j2 = nomjoueur(2)
        os.system('clear||cls')

    reco = ""
    while reco != "n":
        bo = True
        tour = 1
        limite_b = 0
        os.system('clear||cls')
        #initialisation de la partie on  definie le chiffre a deviner et on fait le 1er tour
        print(j1,":")
        while bo:
            try:
                bo = False
                print("------------------------------------------------------------------------------------")
                print("Le jeu de la deviennette")
                print("Le principe est simple, le joueur 1 fait deviner un nombre au joueur 2 !")
                print("Le joueur 2 va lui dire si le nombre donner par J1 est plus petit, plus grand .")
                print("Joueur 1, fait attention à ne pas mentir sur vos réponses !")
                print("Bonne partie")
                print("------------------------------------------------------------------------------------")
                limite_h=int(input("choisie la limite du nombre a deviner : "))
                while limite_h <0:
                    limite_h=int(input("choisie la limite du nombre a deviner : "))
            except ValueError:
                print("la valeur entrée n'est pas bonne !")
                bo = True
        
        print(j1,":")
        
        bo = True
        while bo:
            try:
                bo = False
                devinette=int(input("choisir le chiffre à faire deviner : "))
                while devinette <0 or devinette >limite_h:  # type: ignore
                    devinette =int(input("erreur,choisir le chiffre à faire deviner :"))
            except ValueError:
                bo = True
                print("la valeur entrée n'est pas bonne !")
        os.system("clear||cls")
        

        resultat_ver = 0
        # 1 tour dans le jeu d'abord avec le tour de J2 qui propose un autre nombre
        while resultat_ver != 4 :
            bo = True
            print("la limite du nombre est entre ",limite_b," et ",limite_h)
            while bo:
                try:
                    bo = False
                    proposition = int(input("choisir un chiffre : "))
                    while proposition < 0 or proposition > limite_h:
                        proposition = int(input("impossible, choisir un chiffre : "))
                except ValueError:
                    bo = True
                    print("la valeur entrée n'est pas bonne !")
                    
            os.system("clear||cls")
            resultat_ver = module_jeu.verification(proposition,devinette,j1,j2) # type: ignore
            os.system("clear||cls")
            if resultat_ver == 1 or resultat_ver == 2:
                if resultat_ver == 1:
                    print(j1," a dit trop grand")
                    limite_h = proposition  # type: ignore
                elif resultat_ver == 2:
                    print (j1," a dit trop petit")
                    limite_b = proposition  # type: ignore
            elif resultat_ver == 5:
                print(j1,"a mal repondu, le chiffre est plus petit !")
                limite_b = proposition  # type: ignore
            elif resultat_ver == 6:
                print(j1,"a mal repondu, le chiffre est plus grand !")
                limite_h = proposition  # type: ignore
            tour +=1
                
            if resultat_ver == 4:
                if tour <2:
                    print("Bravo vous avez deviné en",tour,"tour")
                else:
                    print("Bravo",j2 ,"à deviné en",tour,"tours")

            elif resultat_ver == 7:
                print(j2,"veut vous faire perdre !!! Vous avez gagner")
                if tour <2:
                    print("Bravo,",j2,"à deviné en",tour,"tour")
                else:
                    
                    print("Bravo",j2 ,"à deviné en",tour,"tours")
        
        ajout_sc = partie(datetime.now(),"devinette",j2,j1,int(100//tour))
        ajout(ajout_sc,"./score/tableau_score/score_devinette.txt")

        reco = str(input("La partie est fini, voulez-vous recommencer ? o/n : "))
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