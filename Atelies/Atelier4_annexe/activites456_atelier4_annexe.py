from datetime import date
# Activité 4
# classe de base personne
class Personne():
    def __init__(self, nom, prenom) :
        self.nom = nom
        self.prenom = prenom
    
        
# classe Ouvrier heritant de personne 
class Ouvrier(Personne):
    def __init__(self, nom, prenom , identifiant, poste):
        super().__init__(nom, prenom)
        self.identifiant=identifiant
        self.poste = poste

class Absence():
    def __init__(self, ouvrier,date_absence, raison):
        self.ouvrier=ouvrier
        self.date_absence = date_absence
        self.raison=raison

    def afficher_absence(self):
        print(f"Absence de {self.ouvrier.nom} {self.ouvrier.prenom}")
        print(f"Identifiant : {self.ouvrier.identifiant} ")
        print(f"Date : {self.date_absence} ")

# Activité 5
class Horaire():
    def __init__(self, debut_journnee, fin_journnee):
        self.debut_journnee =  debut_journnee
        self.fin_journnee = fin_journnee


class HoraireFlexible(Horaire):
    def __init__(self, debut_journnee, fin_journnee, debut_plage, fin_plage):
        super().__init__(debut_journnee, fin_journnee)
        self.debut_plage = debut_plage
        self.fin_plage = fin_plage

    def Afficher_horaire(self):
        print(f"Horaires standard: de {self.debut_journnee} à {self.fin_journnee}")
        print(f"Plage horaire flexible : de {self.debut_plage} à {self.fin_plage}")    

#Activité : 6
class Equipe():
    def __init__(self, chef_equipe):
        self.chef_equipe  = chef_equipe
        self.ouvriers = []

    def ajouter_ouvrier(self, ouvrier):
        self.ouvriers.append(ouvrier)

    def enregister_absence(self, ouvrier, date_absence, raison):
        if ouvrier in self.ouvriers:
            self.chef_equipe.ajouter_absence(ouvrier, date_absence, raison)
        else:
            print("L'ouvrier n'appartient pas à cette équipe")


class Ouvrier():
    def __init__(self, nom, prenom, identifiant, role):
        self.nom  =nom
        self.prenom = prenom
        self.identifiant = identifiant
        self.role = role

class ChefEquipe(Ouvrier):
    def __init__(self, nom, prenom, identifiant, role):
        super().__init__(nom, prenom, identifiant, role)
        self.absences = []
    def ajouter_absence(self, ouvrier, date_absence, raison):
        self.absences.append((ouvrier, date_absence, raison))

    def Afficher_absence(self):
        for absence in self.absences:
            ouverier, date_absence, raison = absence
            print(f"{ouverier.nom} {ouverier.prenom} était absent le {date_absence} pour raison {raison}")

# Combiner tous les trois parties dans un seul main 
class Main:
      # fonction test absence 
      def test_absence(self):
        ouvrier = Ouvrier("Karim", "zeribi", 134567, "technicien") 
        absence = Absence(ouvrier, "15-04-2024", "maladie") 
        absence.afficher_absence()

      # test Horaires flixibles :
      def test_horaires_flexibles(self):
        horaires_flexibles =HoraireFlexible("9h00","17h00", "10h00","19h30")
        horaires_flexibles.Afficher_horaire() 

      # Fonction test gastion equipe
      def test_gestion_equipes(self):
        chef = ChefEquipe("jordan", "bardea", 23445, "Chef d'équipe")
        equipe = Equipe(chef)
    
        ouvrier1 = Ouvrier("karim", "belhabib", 5678, 'Ouvrier')
        ouvrier2 = Ouvrier("Ahmed", "keroumi", 2341, 'Ouvrier')

        equipe.ajouter_ouvrier(ouvrier1)
        equipe.ajouter_ouvrier(ouvrier2)

        equipe.enregister_absence(ouvrier1, date(2024, 4 ,14), "Maladie")
        equipe.enregister_absence(ouvrier2, date(2024, 5 ,21), "Congé familial")
        chef.Afficher_absence()

#Execution des trois tests
if __name__ == "__main__":
    main = Main()
    main.test_absence()
    main.test_horaires_flexibles() 
    main.test_gestion_equipes() 