import os
from typing import BinaryIO
from jeux.module_pour_jeux.partie_class import partie
import pickle

def tri_insertion(liste_partie:list[partie]) -> list[partie]:
    n:int
    i:int
    j:int
    val:partie

    n = len(liste_partie)
    for i in range (1,n):
        val = liste_partie[i]
		#décalage tant que nécessaire
        j = i
        while j > 0 and liste_partie[j-1].score < val.score:
            liste_partie[j] = liste_partie[j-1]
            j -= 1
		#ajout à la bonne place
        liste_partie[j] = val
    return liste_partie

def afficher_score (chemin:str) -> None:
    f:BinaryIO
    ligne:partie
    fin:bool
    i:int
    j:int
    liste_partie:list[partie]
    liste_resultat:list[list[str]]
    mot:list[str]

    os.system("clear||cls")
    f = open(chemin,"rb")
    fin = False
    liste_partie = []
    while not fin:
        try:
           ligne = pickle.load(f)
           liste_partie.append(ligne)
        except EOFError:
            fin = True
    liste_partie = tri_insertion(liste_partie)  

    
    liste_resultat = []
    for i in range(len(liste_partie)):
        fin = True
        if liste_resultat != [] :
            for j in range(len(liste_resultat)):
                if liste_partie[i].gagnant == liste_resultat[j][0]:
                    fin = False
                    if liste_partie[i].score >= int(liste_resultat[j][1]):
                        liste_resultat[j][1] = str(liste_partie[i].score)
                        
            if fin:
                mot = [liste_partie[i].gagnant,str(liste_partie[i].score)]
                liste_resultat.append(mot)
        else:
            mot = [liste_partie[i].gagnant,str(liste_partie[i].score)]
            liste_resultat.append(mot)

    for i in range(len(liste_resultat)):
        print(i+1,":",liste_resultat[i][0],"    ",liste_resultat[i][1])

    f.close()


def ajout(ph:partie,chemin:str) -> None:
    fichier : BinaryIO

    fichier = open(chemin,"ab")
    pickle.dump(ph,fichier)
    fichier.close()
