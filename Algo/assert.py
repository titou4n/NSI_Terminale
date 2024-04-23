def indice_maxi_tab(T) :
    '''
    Renvoie l'indice de la première occurrence de la valeur 
    maximale de la liste T. T est supposé non vide.
    '''
    valeur_max = T[0]
    indice = 0
    for i in range(len(T)) :
         if T[i] > valeur_max :
            indice = i
            valeur_max = T[i]
    return indice

assert indice_maxi_tab([4, 3, 2, 1]) == 0
assert indice_maxi_tab([4, 5, 3, 2]) == 1
assert indice_maxi_tab([1, 2, 3, 6]) == 3
assert indice_maxi_tab([3, 2, 5, 2]) == 2
assert indice_maxi_tab([1, 1, 1, 1]) == 0
assert indice_maxi_tab([-30, 5, 2, 1]) == 1

#Exercice 1:

def multiplication(a, b):
    '''
    Renvoie le produit de a par b, 
    où a et b sont deux nombres quelconques.
    '''
    return a * b

assert multiplication(4, 3) == 12
assert multiplication(4, 0) == 0
assert multiplication(0, 4) == 0
assert multiplication(4, 4) == 16
assert multiplication(0, 0) == 0
assert multiplication(-4, -3) == 12
assert multiplication(-4, -0) == 0
assert multiplication(-0, -4) == 0
assert multiplication(-4, -4) == 16
assert multiplication(-0, -0) == 0
assert multiplication(4, -3) == -12
assert multiplication(4, -0) == 0
assert multiplication(0, -4) == 0
assert multiplication(4, -4) == -16
assert multiplication(0, -0) == 0
assert multiplication(-4, 3) == -12
assert multiplication(-4, 0) == 0
assert multiplication(-0, 4) == 0
assert multiplication(-4, 4) == -16
assert multiplication(-0, 0) == 0

assert multiplication(4.0, 3) == 12


#assert multiplication(4.2, 3) == 12.6


def somme(t):
    '''
    Renvoie la somme des éléments du tableau t, 
    t étant un tableau de nombres
    '''
    s = 0
    for i in range(len(t)):
        s = s + t[i]
    return s


assert somme([4, 3]) == 7
assert somme([1, 1, 1, 1]) == 4
assert somme([-30, 5, 2, 1]) == -22

def est_croissant(t):
    for i in range(len(t)-1):
        if t[i+1] < t[i]:
            return False
    return True

assert est_croissant([1,2,73,4,5.5])==False
assert est_croissant([1,2,3,5])==True
assert est_croissant([])==True