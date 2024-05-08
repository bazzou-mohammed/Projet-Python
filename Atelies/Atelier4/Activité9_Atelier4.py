from abc import ABC, abstractmethod
from math import pi
#classe abstraite 
class Forme(ABC):
    # methode abstraite
    @abstractmethod
    def calculer_surface(self):
        pass
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon=rayon
    def calculer_surface(self):
        print(f"La surface du cercle de rayon {self.rayon} est: {pi*self.rayon**2} cm^2") 
class Rectangle(Forme):
    def __init__(self, longeur, largeur):
        self.longeur=longeur
        self.largeur=largeur
    def calculer_surface(self):
        print(f"La surface du rectangle de longeur {self.longeur} et de largeur {self.largeur} est : {self.longeur*self.largeur} cm^2")
        
    
cercle = Cercle(2)
rectangle = Rectangle(14, 8)
cercle.calculer_surface()
rectangle.calculer_surface()





                 
