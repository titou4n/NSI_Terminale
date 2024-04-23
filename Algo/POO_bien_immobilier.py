class Bim:
    def __init__(self, nature, surface, prix_moy):
        self.nt = nature
        self.sf = surface
        self.pm = prix_moy

    def estim_prix(self):
        if self.nt == "maison":
            return (self.sf * self.pm)*1.1
        if self.nt == "bureau":
            return (self.sf * self.pm)*0.8
        else:
            return self.sf * self.pm
        
    def nb_maison(lst):
        m = 0
        for nature in lst():
            if nature == "maison":
                m = m+1
        return m


toillete = Bim('toillete', 2.0, 15000.0)
b1 = Bim('maison', 70.0, 2000.0)
print(toillete.estim_prix())