def interaction_gravitationnelle(ma,mb,d):
    G=6.67*10**(-11)
    F=(G*ma*mb)/(d**2)
    return F

ma=5.972*10**24
mb=60
d = 6,37*(10**6)

print(interaction_gravitationnelle(ma,mb,d))
