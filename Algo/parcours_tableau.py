
L1=[1,2,3,4,5,6,7]
for i in range(len(L1)):
    if L1[i]%2==0:
        print("algorithme afin de n’afficher que les nombres pairs : ",L1[i])

L2=["à côté", "à droite", "à gauche", "au milieu", "au-delà", "audessous", "au-dessus", "debout", "dedans", "dehors", "en bas", "enface", "en haut", "loin", "près", "tard", "tôt"]
i=0
mot=str(input("Quel mot cherchez-vous ?"))

while L2[i]!=mot and i<len(L2):
    i+=1
if i == len(L2):
    print("Le mot n’est pas présent dans la liste.")
else:
    print("Le mot est présent dans la liste.")


