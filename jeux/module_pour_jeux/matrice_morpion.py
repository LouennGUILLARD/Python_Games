def verification(tab:list[list[int]]) -> int:
    """
    Fonction qui prend la liste dumorpion et qui verrifie sui une des possibilité de gagné est remplie

    Entrée : tab --> list[list[int]]
    Sortie : int --> 0,1,2 --> 1 pour victoire joueur 1, 2 pour victoire Joueur 2 sinon 0

    Retourne un nombre (0,1,2) selon les paramètre expliquer juste au dessus
    """
    i:int
    ver:int

    ver = 0
    for i in range(3):
        if tab[i][0] == tab[i][1] and tab[i][1] == tab[i][2]:
            if ver == 0:
                ver = tab[i][0]
        elif tab[0][i] == tab[1][i] and tab[1][i] == tab[2][i]:
            if ver == 0:
                ver = tab[0][i]

    if tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] :
        if ver == 0:
            ver = tab[0][0]
    elif tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] :
        if ver == 0:
            ver = tab[0][2]
    
    return ver

def affiche (tab:list[list[int]]):
    """
    Procédure qui sert à afficher le tableau du morpion

    Entrée : tab --> list[list[int]]
    Sortie : rien

    Affiche le tableau en entier
    """
    i:int
    j:int
    ver:int
    ph:str

    print("   0   1   2 ")
    for i in range(len(tab)):
        ver = 0
        ph =""
        for j in range (len(tab[i])):
            if ver == 0:
                ph += str(i)
                ph += "  "
            if tab[i][j] == 1:
                ph += "X"
            elif tab[i][j] == 2:
                ph += "O"
            else:
                ph += "."
            if ver < 2:
                ph += " | "
            ver += 1
        print(ph)
        

def matrice(nligne:int,ncol:int)->list[list[int]]:
    """
    fonction qui créer un tableau à double entrée avec n lignes et m colonnes

    Entrée: nligne --> entier, ncol --> entier
    Sortie: tab 

    rtourne un tableau à double entrée rempli de 0
    """
    i:int
    j:int
    mat : list[list[int]]
    mat = list([])

    #création d'une liste pour chaque ligne du tableau, il y aura nligne lignes dans se tableau
    for j in range(nligne):
        j = j
        ligne:list[int]
        ligne = []
        #chaque ligne de se tableau à ncol valeur
        for i in range(ncol):
            i = i
            ligne.append(0)
        mat.append(ligne)
    return mat

def controle(tab:list[list[int]]) -> int:
    """
    Fonction qui sert à savoir le nombre de tour qu'il reste

    Entrée : tab --> list[list[int]] --> morpion
    Sortie : int --> nombre de tour jouer

    Retourne le nombre de tour jouer
    """
    i:int
    j:int
    a:int

    a = 0
    for i in range (len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] != 0:
                a += 1

    return a