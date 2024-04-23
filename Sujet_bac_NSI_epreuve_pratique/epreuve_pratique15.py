t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(t_moy, annees):
    pbt = t_moy[0]
    a = None
    for i in range(len(t_moy)):
        if t_moy[i] < pbt:
            pbt=t_moy[i]
            a = i
    annee = annees[a]
    return pbt, annee
    
print(mini(t_moy, annees))
