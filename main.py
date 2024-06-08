from models.parti import Parti
from models.electeur import Electeur
from os import listdir
import os.path

if __name__=="__main__":

    electeur=input("Quel est le nom de l'electeur a charger ? ")
    if not os.path.isfile(f"electeurs/{electeur}.json"):
        exit("""Veuillez copier le template dans /electeurs et \
specifier des poids en fonction de vos priorites dans ce fichier (ex: eliot.json).""")
    
    for p in listdir('programmes'):
        Parti(p.split('.')[0])
    
    try:
        Electeur(electeur).evaluate()
    except KeyboardInterrupt:
        print('\nAu revoir :)')
