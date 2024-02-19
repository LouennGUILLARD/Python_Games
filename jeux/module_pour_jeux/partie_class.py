from datetime import datetime

class partie:
    date:datetime
    jeu:str
    gagnant:str
    perdant:str
    score:int

    def __init__(self,date:datetime,jeu:str,gagnant:str,perdant:str,score:int) -> None:
        self.date = date
        self.jeu = jeu
        self.gagnant = gagnant
        self.perdant = perdant
        self.score = score