# Créé par simon1, le 25/03/2024 en Python 3.7

mot = "INFORMATIQUE"
mot_a_trous = "************"
def correspond(mot, mot_a_trous):
    if  len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot)):
        if mot[i] != mot_a_trous[i]:
            if mot_a_trous[i] != "*":
                return False
    return True

#print(correspond(mot, mot_a_trous))



def est_cyclique(plan):
    ex = 'A'
    des = plan[ex]
    nb_des = 1
    while des != ex :
        des = plan[des]
        nb_des = nb_des +1
    return nb_des == len(plan)

plan = {'A':'E', 'E':'F', 'F':'A'}

print(est_cyclique(plan))