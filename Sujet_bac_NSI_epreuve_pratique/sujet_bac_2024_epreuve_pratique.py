a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}

def fn_taille(arbre, lettre):
    #arbre[lettre]
    #print(arbre[lettre])
    #print(arbre[lettre][0])
    if arbre[lettre] != ['','']:
        if arbre[lettre][0] != None:
            taille = fn_taille(arbre[arbre[lettre][0]], arbre[lettre][0])
        elif arbre[lettre][1] != None:
            taille = fn_taille(arbre[arbre[lettre][1]], arbre[lettre][1])
    return taille

    
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N-1): 
        imin = k 
        for i in range(k+1, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin) 

tab = [41, 55, 21, 18, 12, 6, 25]
print(tri_selection(tab))