class Emploiye():
    #Atributs statiques
    nombre_emploiyes = 100 
    augmentation_salaire = 0
    # @staticmethod
    # def augment_salaire(self)->None:
    #     Emploiye.augmentation_salaire+=5

    def __init__(self, Nom, Salaire_de_base):
        self.Nom =Nom
        self.Salaire_de_base=Salaire_de_base
        Emploiye.augmentation_salaire+=5
     
        # Emploiye.augment_salaire()
    def afficher_informations(self, Emploiye):
        print(f"Nom de l'emploiyé : ", Emploiye.Nom)
        print("Salaire de base: ", Emploiye.Salaire_de_base)
        Salaire_apres_augmentation = Emploiye.Salaire_de_base + (Emploiye.Salaire_de_base*(self.augmentation_salaire)/100)
        print(f"Salaire de {Emploiye.Nom} après l'augmentation : {Salaire_apres_augmentation} £")


# print(Emploiye.augmentation_salaire)
# print(Emploiye.afficher_informations())
emploiye=Emploiye("Mohammed", 3000)
emploiye.afficher_informations(emploiye)
