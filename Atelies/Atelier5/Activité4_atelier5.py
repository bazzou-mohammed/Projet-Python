import tkinter as tk

# Fonction pour incrémenter le compteur et mettre à jour le label
def increment_counter():
    global counter
    counter += 1
    label.config(text="Compteur : " + str(counter))

# fenêtre Tkinter
window = tk.Tk()
window.title("Application compteur")

# Initialisation du compteur
counter = 0

# Création d'une label pour afficher le compteur
label = tk.Label(window, text="Compteur : " + str(counter))
label.pack()

# Créer un bouton pour incrémenter le compteur
button = tk.Button(window, text="Cliquez ici", command=increment_counter)
button.pack()

# Lancer la boucle principale de l'application
window.mainloop()
