#Exercice 1

def maximum_tableau(tab):
    '''
    Écrire la fonction maximum_tableau, prenant en paramètre un tableau non vide de nombres
    tab (de type list) et renvoyant le plus grand élément de ce tableau.
    '''
    assert type(tab) == list, "Erreur type"
    assert len(tab) != 0, "Liste vide"
    maximum = tab[0]
    for i in tab:
        if i > maximum :
            maximum = i
    return maximum

print(maximum_tableau([98, 12, 104, 23, 131, 9]))
print(maximum_tableau([-27, 24, -3, 15]))

#Exercice 2

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def bon_parenthesage(ch):
    """
    Renvoie un booléen indiquant si la chaîne ch 
    est bien parenthésée
    """
    p = Pile()
    for c in ch:
        if c == "(": 
            p.empiler(c)
        elif c == ")": 
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()
    
print(bon_parenthesage("((()())(()))"))
print(bon_parenthesage("())(()"))
print(bon_parenthesage("(())(()"))