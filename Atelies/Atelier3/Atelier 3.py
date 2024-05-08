# Activité 1
def somme_pairs(liste):
    sum=0
    for i in liste:
        if i%2==0:
            sum+=i
    return sum
###### test ########
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
S = somme_pairs(L)
print("La somme des nombres pairs dans la liste L est :",S)

# Activité 2
def calculer_aire_rectangle(longueur,largeur):
    return longueur*largeur

def calculer_perimetre_rectangle(longueur,largeur):
    return 2*(longueur+largeur)
####### test ########
Air_rectng = calculer_aire_rectangle(15,7)
Perm_rectg = calculer_perimetre_rectangle(20,6)
print("l'aire du rectangle est :".format(), Air_rectng)
print("l'aire du rectangle est :".format(), Perm_rectg)

# Activité 3

# intitialisation de la base de données
donnes_eleves = {
    'Nom': '',
    'Age': '',
    'Taille': ''
}

def remplissage(Nom_eleve, age_eleve, taille_eleve):
    donnes_eleves['Nom'] = Nom_eleve
    donnes_eleves['Age'] = age_eleve
    donnes_eleves['Taille'] = taille_eleve

def consultation(Nom):
    # Vérifier si le nom existe dans les données des élèves
    if Nom in donnes_eleves['Nom']:
        age = donnes_eleves['Age']
        taille = donnes_eleves['Taille']
        return "L'élève {} existe dans la base de données, voici ses coordonnées : {} ans, {} m".format(Nom, age, taille)
       # return (age, taille)
    else:
        return "L'élève {} non trouvé.".format(Nom)
    


##### test ##### 
remplissage('Mohamed', 26, 1.8)
print(consultation('Mohamed'))  
print(consultation('Younes'))    

# Activité 4

def mediane(liste):
    L = sorted(liste)  
    L_len = len(L)     
    if L_len < 1:      
        return None 
    if L_len % 2 != 0: 
        return L[L_len // 2]# longueur impaire
    else:      
        return (L[L_len // 2 - 1] + L[L_len // 2]) / 2.0 # Longueur paire

###### test
l0 = []
l1 = [1,5,3,2,4]
l2 = [0,2,3,1,5,4]
print ("la médiane de la liste est : ",mediane(l0))

# Activité 5
# a

def inversion_mots(liste):
    list_inver = []
    for mot in liste:
        list_inver.append(mot[::-1])
    return list_inver

def mot_palindrome(liste):
    palindromes = []
    for mot in liste:
        if mot == mot[::-1]:
            palindromes.append(mot)
    return palindromes


# # ###### test1
L = ["hello", "Bonjour"]
print(inversion_mots(L))
# ###### test2
List_mots = ["radar", "bonjour", "ressasser", "kayak", "python"]
print(mot_palindrome(List_mots))

# Activité 6
def calculatrice(a, b, char):
    if char == '+':
        return lambda: a+b
    elif char == '-':
        return lambda: a-b
    elif char == '*':
        return lambda: a*b
    elif char == '/':
        return lambda: a/b
    else:
        print("Opération invalide")

# Test
resultat_calcul = calculatrice(2, 3, '*')
print("Le resultat de calcul est ",resultat_calcul())
















