import subprocess

# Créer un fichier sous linux 
def create_file(file_name):
   try:
     subprocess.run(['touch', file_name], check=True)
     print(f"Le fichier {file_name} a été créé.")
   except subprocess.CalledProcessError:
     print(f"Erreur : Impossible de créer le fichier {file_name}.")

# Lister les fichiers d'un répértoire sous linux 
def list_files():
    try:
      result = subprocess.run(['ls'], stdout=subprocess.PIPE, text=True, check=True)
      file_list = result.stdout.split('\n')
      file_list = [file.strip() for file in file_list if file.strip()]
      print("Liste des fichiers dans le répertoire courant :")
      print(file_list)
      return file_list
    except subprocess.CalledProcessError:
     print("Erreur : Impossible de lister les fichiers.")

# Supprimer un fichier sous linux 
def delete_file(file_name):
     try:
       subprocess.run(['rm', file_name], check=True)
       print(f"Le fichier {file_name} a été supprimé.")
     except subprocess.CalledProcessError:
      print(f"Erreur : Impossible de supprimer le fichier {file_name}.")

# Modifier dans un fichier sous linux 
def append_to_file(file_name, text):
    try:
      subprocess.run(['echo', text, '>>', file_name], shell=True, check=True)
      print(f"Le texte a été ajouté à {file_name}.")
    except subprocess.CalledProcessError:
     print(f"Erreur : Impossible d'ajouter du texte à {file_name}.")