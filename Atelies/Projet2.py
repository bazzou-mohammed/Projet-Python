import subprocess
from datetime import datetime

repertoire_temp = r'C:\Users\user\Desktop\Python\Atelies\Temp'

def supprimer_fichiers_temp(repertoire_temp):
    try:
        subprocess.run(['rm', '-rf', repertoire_temp], check=True)
        print(f"Le répertoire {repertoire_temp} a été supprimé.")
    except subprocess.CalledProcessError:
        print(f"Erreur : Impossible de supprimer le répertoire {repertoire_temp}.")

        
             

    
      
  