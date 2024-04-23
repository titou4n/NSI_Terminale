tab_itineraires=[]
def cherche_itineraires(G, start, end, chaine=[]):
    chaine = chaine + [start]
    if start == end:
        return chaine
    for u in G[start]:
        if u not in chaine:
            nchemin = cherche_itineraires(G, u, end, chaine)
            if len(nchemin) != 0:
                tab_itineraires.append(nchemin)
    return []

def itineraires_court(G,dep,arr):
    cherche_itineraires(G, dep, arr)
    tab_court = []
    mini = float('inf')
    for v in tab_itineraires:
        if len(v) <= mini :
            mini = len(v)
    for v in tab_itineraires:
        if len(v) == mini:
            tab_court.append(v)
    return tab_court

G = {}
G["A"] = "B", "E"
G["B"] = "A", "G", "F"
G["C"] = "E", "D"
G["D"] = "F", "E", "C"
G["E"] = "A", "C", "D"
G["F"] = "B", "D", "G"
G["G"] = "B", "F"

dep = "A"
arr="C"
print(itineraires_court(G,dep,arr))