def distance(x_un, x_deux):
    return abs(x_un-x_deux)

def k_voisins(L,k,x):
    n=len(L)
    list_distance_indice = []
    for i in range(n):
        d = distance(x, L[i])
        list_distance_indice.append([d,i])
    list_distance_indice.sort()
    voisins = []
    for i in range(k):
        voisins.append(list_distance_indice[i][1])
    return voisins

def predire_classe(L, classes, k, x):
    '''
    L est la liste de tous les abcisses des voisins
    classes est la liste de la classe de tous les voisins
    k est le nbr de voisins
    x est l'abcsisse donné afin de trouver et de prédire les voisins les plus proches
    '''
    assert type(L)==list, "Le type de L doit etre une liste"
    assert type(classes)==list, "Le type de classe doit etre une liste"
    assert type(x)==float or type(x)==int, "Le type de x doit etre un float"
    x = float(x)
    voisins = k_voisins(L,k,x)
    classes_possibles = ['C','T']
    decompte = [0,0]
    for v in range(len(L)):
        if classes[v] == 'C':
            decompte[0] += 1
        else:
            decompte[1] += 1
    if decompte[0]<decompte[1]:
        classes_possibles='T'
    else:
        classes_possibles='C'
    return classes_possibles

#k est le nbr de voisins
#L = [0.5, 1.0, 2.0, 3.8, 5.2, 6.0, 7.0]
L = [0.5, 1.0, 2.0, 3.8, 5.2, 6.0]
#classes = ['T','C','C', 'T', 'T','C', 'C']
classes = ['T','C','C', 'T']
k=3
x=3.0
print("La classe prédit :",predire_classe(L, classes, k, x))

