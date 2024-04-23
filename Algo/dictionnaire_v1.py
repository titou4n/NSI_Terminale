#exercice 1
panier={"orange":1.5,
        "ananas":1,
        "grappe de raisin":1,
        "banane":4,
        "pommme":3,
        "prune":2
        }

print(panier["orange"])
print(panier.keys())
print("prune" in panier)

#print(panier["mangue"]) renvoi une erreur

#exercice 2

#fruit=str(input("fruit: "))
#quantité=float(input("quatité: "))

def ajoute_fruit(panier,fruit, quantité):
    if fruit in panier is False:
        panier[fruit]=quantité
    else:
        panier[fruit]=panier[fruit]+quantité
    return panier

#ajoute_fruit(panier,fruit, quantité)
print(panier.items())

#exercice 3
parc={  "machine1":"238.135.45.26",
        "machine2":"238.135.45.27",
        "machine3":"238.135.45.28"
    }

print(parc.items())
print("238.135.45.30" in parc.values())


#exercice 4

capitales={"France":"Paris",
            "Allemagne":"Berlin",
            "Portugal":"Lisbonne",
            "Espagne":"Madrid"
}