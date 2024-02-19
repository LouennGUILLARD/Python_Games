import os
def choisir(proposition:int,j2:str) :

    print(j2, "a proposé :",proposition)
    print("-------------------------------")
    print("choisir entre :")
    print("1: le résultat est trop grand")
    print("2: le résultat est trop petit")
    print("3: rappel du nombre choisi")
    print("4: c'est gagné")
    print("-------------------------------")

def verification(proposition:int,devinette:int,j1:str,j2:str) -> int :
    choix:int
    bo:bool

    choix = 3
    while choix == 3:
        bo = True
        while bo:
            try:
                bo = False
                choisir(proposition,j2)
                choix = int(input("faite votre choix :"))
                while choix < 1 or choix >4:
                    choix = int(input("erreur,faite votre choix :"))
            except ValueError:
                bo = True
                os.system("clear||cls")
                print("vous n'avez pas utiliser de valeur numérique !")
        
        if choix == 1 and proposition < devinette:
            choix = 5
        elif choix == 2 and proposition > devinette:
            choix = 6
        elif choix == 3 :
            print("votre nombre :",devinette)
            print("")
        elif choix == 4 and devinette != proposition:
            print("impossible la proposition de", j2 ,"n'est pas celle de", j1 ,"faite un autre choix")
            choix = 3
        elif (choix == 1 or choix == 2) and devinette == proposition:
            choix = 7

    return choix