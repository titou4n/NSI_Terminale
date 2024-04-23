
"""
dico={}
dico["bit"] = "élement d'information allant de 0 à 1"
dico["processeur"] = "unité de calcul de l'ordinateur"
dico["RAM"] = "Mémoire vive"
print(type(dico["bit"]))
print(len(dico))

dicoHP = {}
dicoHP["dumbeldore"] = "Directeur de l'école poudlard"
dicoHP["Rogue"] = "Le meilleur !"
dicoHP["Gryffondor"] = "Premiere maison"

print("Merlin" in dicoHP)

dicoHP["Merlin"] = "test 1"
print("Merlin" in dicoHP)

del(dicoHP["Merlin"])
dicoHP["test 2"] = "Merlin"
print("Merlin" in dicoHP)

dicoHP2 ={}
dicoHP2["Merlin"] = "Merlin"
print("Merlin" in dicoHP2)
"""
"""
panier = {"ananas":1,"orange":1.5,"banane":4, "pomme":3, "prune":2 , "grappe raisin":1}
print(panier["orange"])
print(panier.keys())

l = []
for i in panier.keys():
    l.append(i)
print(l)

print("prune" in panier)
#print(panier["mangue"]) -> renvoit une erreur


"""
#exercice 2
'''
def ajoute_fruit(panier, fruit, quantite):
    if fruit in panier is False:
        panier[fruit] = quantite
    else:
        panier[fruit] = panier[fruit]+quantite
    return panier


print(panier.items())
fruit=str(input("fruit: "))
quantité=float(input("quatité: "))
ajoute_fruit(panier,fruit, quantité)
print(panier)
'''
#exercice 3
'''
parc = {}
for i in range(256):
    machine = "machine"+str(i)
    ip = "238.135.45."+str(i)
    parc[machine] = ip
for i in parc:
    print(str(i)+"     :   "+str(parc[i]))


parc={  "machine1":"238.135.45.26",
        "machine2":"238.135.45.27",
        "machine3":"238.135.45.28"
    }
print(parc.items())
print("238.135.45.30" in parc.values())
'''

#exercice 4
"""
dict_capitales={"France":"Paris",
                "Allemagne":"Berlin",
                "Portugal":"Lisbonne",
                "Espagne":"Madrid"
}


def verif_dict_capitales(capitale:str, dict_capitales:dict):
    if capitale in dict_capitales.values():
        for pays in dict_capitales:
            if dict_capitales[pays] == capitale:
                return pays
    else:
        ajoute_capitale(capitale, dict_capitales)

def ajoute_capitale(capitale:str, dict_capitales:dict):
    pays = str(input("Veuillez entrez le pays de la capitale : "))
    dict_capitales[pays] = capitale
    print("Le pays et la capitale associé ont bien été associé au dictionnaire .")

def recherche(capitale:str, dict_capitales:dict):
    dict_pays={}
    for (p,c) in dict_capitales.items():
        dict_pays[c] = p
    if capitale in dict_capitales.keys():
        return dict_pays[capitale]
    else:
        None


capitale = str(input("capitale : ")).strip().capitalize()
print("Pays  : "+verif_dict_capitales(capitale, dict_capitales))
print(dict_capitales)
"""

#Exercice5
"""
Exercice 5
On considère un dictionnaire personnes qui associe à des noms de personnes un dictionnaire contenant des informations personnelles :
1. Ecrire une fonction qui prend un nom de personne en paramètre et retourne son âge, ou None si la personne n’est pas dans le dictionnaire.
2. Ecrire une fonction qui calcule la taille moyenne des personnes dans le dictionnaire.
"""

personnes ={
    "Jean Aymar":{"taille":178,"pays":"USA","age":31},
    "Clio Patre":{"pays":"Portugal","age":32,"taille":179},
    "Mateo":{"pays":"France","age":32,"taille":175},
    "Sébastien":{"pays":"France","age":32,"taille":178},
    "Antonin":{"pays":"France","age":32,"taille":190},
    "Lucas":{"pays":"France","age":32,"taille":183},
    "Mr_Candapin":{"pays":"France","age":32,"taille":300},
    "Arthur":{"pays":"France","age":32,"taille":177},
    "Titouan":{"pays":"France","age":32,"taille":184}
}
def trouve_age(nom:str, personnes:dict):
    if nom in personnes:
        return personnes[nom]["age"]
    else:
        return None


def trouve_taille(nom:str, personnes:dict):
    if nom in personnes:
        return personnes[nom]["taille"]
    else:
        return None

nom = "Jean Aymar"
print(trouve_taille(nom, personnes))

def calcule_taille_moyenne(personnes:dict):
    liste_taille = []
    taille_adition = 0
    for personne in personnes:
        liste_taille.append(trouve_taille(nom=personne , personnes=personnes))
    for taille in liste_taille:
        taille_adition = taille_adition + taille
    return taille_adition/len(liste_taille)

def calcule_taille_moyenne2(personnes:dict):
    taille_adition = 0
    for personne in personnes:
        taille_adition = taille_adition + trouve_taille(nom=personne , personnes=personnes)
    return taille_adition/len(personnes)

def info_nom():
    for nom in personnes:
        print("\nNom    : "+nom)
        print("Pays   : "+str(personnes[nom]["pays"]))
        print("Taille : "+str(personnes[nom]["taille"])+" an(s)")
        print("Age    : "+str(personnes[nom]["age"])+" cm")

info_nom()

print("\nTaille moyenne = "+str(calcule_taille_moyenne2(personnes)))