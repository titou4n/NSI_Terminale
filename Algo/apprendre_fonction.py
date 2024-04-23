import random

# fontion qui renvoi la puissance n d'un nombre x

def puissance(x,n):
    '''
    Renvoi la valeur de x puissance n
    x un flot ou int et n un nombre entier positif
    Renvoie  la valeur en float ou int

    '''
    r=1
    for i in range(n):
        r=r*x
    return r

def test():
    for i in range(100):
        #x=random.randint(0,9)
        #n=random.randint(0,9)
        x=i
        n=i
        print(x, " puissance ", n, " = ",puissance(x,n))


print(puissance(2,3))
print(puissance(0.5,2))
print(puissance(-2,5))
print(puissance(2,-3))
#print(puissance(4,1/2))


def dire_bonjour():
    print("Bonjour à tous !!!!!!!!!!!!!!!!!!!!!!!!!")

dire_bonjour()

var=dire_bonjour()
print(var)

#Bilan: affiche juste le string elle ne prent aucun argument en entrée et ne renvoi rien
#si on essai de recuperer le texte affiché dans une variables Python affecte la valeur None a la variable; ce n'est pas une faute car Python n'émet pas d'erreur, cepandant cela n'a pas d'interet.
#la solution est d'utiliser return dans la fonction pour pouvoir récuperer la valeur sous forme d'une variable

#Ex 2

prenom="Titouan"

def dire_bonjour_prenom1(prenom):
    '''met un nom stp'''
    return("Bonjour", prenom, " !!!!!!!!!!!!!!!!!!!!!!!!!")

a,b,c = dire_bonjour_prenom1(prenom)
print(a,b,c)

def dire_bonjour_prenom2(prenom):
    '''met un nom stp'''
    print("Bonjour", prenom, " !!!!!!!!!!!!!!!!!!!!!!!!!")
dire_bonjour_prenom2(prenom)



#Ex 3

def compteur(debut,stop, cpt):
    i = debut
    while i <= stop:
        print(i)
        i = i + cpt

print(compteur(1,10,2))

#voila ce qu'elle affiche
#1
#3
#5
#7
#9
#None

#Ex 4

def fct(x=1):
    return x

print(fct())

def se_presenter(prenom,nom="Martin"):
    return(prenom,nom)

a,b = se_presenter("Jean")
print("Bonjour ", a ,". Mon nom est ", b , " !")
c,d = se_presenter("Jean", "Brassard")
print("Bonjour ", c ,". Mon nom est ", d , " !")

#Bonjour  Jean . Mon nom est  Martin  !
#Bonjour  Jean . Mon nom est  Brassard  !

#Application 1

def fct_1():
    print("La fonction fct_1 affiche : i = ",i , " et j = ", j)

i=1
j=2
fct_1()
#La fonction fct_1 affiche : i =  1  et j =  2

#Application 2

def fct_2(i,j):
    i = 33
    print("La fonction fct_2 affiche : i = ",i , " et j = ", j)

i=1
j=2
fct_2(16,87)
print("i = ", i, " et j = ", j)

#La fonction fct_2 affiche : i =  33  et j =  87
#i =  1  et j =  2

#Application 3

def fct_3():
    global i
    i = 947
    j = 5
    print("La fonction fct_3 affiche : i = ",i , " et j = ", j)

i=1
j=2
fct_3()
print("i et j après fct_3 : i = ", i, " et j = ", j)

#La fonction fct_3 affiche : i =  947  et j =  5
#i et j après fct_3 : i =  947  et j =  2


#III)Les fonctions prédéfinies :

liste=(9,6,8,-3,0,2,6,33,-4)

def min(liste):
    '''
    Fonction qui recherche le minimum d’une liste
    min(liste)
    '''
    i=0
    r = liste[0]
    for i in range(len(liste)):
        if liste[i] <r:
            r=liste[i]
            i=i+1
        else:
            i=i+1
    return r

def max(liste):
    '''
    Fonction qui recherche le maximum d’une liste
    max(liste)
    '''
    i=0
    r = liste[0]
    for i in range(len(liste)):
        if liste[i] > r:
            r=liste[i]
            i=i+1
        else:
            i=i+1
    return r




