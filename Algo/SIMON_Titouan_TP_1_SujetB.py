#Exercice 1 :

for i in range(10):
    if i == 0 or i == 2 or i == 6 or i == 8 :
        print("-+-xxx   xxx-+-")
    elif i == 1 or i == 7 :
        print("#"*15)
    else:
        print("===|||||||||===")


#Exercice 2 :

liste = [1,8,9,6,55,105,5,2055,7,85]
tuple = ()

def retourn_le_plus_grand_element(liste):
    plus_grand_element = 0
    for i in range(len(liste)):
        plus_grand_element = liste[i]
        if plus_grand_element >= liste[i-1] or plus_grand_element >= liste[i+1]:
                return plus_grand_element, liste.index(plus_grand_element)


print(retourn_le_plus_grand_element(liste))