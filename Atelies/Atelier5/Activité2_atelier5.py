# Activité 2
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
notes_maths = np.random.randint(10, 21, size=20)
notes_physique = np.random.randint(12, 19, size=20)
print(notes_maths)
print(notes_physique)

moyenne1 = np.mean(notes_maths)

mediane1 = np.median(notes_maths)

ecart_type1 = np.std(notes_maths)

moyenne2 = np.mean(notes_physique)

mediane2 = np.median(notes_physique)

ecart_type2 = np.std(notes_physique)

print("\nResultats de l'ensemble maths :")
print("moyenne :", moyenne1)
print("mediane :", mediane1)
print("ecart_type :", ecart_type1)

print("\nResultats de l'ensemble physique :")
print("moyenne :", moyenne2)
print("mediane :", mediane2)
print("ecart_type :", ecart_type2)

notes_combined = np.array([[notes_maths, notes_physique]], int)
notes_combined = notes_combined.flatten()
print(" notes combiné:", notes_combined)
print(len(notes_combined))

indice_éléments_supérieurs_à_15 = np.where(notes_combined>15)
# éléments_supérieurs_à_15 = notes_combined[notes_combined > 15] 
print(" indices des éléments supérieurs à 15 :", indice_éléments_supérieurs_à_15[0])

print("Remplacement des notes inférieures à 14 par la valeur 14")
notes_combined[notes_combined < 14] =14
# print(notes_combined)

mentions = notes_combined >= 16
# notes_combined[notes_combined <= 16] = True
# notes_combined[notes_combined > 16] = False

print("tableau booléen indiquant si chaque element supérieure ou égale à 16 :")
print(mentions)

etudiants_meritants = notes_combined[mentions]
print("notes des étudiant meritants :", etudiants_meritants)

nombbre_etudiant_meritants = len(etudiants_meritants)

pourcentage_étudiants = (nombbre_etudiant_meritants*100)/40

print("pourcentage d'étudiants ayant une mention est {} %".format(pourcentage_étudiants))


data = {"Maths": notes_maths, "Physique": notes_physique}
df = pd.DataFrame(data)
df.to_csv("notes_combined.csv", index=False)

