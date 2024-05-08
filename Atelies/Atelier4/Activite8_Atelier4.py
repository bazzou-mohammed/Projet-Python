class Employe():
    def __init__(self, nom, salaire_de_base, annee_embauche):
        self.Nom = nom
        self.salaire_de_base = salaire_de_base
        self.anne_embauche = annee_embauche
    def calcul_salaire_annuel(self):
        return self.salaire_de_base*12

class Manager(Employe):
    def __init__(self, nom, salaire_de_base, annee_embauche, bonus):
        super().__init__(nom, salaire_de_base, annee_embauche)
        self.bonus = bonus
    def calcul_salaire_annuel(self):
        salaire_annuel_plus_bonus = super().calcul_salaire_annuel() + self.bonus
        print(f"Le salaire annuel de {self.Nom} avec bonus inclu :{salaire_annuel_plus_bonus} £")

class Developpeur(Employe):
    def __init__(self, nom, salaire_de_base, annee_embauche, langage):
        super().__init__(nom, salaire_de_base, annee_embauche)
        self.langage = langage
    def affiche_infos(self):
        print(f"Developpeur : {self.Nom}")
        print(f"Salaire de base : {self.salaire_de_base} £")
        print(f"Année d'embauche : {self.anne_embauche}")
        print(f"Langage : {self.langage}")

manager = Manager('karim zeribi', 5000, '2010', 10000)
developpeur = Developpeur("mohammed bazzou", 3500, '2015', 'Python')

manager.calcul_salaire_annuel()
developpeur.affiche_infos()