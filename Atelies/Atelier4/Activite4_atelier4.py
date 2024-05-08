class CompteBancaire():
    def __init__(self, Nom, Solde) :
        self.__Nom = Nom
        self.__Solde = Solde
    def deposer(self, montant):
        self.__Solde+= montant
        print(f"le montant {montant}£ a été ajouté avec succès au compte de M.{self.__Nom} ")
    def retirer(self, montant):
        if self.__Solde>=montant:
            self.__Solde-=montant
            print(f"le montant {montant}£ a été debité du compte de M.{self.__Nom} ")
        else:
            print("solde insuffisant")
    def consulter_solde(self):
        print(f"Votre solde actuel est {self.__Solde} £")
    

compte = CompteBancaire("bazzou mohammed", 0)
print("######## Déposer un montant sur mon compte ######## ")
mont = int(input("Donnez le montant à déposer: "))
compte.deposer(mont)
print("######## consulter le solde de mon compte ######## ")
compte.consulter_solde()
print("######## Retrait d'un montant de mon compte ######## ")
mont = int(input("Donnez le montant à retirer: "))
compte.retirer(mont)
print("######## consulter le solde de mon compte ######## ")
compte.consulter_solde()
        