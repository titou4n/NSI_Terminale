T_1 = [8,3,11,7,9,2]
T_2 = [8,3,11,7,9,2]
i = 0
j = len(T)-1

def echange(T, i, j):
    T[i], T[j] =  T[j],T[i]
    return T[i], T[j]


def tri_par_selection(T):
    len_t = len(T)
    for i in range(len_t):
        print(T)
        min = i
        for j in range(i+1, len_t):
            if T[min] > T[j]:
                min = j
            else:
                pass
        if min != i:
            echange(T, i, min)
        else:
            pass
    return T

print(tri_par_selection(T_1))
print(T_1)


def tri_par_insertion(T):
    for i in range(len_t):
        indice_i = i
        valeur = T[i]
        while i > 0:
            if T[indice_i -1]>valeur:
                T[indice_i], T[indice_i-1] = T[indice_i-1], T[indice_i]
            i = i-1
    return T

print(tri_par_insertion(T_2))
print(T_2)