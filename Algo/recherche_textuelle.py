mot = "ABRACADABRA"
recherche = "BRA"

def occurrences(mot, recherche):
    liste_mot = []
    occurrences = 0
    position = []
    for i in range(len(mot)-2):
        liste_mot.append(mot[i]+mot[i+1]+mot[i+2])
    for i in range(len(liste_mot)-2):
        if liste_mot[i] == recherche:
            occurrences +=1
            position.append(str(i)+str(i+1)+str(i+1))
    return position, occurrences

print(occurrences(mot, recherche))


def fn_position(mot, recherche):
    liste_mot = []
    position = []
    for i in range(2, len(mot)-1):
        a = str(mot[i-1])+str(mot[i])+str(mot[i+1])
        if a == recherche:
            #position.append(str(i-1)+str(i)+str(i+1))
            position.append(a)
    return position

#print(fn_position(mot, recherche))


t = "ABRACdsftbvhBRfyrgsyabracadabragdDABRABRACdsftbvhBRfyrgsygdDABABRAABRABRACdsftbvabracadabrahBRfyrgsygdDABABRABRABRACdsftbvhBRfyrgsygdDabracadabraABABRACdACdCdsABRACdsftbvhBRfyrgsygdDABRAftbvhBRfyrgsygdDABRARAABRACdsftbABRACdABRACdsftbvhBRfyrgsygdDABRAsftbvhBRfyrgsygdDABRAvhBRfyrgsygdDABRAABRACdsftbvhBRfyrgsygdDABRAA"
m = "abracadabra"


'''
def occurrence(m, t, i):
    if i < 0 or i > len(t)-len(m):
        return False
    for j in range(0, len(m)):
        if m[j]!=t[i+j]:
            return False
    return True

def recherche_v2(m, t):
    for i in range(0, len(t)-len(m)+1):
        if occurrence(m, t, i):
            print('occurrence à la position : ', i)

print(recherche_v2(m, t))
'''

def table_bm(m):
    dictionnaire = [{} for i in range(len(m))]
    for j in range(len(m)):
        for k in range(j):
            dictionnaire[j][m[k]]=k
    return dictionnaire


print(table_bm(m))