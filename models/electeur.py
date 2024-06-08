import json
import os.path
from os import listdir
from os import system
from models.parti import Parti

def oscls():
    try:
        system('cls')
    except:
        system('clear')

class Electeur:
    electeurs={}

    def __init__(self, name: str):
        if not os.path.isfile(f"electeurs/{name}.json"):
            return None
        with open(f"electeurs/{name}.json", "r") as file:
            self.themes=json.load(file)
        self.name=name
        self.scores={}
        Electeur.electeurs[name]=self
    
    def ask_score():
        score=input('Quel score sur 100 donnez vous à cette réponse ? ')
        while True:
            try:
                return int(score)
            except:
                score=input('Quel score sur 100 donnez vous à cette réponse ? ')

    def evaluate(self):
        scores={parti:0 for parti in Parti.list(values=False)}
        total=0
        for theme, coef in self.themes.items():
            oscls()
            print(f"Voici les propositions des partis pour le theme {theme}:\n")
            for parti in Parti.list():
                print(f"Parti: {parti}\n")
                print(parti.get_proposition(theme))
                scores[f"{parti}"]+=coef*Electeur.ask_score()
                print()
            total+=coef
        self.scores={key: "{:.2f}".format(value/total) for key, value in scores.items()}
        self.display_scores()
    
    def display_scores(self):
        oscls()
        print("Voici les scores des partis:")
        for key, value in self.scores.items():
            print(f"{key}: {value}%")
