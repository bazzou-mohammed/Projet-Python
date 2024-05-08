import json
from tinydb import TinyDB
# Ecriture dans le fichier json  
def create_json_file(nom_fichier_json, donnees):
    with open(nom_fichier_json, 'w') as fichier_json:
        json.dump(donnees, fichier_json, indent=4)
    
 # Lecture de fichier json   
def read_json_file(nom_fichier):
    with open(nom_fichier, 'r') as fichier_json:
        donnees = json.load(fichier_json)
    return donnees
# Mettre à jour des donnes 
def update_json_file(nom_ficher, cle, nouvelle_valeur):
    donnees = read_json_file(nom_ficher)
    if cle in donnees:
        donnees[cle] = nouvelle_valeur
        with open(nom_ficher, 'w') as fichier_json:
            json.dump(donnees, fichier_json, indent=4)
    else:
        print(f"La clé '{cle}' n'existe pas dans le fichier {nom_ficher}")
# Affiche le contenu
def display_data(nom_ficher):
    donnees = read_json_file(nom_ficher)
    print(f"Contenu du fichier {nom_ficher} :")
    print(json.dumps(donnees, indent=4))

# Exemple d'utilisation
fichier_json = "donnees.json"
donnees = {'nom': 'Mohammed Bazzou', 
        'age': 30, 
        'ville': 'Paris',
        'est_etudiant': False, 
        'Hobbies' : ["Sport", "Music", "Lecture"]
        }

# fichier JSON avec des données
create_json_file(fichier_json, donnees)

# Lecture de données depuis le fichier JSON
donnees_depuis_fichier_json = read_json_file(fichier_json)
# print("Données lues depuis le fichier JSON :", donnees_depuis_fichier_json)

print("!!!!!!!!!!!!!fichier JSON avant la mise à jour !!!!!!!!!!!!!!!!!!")
# Afficher le contenu du fichier JSON avant la mise à jour
display_data(fichier_json)

# Mettre à jour une valeur dans le fichier JSON
update_json_file(fichier_json, 'Hobbies', ["Voyage", "Music", "Lecture"])
update_json_file(fichier_json, 'est_etudiant', True)
update_json_file(fichier_json, 'ville', 'Nice')
update_json_file(fichier_json, 'age', 27)

print("!!!!!!!!!!!!!fichier JSON après la mise à jour !!!!!!!!!!!!!!!!!!")
# Afficher le contenu du fichier JSON apres la mise à jour
display_data(fichier_json)