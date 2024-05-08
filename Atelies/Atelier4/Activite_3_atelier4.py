# Classe Livre
class Livre():
    def __init__(self, Titre, Auteur, Annee_de_publication, ISBN):
        self.Titre = Titre
        self.Auteur = Auteur
        self.Annee_de_publication = Annee_de_publication
        self.ISBN = ISBN
# Classe Membre   
class Membre():
    def __init__(self, Nom, Numero_de_membre, Livres_empruntes :list):
        self.Nom = Nom
        self.Numero_de_membre = Numero_de_membre
        self.Livres_empruntes = Livres_empruntes

# Classe Bibliotheque
class Bibliotheque():
    def __init__(self):
        self.Livres_disponibles = []

    def Ajouter_un_livre(self, Livre):
        self.Livres_disponibles.append(Livre)
        print(f"Le livre '{Livre.Titre}' a été ajouté.")

    def Retirer_un_livre(self, Livre):
        if Livre in self.Livres_disponibles :
           self.Livres_disponibles.remove(Livre)
           print(f"Le livre '{Livre.Titre}' a été retiré.")
        

    def Emprunter_un_livre(self, Membre, Livre):
        if Livre in self.Livres_disponibles :
           Membre.Livres_empruntes.append(Livre)
           self.Livres_disponibles.remove(Livre)
           print(f"Le livre '{Livre.Titre}' a été emprunté par {Membre.Nom}.")
        else :
            print(f"Le livre '{Livre.Titre}' n'est pas disponible")

    def Retourner_un_livre(self, Membre, Livre):
        if Livre in self.Livres_disponibles :
            print(f"Le livre '{Livre.Titre}' n'a pas été emprunté par {Membre.Nom}.")         
        else:  
           Membre.Livres_empruntes.remove(Livre)
           self.Livres_disponibles.append(Livre)
           print(f"Le livre '{Livre.Titre}' a été retourné par {Membre.Nom}.")


livre1 = Livre("test1", "M.Bazzou", 1997, 9780747532743)
livre2 = Livre("test2", "M.zakraoui", 1954, 9780544003415)
membre1 = Membre("Mohamed", 12345, [])
membre2 = Membre("khalid", 12745, [])
bibliotheque = Bibliotheque()
print("Ajout d'un ou plusieurs lives : ")
bibliotheque.Ajouter_un_livre(livre1)
# bibliotheque.Ajouter_un_livre(livre2)

print("Après l'ajout de livres :")
bibliotheque.Emprunter_un_livre(membre1, livre1)
# bibliotheque.Emprunter_un_livre(membre2, livre1)

print("Après l'emprinte de livres :")
bibliotheque.Retirer_un_livre(livre1)
# # bibliotheque.Retirer_un_livre(livre2)

print("Retour des livres :")
bibliotheque.Retourner_un_livre(membre1, livre1)
# # bibliotheque.Retourner_un_livre(livre2)





    