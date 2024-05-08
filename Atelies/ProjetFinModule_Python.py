import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
################################ Gestion des étudiants ##################################
class Etudiants:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, nom, prenom, numero_etudiant):
        etudiant = {
            'nom': nom,
            'prenom': prenom,
            'numero_etudiant': numero_etudiant
        }
        self.etudiants.append(etudiant)
        print(f"L'étudiant {nom} a été ajouté avec succès.")

    def mise_a_jour_infos(self, nom, nouvelle_info):
        for etudiant in self.etudiants:
            if etudiant['nom'] == nom:
                etudiant['nom'] = nouvelle_info['nom']
                etudiant['prenom'] = nouvelle_info['prenom']
                etudiant['numero_etudiant'] = nouvelle_info['numero_etudiant']
                print("Les informations ont été mises à jour.")
         

    def supprimer_infos(self, nom):
        for etudiant in self.etudiants:
            if etudiant['nom'] == nom:
                self.etudiants.remove(etudiant)
                print(f"L'étudiant {nom} a été supprimé avec succès.")
         
########################################## test pour la gestion des étudiants ###############################################
# etudiants = Etudiants()
# etudiants.ajouter_etudiant("mohammed", "Bazzou", 12345)
# etudiants.ajouter_etudiant("Younes", "Lakhnichy", 67890)

# print("Étudiants avant la mise à jour :")
# for etudiant in etudiants.etudiants:
#     print(etudiant)

# etudiants.mise_a_jour_infos("mohammed", {'nom': 'Khalid', 'prenom': 'zeribi', 'numero_etudiant': (567890)})

# print("Étudiants après la mise à jour :")
# for etudiant in etudiants.etudiants:
#     print(etudiant)

# etudiants.supprimer_infos('Younes')

################################ Gestion des Cours ##################################
class Cours:
    def __init__(self):
        self.cours = []

    def ajouter_cour(self, nom, code_cour, professeur_responsable):
        cour = {
            'nom': nom,
            'code_cours': code_cour,
            'professeur_responsable': professeur_responsable
        }
        self.cours.append(cour)
        print(f"Le cours {nom} a été ajouté avec succès.")

    def mise_a_jour_cour(self, nom, nouvel_cour):
        for cour in self.cours:
            if cour['nom'] == nom:
                cour['nom'] = nouvel_cour['nom']
                cour['code_cours'] = nouvel_cour['code_cours']
                cour['professeur_responsable'] = nouvel_cour['professeur_responsable']
                print("Les informations ont été mises à jour.")
         

    def supprimer_cour(self, nom):
        for cour in self.cours:
            if cour['nom'] == nom:
                self.cours.remove(cour)
                print(f"Le cours {nom} a été supprimé avec succès.")
         
########################################## test pour la gestion des cours ###############################################

# cours = Cours()
# cours.ajouter_cour("Math", 12345, "jerome")
# cours.ajouter_cour("Physique", 67890, "stephane")

# print("Cours avant la mise à jour :")
# for cour in cours.cours:
#     print(cour)

# cours.mise_a_jour_cour("Math", {'nom': 'français', 'code_cours': 00000, 'professeur_responsable': 'Jean'})

# print("Cours après la mise à jour :")
# for cour in cours.cours:
#     print(cour)

# cours.supprimer_cour('Physique')


################################ Gestion des notes ##################################

class Notes():
    def __init__(self):
        self.notes = []

    def ajouter_note(self, nom, note, matiere):
        N = {
            'nom': nom,
            'Note': note,
            'matiere': matiere,
        }
        self.notes.append(N)
        print(f"La note {note} a été ajoutée à l'étudiant {nom} pour la matière {matiere}.")

    def mettre_a_jour_note(self, nom, note, matiere):
        for N in self.notes:
            if N['nom'] == nom :
                N['Note'] = note
        print(f"La note {note} de {nom} a été mise à jour pour la matière {matiere}.")
       

    def supprimer_note(self, nom, matiere):
        for N in self.notes:
            if N['nom'] == nom :
                self.notes.remove(N)
        print(f"La note de {nom} pour la matière {matiere} a été supprimée.")
        

    def calculer_moyenne(self):
        return np.mean([N['Note'] for N in self.notes])

    def calculer_mediane(self):
        return np.median([N['Note'] for N in self.notes])

    def calculer_ecart_type(self):
        return np.std([N['Note'] for N in self.notes])
             
########################################## test pour la gestion des notes  ###############################################
# Exemple d'utilisation
# notes = Notes()
# notes.ajouter_note("Mohamed", 15, "Maths")
# notes.ajouter_note("mohamed", 14, "Physique")
# notes.ajouter_note("mohamed", 12, "Histoire")
# notes.ajouter_note("mohamed", 13, "Français")
# notes.ajouter_note("mohamed", 16, "Anglais")

# print("Moyenne :", notes.calculer_moyenne())
# print("Médiane :", notes.calculer_mediane())
# print("Écart type :", notes.calculer_ecart_type())

# notes.mettre_a_jour_note("mohamed", 16, "Maths")
# notes.supprimer_note("Mohamed", "Physique")

# Création de rapports 
etudiants  = [ {"id":1, "nom":"Bazzou", "prenom": "Mohammed", "numero_etudiant":"15F94Y"},
               {"id":2, "nom":"Lkhnichy", "prenom": "Younes", "numero_etudiant":"A150T3"},
               {"id":3, "nom":"Zeribi", "prenom": "Karim", "numero_etudiant":"1Q094Q"}
               ]
coures  =    [ {"code_cour":"MATH101", "nom":"Algèbre", "professeur_responsable": "M.Jerome"},
               {"code_cour":"PHY101", "nom":"Mécanique", "professeur_responsable": "Mme.Alice"}
               ]


# Initialisation de notes
np.random.seed(0)
notes = np.random.randint(0, 21, size=(len(etudiants), len(coures)))

# Création de dataFrames
etudiant_df = pd.DataFrame(etudiants)
coures_df = pd.DataFrame(coures)
grad_df = pd.DataFrame(notes, index=[s["id"]for s in etudiants], columns=[c["code_cour"] for c in coures])

# graphe
moyennes_par_etudiant = grad_df.mean(axis=1)
medianes_par_etudiant = grad_df.median(axis=1)
plt.figure(figsize=(10,6))
plt.bar(etudiant_df["numero_etudiant"], moyennes_par_etudiant, color='skyblue')
plt.xlabel("numero étudiant")
plt.ylabel("Moyenne des notes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()