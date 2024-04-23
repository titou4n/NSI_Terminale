def puissance(x,n):
    '''
    Renvoi la valeur de x puissance n
    '''
    assert type(x) == int and n >= 0, "n doit être un entier positif"
    assert type(x)==int or type(x)==float, "x doit etre un nbr"
    r=1
    for i in range(n):
        r=r*x
    return r


def indice_maxi_tab(T):
    """
    Renvoie l'indice de la première occurence de la valeur 
    maximale du tableau T. T est supposé non vide.
    """
    assert (type(T)==list or type(T)==tuple) and len(T)!=0, "T doit être une liste ou un tuple non vide"
    for i in T:
        assert type(i)==float or type(i)==int, "les élements doivent être des nbrs"


def quotient(a, b):
    '''
    Renvoie la valeur du quotient de a par b, b étant non nul.
    '''
    assert a==None and b==None, "a or b are required"
    assert b==0, "b can't be nul"


T=[1,3.2,6,8,-6,9,198,999.999]
print(puissance(-2,8))
print(indice_maxi_tab(T))
print(quotient(9))

