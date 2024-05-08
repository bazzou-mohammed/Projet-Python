#Activité 1
from datetime import datetime
#classe de base pour une personne 
class Personne():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
# Classe Client héritant de Personne
class Client(Personne):
    def __init__(self, nom, prenom, numero_telephone):
        super().__init__(nom, prenom)
        self.numero_telephone =numero_telephone
# Classe Reservation
class Reservation():
    def __init__(self, client,nombre_de_personnes, heure_date):
        self.nombre_de_personnes=nombre_de_personnes
        self.heure_date=heure_date
        self.client = client
    def Affiche_reservation(self):
        print(f"Reservation au nom de {self.client.nom} {self.client.prenom}")
        print(f"Numero de télephone :  {self.client.numero_telephone}")
        print(f"Nombre de personnes : {self.nombre_de_personnes}")
        print(f"Heure et date : {self.heure_date.strftime('%Y-%m-%d %H:%M')}  ")

#Activité 2
class Table():
    def __init__(self, numero_table, capacite):
        self.numero_table=numero_table
        self.capacite=capacite

class TableRonde(Table):
    def __init__(self, numero_table, capacite, diametre):
        super().__init__(numero_table, capacite)
        self.diametre = diametre
class TableCarree(Table):
    def __init__(self, numero_table, capacite, longeur):
        super().__init__(numero_table, capacite)
        self.longeur = longeur

# Activite 3
class Article():
    def __init__(self, nom, prix):
        self.nom =nom
        self.prix = prix
        
class CommandeArticle(Article):
    def __init__(self, nom, prix ,quantite_commandee):
        super().__init__(nom, prix)
        self.quantite_commandee=quantite_commandee


class Commande():
    def __init__(self,client, articles):
        self.client = client
        self.articles=articles

    def calculer_total(self):
        return sum (article.prix * article.quantite_commandee for article in self.articles)       


# Combiner tous les trois parties dans un seul main 
class Main: 
    # Fonction test reservation
      def test_reservation(self):
        client = Client("Bazzou", "Mohammed", "0753762897")
        date_heure = datetime(2024, 4, 28, 19, 00)
        reservation = Reservation(client, 8, date_heure)
        reservation.Affiche_reservation()

        # Fonction test table
      def test_table(self):
        table_ronde = TableRonde(2, 4, 0.8)
        table_carree = TableCarree(1, 8, 2)
        print(f"Table carree numéro {table_carree.numero_table}, de diametre {table_carree.longeur} est réservée pour {table_carree.capacite} personnes ")
        print(f"Table ronde numéro {table_ronde.numero_table}, de diametre {table_ronde.diametre} est réservée pour {table_ronde.capacite} personnes ")

      # Fonction test commande 
      def test_commande(self):
        #client
        client = Client("jean", "laptop","0765432789")
        #commander les articles 
        article1 = CommandeArticle("Pizza fruit de mer", 10,1)
        article2 = CommandeArticle("Tacos poulet", 8, 1)
        article3 = CommandeArticle("Kebab", 7, 1)

        # création d'une liste d'articles 
        articles = [article1, article2, article3]

        # Total de la commande
        Total_commande = Commande(client, articles)
        total = Total_commande.calculer_total()
        print(f"Le total à payer: {total} euros")
#Execution des trois tests
if __name__ == "__main__":
    main = Main()
    main.test_reservation()
    main.test_table()
    main.test_commande() 

        











        
        



















