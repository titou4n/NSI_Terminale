

#Exercice1
tab = [1, 5, 6, 9, 1, 2, 3, 7, 9, 8]

def indice_maxi(tab):
    maximum = tab[0]
    j = []
    for i in range(1, len(tab)):
        if maximum<tab[i]:
            maximum = tab[i]
    for i in range(0, len(tab)):
        if maximum == tab[i]:
            j.append(i)
    return maximum, j

print(indice_maxi(tab))

#Exercice2


pile = [-1, 0, 5, -3, 4, -6, 10, 9, -8]
def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

print(positif(pile))