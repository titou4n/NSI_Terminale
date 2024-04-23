

'''
v=9

def recherche_dichotomique(T, v):
    g = 0
    d = len(T)-1
    while g <= d:
        m = (g+d)//2
        if T[m] < v:
            g=m+1
        elif T[m] > v:
            d=m-1
        else:
            return m
    return None

g = 0
d = len(T)-1    
print(recherche_dichotomique(T, v))
#Question 1 : Quels sont les deux cas de base mettant fin aux appels récursifs ? Quelle valeur la fonction doit-elle renvoyer dans chaque cas ?
# None ou la position de v (m)
'''
'''
Question 2 : On note m = (g + d) // 2 l'élément central.
    • Quel appel récursif faut-il faire si l'élément central est strictement supérieur à v ? si élément central m > v : on retrecit notre liste par la droite jusqu'a m
    • Quel appel récursif faut-il faire si l'élément central est strictement inférieur à v ? si élément central m < v : on retrecit notre liste par la gauche jusqu'a m

Question 3 : On note toujours m = (g + d) // 2 l'élément central.
Ecrivez la fonction récursive recherche(T, v, g, d) qui renvoie une position de v dans T[g..d], ou None si v ne s'y trouve pas.

'''


'''
def recherche(T, v, g, d):
    """renvoie une position de v dans T[g..d], supposé trié,
    ou None si v ne s'y trouve pas"""
    m = (g+d)//2
    print("m = "+str(T[m]))
    print(T[g:d])
    if T[m]==v:
        return m
  
    if T[m] > v:
        d=m-1
        recherche(T, v, g, d)
    elif T[m] < v:
        g=m
        recherche(T, v, g, d)
    else:
        return m
    return None
    

print(recherche(T, v, g, d))


'''



T = [1, 2, 2, 5, 6, 6, 7, 9, 9, 10, 10, 13, 13, 15]
g = 0
d = len(T) - 1
v = int(input("Veuillez-entrer un nombre : "))
print(T[g:d + 1])

def recherche_dichotomique_recursivité(T, v, g, d):
    """renvoie une position de v dans T[g..d], supposé trié,
    ou None si v ne s'y trouve pas"""
    if g <= d:
        m = (g + d) // 2
        if T[m] > v:
            return recherche_dichotomique_recursivité(T, v, g, m - 1)
        elif T[m] < v:
            return recherche_dichotomique_recursivité(T, v, m + 1, d)
        else:
            return m
    return None

print(recherche_dichotomique_recursivité(T, v, g, d))

