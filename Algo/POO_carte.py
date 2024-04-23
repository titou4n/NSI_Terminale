import random

class Carte:
    def __init__(self, c, v):
        """ Initialise les attributs couleur (entre 1 et 4), et
        valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v
    def get_valeur(self):
        """ Renvoie la valeur de la carte : As, 2, ..., 10,
        Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9',
        '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]
    def get_couleur(self):
        """ Renvoie la couleur de la carte (parmi pique, coeur,
        carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]
    
class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangés par valeurs croissantes en
        commençant par pique, puis coeur, carreau et trèfle. """
        self.contenu = [Carte(c,v)  for c in range(1,5)
                                        for v in range(1,14)]

    def get_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos
        (entier compris entre 0 et 51). """
        return self.contenu[pos]
    
    '''
    Exemple :
    >>> jeu = Paquet_de_cartes()
    >>> carte1 = jeu.get_carte(20)
    >>> print(carte1.get_valeur() + " de " + carte1.get_couleur())
    8 de coeur
    >>> carte2 = jeu.get_carte(0)
    >>> print(carte2.get_valeur() + " de " + carte2.get_couleur())
    As de pique
    >>> carte3 = jeu.get_carte(52)
    AssertionError : paramètre pos invalide
    '''



def tirage():
    jeu = Paquet_de_cartes()
    L = []
    while len(L)!=51:
        r = random.randint(0, 51)
        if r in L:
            pass
        else:
            carte = jeu.get_carte(r)
            L.append(r)
            print(carte.get_valeur() + " de " + carte.get_couleur())
    return L

def jeu():
    L = tirage()
    d = 0
    f = len(L)
    m = (d+f)//2
    J1 = L[0:m]
    J2 = L[m:f]
    print(L)
    print(J1)
    print(J2)
    print(len(J1))
    print(len(J2))
    carte_J1 = J1.pop(0)
    carte_J2 = J2.pop(0)

    while J1 != [] or J2 != []:
        carte_J1 = J1.pop(0)
        carte_J2 = J2.pop(0)
        print(f"{carte_J1} vs {carte_J2}")
        if carte_J1 < carte_J2:
            J2.append(carte_J1)
            J2.append(carte_J2)
        else:
            J1.append(carte_J1)
            J1.append(carte_J2)
    print("La partie est finie")






jeu()

