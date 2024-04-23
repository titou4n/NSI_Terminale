#Exercice 1:

def nbr_multiplier_par_4(a):
    '''
    Renvoie la valeur de a*4, un int ou un float
    a doit etre un int ou un float
    '''
    return a*4

#Exercice 2:

def ajoute_1(n):
    assert n!=int or n!=float, "Le nombre doit etre un entier ou un flotant"
    return n+1

assert ajoute_1(2)==3
assert ajoute_1(-1)==0
assert ajoute_1(0)==1
assert ajoute_1(0.0)==1
assert ajoute_1(0.4)==1.4
assert ajoute_1(-6.5)==-5.5


#Exercice 3:

def prod_scal(x_vecteur_u, y_vecteur_u, x_vecteur_v, y_vecteur_v):
    '''
    prod_scal renvoi le produit scalaire de deux vecteurs, un int or float 
    prod_scal(x_vecteur_u, y_vecteur_u, x_vecteur_v, y_vecteur_v)
    4 arguments:
    x_vecteur_u -> coordonnées x du vecteur u, int or float
    y_vecteur_u -> coordonnées y du vecteur u, int or float
    x_vecteur_v -> coordonnées x du vecteur v, int or float
    y_vecteur_v -> coordonnées y du vecteur v, int or float
    '''
    assert x_vecteur_u!=int or x_vecteur_u!=float, "x_vecteur_u doit etre un entier ou un flotant"
    assert y_vecteur_u!=int or y_vecteur_u!=float, "y_vecteur_u doit etre un entier ou un flotant"
    assert x_vecteur_v!=int or x_vecteur_v!=float, "x_vecteur_v doit etre un entier ou un flotant"
    assert x_vecteur_v!=int or x_vecteur_v!=float, "x_vecteur_v doit etre un entier ou un flotant"
    return (x_vecteur_u*x_vecteur_v)+(y_vecteur_u*y_vecteur_v)

assert prod_scal(1, 2, 3, 4)==11
assert prod_scal(-1, 2, 3, 4)==5
assert prod_scal(-1, 2, -2, 4)==10
assert prod_scal(-10, -2, 2, 4)==-28
assert prod_scal(0, 2, -2, 0)==0
assert prod_scal(0, 2, 6, 4)==8
assert prod_scal(1.5, 2, 2, 1.5)==6
assert prod_scal(1.5, 2, -2, 1.5)==0




def orthogon(x_vecteur_u, y_vecteur_u, x_vecteur_v, y_vecteur_v):
    '''
    orthogon determine si deux vecteurs sont othogonaux.
    Si orthogon renvoie le booléen True alors les deux vecteurs sont othogonaux.
    Et si orthogon renvoie le booléen False alors les deux vecteurs ne sont pas othogonaux.
    orthogon(x_vecteur_u, y_vecteur_u, x_vecteur_v, y_vecteur_v)
    4 arguments:
    x_vecteur_u -> coordonnées x du vecteur u, int or float
    y_vecteur_u -> coordonnées y du vecteur u, int or float
    x_vecteur_v -> coordonnées x du vecteur v, int or float
    y_vecteur_v -> coordonnées y du vecteur v, int or float
    '''
    assert x_vecteur_u!=int or x_vecteur_u!=float, "x_vecteur_u doit etre un entier ou un flotant"
    assert y_vecteur_u!=int or y_vecteur_u!=float, "y_vecteur_u doit etre un entier ou un flotant"
    assert x_vecteur_v!=int or x_vecteur_v!=float, "x_vecteur_v doit etre un entier ou un flotant"
    assert x_vecteur_v!=int or x_vecteur_v!=float, "x_vecteur_v doit etre un entier ou un flotant"
    P=False
    if prod_scal(x_vecteur_u, y_vecteur_u, x_vecteur_v, y_vecteur_v)==0:
        P=True
    return P

assert orthogon(0, 3, 26, 0)==True
assert orthogon(0, 3, 26, 1)==False
assert orthogon(0, 2, -2, 0)==True
assert orthogon(0, 2.255, -2, 0)==True
assert orthogon(4, 3, 26, 1)==False





