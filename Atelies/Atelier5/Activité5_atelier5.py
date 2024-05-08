import tkinter as tk

#Activité 5 

class Contact():
    def __init__(self, nom :str, numéro_de_téléphone :str) :
        self.nom=nom
        self.numéro_de_téléphone = numéro_de_téléphone
    def Affiche_Contact(self):
        print("\nNom : ", self.nom)
        print("Numéro téléphone : ", self.numéro_de_téléphone)
        

class CarnetAdresses():
    
    def __init__(self):
        self.liste_de_contacts = []  

    def Ajouter_un_contact(self, contact):
        self.liste_de_contacts.append(contact)

    def recuperer_liste_contacts(self):
        return self.liste_de_contacts
               
# contact1 = Contact("Anas", "0753762897")
# contact2 = Contact("Mohamed", "0624789900")
# contact3 = Contact("Karim", "0757762890")
# contact4 = Contact("Meryem", "0731762807")

# carnet =CarnetAdresses()

# carnet.Ajouter_un_contact(contact1)
# carnet.Ajouter_un_contact(contact2)
# carnet.Ajouter_un_contact(contact3)
# carnet.Ajouter_un_contact(contact4)

# # Afficher la liste des contacts
# liste_contacts = carnet.recuperer_liste_contacts()
# for contact in liste_contacts:
#     contact.Affiche_Contact()

def ajouter_contact():
    carnet =CarnetAdresses()
    c = Contact(nom.get(), numero_telephone.get())
    carnet.Ajouter_un_contact(c)
    # Efface le contenu actuel de la zone de texte
    # zone_texte.delete('1.0', tk.END)
    # Ajoute tous les contacts dans la zone de texte
    for contact in carnet.recuperer_liste_contacts():
        zone_texte.insert(tk.END, "Nom : " + contact.nom + "\n")
        zone_texte.insert(tk.END, "Numéro de téléphone : " + contact.numéro_de_téléphone + "\n\n")
    # Efface les champs de saisie
    nom.delete(0, tk.END)
    numero_telephone.delete(0, tk.END)
    # Met le focus sur le champ "nom"
    nom.focus_set()

# Créer une fenêtre Tkinter
window = tk.Tk()
window.title("Carnet d'Adresse")

# Couleur de fond pour la fenêtre
window.configure(bg="#2176C1")

# Créer un label pour afficher le nom et numéro téléphone
label1 = tk.Label(window, text="Nom :", bg="#2176C1", fg='white', font = ('Arial Black' , 12))
label1.pack()
# Création des champs de saisie
nom = tk.Entry(window)
label2 = tk.Label(window, text="Numéro de téléphone :", bg="#2176C1", fg='white', font = ('Arial Black' , 12))
label2.pack()
numero_telephone = tk.Entry(window)


nom.pack()
numero_telephone.pack()
# Place automatiquement le curseur dans le champ "nom" au lancement de l'application
nom.focus_set()

# Créer un bouton Ajouter
button = tk.Button(window, text="Ajouter", command=ajouter_contact, bg = "#6FAFE7" , fg = "black" , font = ('Arial' , 10))
button.pack()

# Création de la zone de texte
zone_texte = tk.Text(window)
zone_texte.pack()


# Lancer la boucle principale de l'application
window.mainloop()


