class Calculatrice():
    def __init__(self, x,y) :
        self.x= x
        self.y =y
    # '+'
    def __add__(self, other):
        return Calculatrice(self.x+other.x, self.y+other.y)
     # '-'
    def __sub__(self,other):
        return Calculatrice(self.x-other.x, self.y-other.y)
        # '*'
    def __mul__(self,other):
        return Calculatrice(self.x*other.x, self.y*other.y)
            # '/'
    def __truediv__(self,other):
        return Calculatrice(self.x/other.x, self.y/other.y)
    # Méthodes avancées
    def puissance(self, other):
        return self.x**other.y
    def racine_carree(self):
        return self.x**0.5




Calc1 = Calculatrice(2,6)
Calc2 = Calculatrice(4,7)
#Surcharge de '+'
S = Calc1+Calc2
print(S.x, S.y)

#Surcharge de '-'
Sustr = Calc1-Calc2
print(Sustr.x, Sustr.y)

#Surcharge de '*'
mult = Calc1*Calc2
print(mult.x, mult.y)

#Surcharge de '/'
try:
  divis = Calc1/Calc2
  print(divis.x, divis.y)
except ZeroDivisionError:
    print("Erreur: Division par zéro")

# x^y
calc = Calculatrice(2,3)
x_puiss_y = calc.puissance(calc)
print(x_puiss_y)

# x^2
calc = Calculatrice(25, 4)
racine_carree_x = calc.racine_carree()
print(racine_carree_x)