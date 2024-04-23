#Exercice 1:
#Q1
chevaliers = {  "Arthur":"roi",
                "Lancelot":"chevalier à la charette",
                "Yvain":"chevalier au lion"
}
#Q2
def ajout(chevaliers:dict, nom:str, surnom:str):
    if nom in chevaliers.keys():
        print("impossible")
    else:
        chevaliers[nom] = surnom

#Exercice 2:
#Q1
batiment = {"France":"Tour Eiffel",
            "Italie":"Colisée",
            "Angleterre":"Big Ben"
}

#Q2
def geographie(monument:str, batiment:dict):
    dict_batiment_inverse = {}
    for (pays, monume) in batiment.items():
        dict_batiment_inverse[monume] = pays
    if monument in dict_batiment_inverse.keys():
        return dict_batiment_inverse[monument]
    else:
        return None

print(geographie("Colisée", batiment))

#Q3
capitale = {"France":"Paris",
            "Italie":"Rome",
            "Angleterre":"Londres"
}
#Q4
def localisation(batiment:dict, capitale:dict):
    geoloc = {}
    for pays in capitale:
        ville = capitale[pays]
        monument = batiment[pays]
        geoloc[ville] = monument
    return geoloc


#Exercice 3:
#Q1
Jeux = {"Mattéo":{"PC":3, "XBOX":5, "Switch":8},
        "Antonin":{"XBOX":7, "PS":4},
        "Sébastien":{"Wii":10, "PS":2, "XBOX":1, "PC":5}
}

#Q2
def quantite(Jeux:dict, nom:str, nom_console:str):
    if nom in Jeux.keys():
        if nom_console in Jeux[nom]:
            return Jeux[nom][nom_console]
        else:
            return None
    else:
        return None