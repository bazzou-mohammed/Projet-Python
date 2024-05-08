from datetime import datetime, timedelta
import random
import pandas as pd
import matplotlib.pyplot as plt

dates = [datetime(2023, 1, 1) + timedelta(days=i) for i in range(365)] 
produits = ['Produit_A', 'Produit_B', 'Produit_C']

quantites = [random.randint(10, 100) for _ in range(365)]

prix_unitaires = [random.uniform(10, 180) for _ in range(365)]

data = {
    'Date': dates,
    'Produit': [random.choice(produits) for _ in range(365)],
    'Quantité': quantites,
    'Prix unitaire': prix_unitaires
}
df = pd.DataFrame(data)
# print(df)
#1
print("Les 5 premières lignes du DataFrame :")
print(df.head())
#2
chiffre_affaires_total = (df['Quantité'] * df['Prix unitaire']).sum()
print("\nLe chiffre d'affaires total réalisé par l'entreprise est de :", chiffre_affaires_total)

#3
produit_plus_vendu = df.groupby('Produit')['Quantité'].sum().idxmax()
print("Le produit le plus vendu est :", produit_plus_vendu)

#4 
df['Chiffre_affaires'] = df['Quantité'] * df['Prix unitaire']  
meilleur_chiffre_affaires_journalier = df.groupby('Date')['Chiffre_affaires'].sum().idxmax()
print("\nLa date à laquelle l'entreprise a réalisé le meilleur chiffre d'affaires est :", meilleur_chiffre_affaires_journalier)

#5
ventes_par_produit = df.groupby('Produit')['Quantité'].sum()
ventes_par_produit.plot(kind='bar', xlabel='Produit', ylabel='Quantité vendue', title='Ventes par produit')
plt.show()