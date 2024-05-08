import subprocess
import os

def create_file(file_name):
    try:
        with open(file_name, 'w'):
            pass
        print(f"Le fichier {file_name} a été créé.")
    except Exception as e:
        print(f"Erreur : Impossible de créer le fichier {file_name}.")
        print(e)

def list_files():
    try:
        file_list = os.listdir('.')
        # print("Liste des fichiers dans le répertoire courant :")
        # print(file_list)
        return file_list
    except Exception as e:
        print("Erreur : Impossible de lister les fichiers.")
        print(e)

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"Le fichier {file_name} a été supprimé.")
    except Exception as e:
        print(f"Erreur : Impossible de supprimer le fichier {file_name}.")
        print(e)

def append_to_file(file_name, text):
    try:
        with open(file_name, 'a') as file:
            file.write(text + '\n')
        print(f"Le texte a été ajouté à {file_name}.")
    except Exception as e:
        print(f"Erreur : Impossible d'ajouter du texte à {file_name}.")
        print(e)

# Tests
create_file('test_file.txt')
file_list = list_files()
if file_list:
    delete_file(file_list[0])
    append_to_file(file_list[0], "Nouveau texte ajouté.")
    list_files()
