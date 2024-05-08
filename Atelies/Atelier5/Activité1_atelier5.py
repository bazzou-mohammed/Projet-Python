#Activité 1
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
donnees = np.random.randint(1, 101, size=100)

moyenne = np.mean(donnees)

mediane = np.median(donnees)

ecart_type = np.std(donnees)

donnees_pairs = donnees[donnees % 2 == 0]

donnees_impaires = donnees[donnees % 2 != 0]

valeur_maximale = np.max(donnees)

indice_valeur_maximale = np.argmax(donnees)

donnees_triees = np.sort(donnees)
# Affichage des résultats
print("Tableau de données:")
print(donnees)

print("\nMoyenne :", moyenne)
print("Médiane :", mediane)
print("Écart-type :", ecart_type)

print("\nvaleurs paires:")
print(donnees_pairs)

print("\nvaleurs impaires:")
print(donnees_impaires)

print("\nvaleur maximale :")
print(valeur_maximale)

print("\nindice de la valeur maximale :")
print(indice_valeur_maximale)

print("Tableau trié par ordre croissant:")
print(donnees_triees)







