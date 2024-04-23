#Sujet 16

#EXERCICE 1 (4 points)

def recherche_indices_classement(elt:int, tab:list):
    '''
    Écrire une fonction recherche_indices_classement qui prend en paramètres un
    entier elt et une liste d’entiers tab, et qui renvoie trois listes :
        - la première liste contient les indices des valeurs de la liste tab strictement inférieures à elt ;
        - la deuxième liste contient les indices des valeurs de la liste tab égales à elt ;
        - la troisième liste contient les indices des valeurs de la liste tab strictement supérieures à elt.
    '''
    liste_1 = []
    liste_2 = []
    liste_3 = []
    for i in range(len(tab)):
        if tab[i] < elt:
            liste_1.append(i)
        elif tab[i] == elt:
            liste_2.append(i)
        else:
            liste_3.append(i)
    return (liste_1, liste_2, liste_3)


print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
#([0, 3, 7], [1, 6], [2, 4, 5])
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))
#([0, 2, 5], [], [1, 3, 4])
print(recherche_indices_classement(3, [1, 1, 1, 1]))
#([0, 1, 2, 3], [], [])
print(recherche_indices_classement(3, []))
#([], [], [])

#EXERCICE 2 (4 points)

resultats = {
    'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [13, 4],
        'PROJET1': [16, 3],
        'DS3': [14, 4]
        },
    'Durand': {
        'DS1': [6 , 4],
        'DM1': [14.5, 1],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [8, 4],
        'DS4':[15, 4]
        }
    }

def moyenne(nom, dico_result):
    if nom in dico_result.keys():
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points/total_coefficients, 1)
    else:
        return -1

for i in resultats:
    print(f"moyenne de {i} = {moyenne(str(i), dico_result=resultats)}")


#Sujet 17 2 / 3

#EXERCICE 1 (4 points)

liste_notes = [(15, 2), (9, 1), (12, 3)]
def moyenne(liste_notes):
    total_points = 0
    total_coefficients = 0
    for i in range(len(liste_notes)):
        point = liste_notes[i][0]*liste_notes[i][1]
        total_points = total_points + point
        total_coefficients = total_coefficients+liste_notes[i][1]
    return total_points/total_coefficients

print(moyenne(liste_notes))

#EXERCICE 2 (4 points)


def pascal(n):
    '''
    On cherche à déterminer les valeurs du triangle de Pascal (Figure 1).
    Dans le triangle de Pascal, chaque ligne commence et se termine par le nombre 1.
    Comme l’illustre la Figure 2, on additionne deux valeurs successives d’une ligne pour
    obtenir la valeur qui se situe sous la deuxième valeur.
    Figure 1 : triangle de Pascal Figure 2 : méthode de calcul
    Compléter la fonction pascal ci-après prenant en paramètre un entier n supérieur ou
    égal à 2. Cette fonction doit renvoyer une liste correspondant au triangle de Pascal de la
    ligne 0 à la ligne n. Le tableau représentant le triangle de Pascal sera contenu dans la
    variable triangle.
    '''
    triangle= [[1]]
    for k in range(1,n):
        ligne_k = [k]
        for i in range(1, k):
            ligne_k.append(triangle[k][i-1] + triangle[k][i])
        ligne_k.append(ligne_k)
        triangle.append(ligne_k)
    return triangle

print(pascal(4))
'''
pascal(4)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
Et pour n = 5, voici ce que l’on devra obtenir :
>> pascal(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],
[1, 5, 10, 10, 5, 1]]'''