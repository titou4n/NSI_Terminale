class Animal():
    def __init__(self, nom, age, faim, repos):
        self.nom = nom
        self.age = age
        #self.__faim = faim
        #self.__repos = repos
        self.faim = faim
        self.repos = repos
    
    def manger(self)->None:
        #self.__faim = self.__faim + 1
        #self.__repos = False
        self.faim = self.faim + 1
        self.repos = False
        return None

    def dormir(self)->None:
        #self.__faim = self.__faim - 1
        #self.__repos = True
        self.faim = self.faim - 1
        self.repos = False
        return None

    def manger_herbe(self)->None:
        raise PasBon()

    def manger_viande(self)->None:
        raise PasBon()

    def nourrir(self, nourriture): #animal, Viande
        nourriture.nourrir(self)



class Herbivore(Animal):
    def __init__(self, nom, age, faim, repos):
        Animal.__init__(self, nom, age, faim, repos)
    
    def manger_herbe(self)->None:
        self.manger()

class Carnivore(Animal):
    def __init__(self, nom, age, faim, repos):
        Animal.__init__(self, nom, age, faim, repos)

    def manger_viande(self)->None:
        self.manger()


class Omnivore(Animal):
    def __init__(self, nom, age, faim, repos):
        Animal.__init__(self, nom, age, faim, repos)

    def manger_herbe(self)->None:
        self.manger()

    def manger_viande(self)->None:
        self.manger()


class PasBon(Exception):
    pass


class Herbe():
    def nourrir(self, a)->None:
        try:
            a.manger_herbe()
        except PasBon:
            print("Je refuse cette nourriture")

class Viande():
    def nourrir(self, a)->None:
        try:
            a.manger_viande()
        except PasBon:
            print("Je refuse cette nourriture")


#animal = Carnivore(nom="pierre", age=72, faim=2, repos=False)

def jeu(espece):
    print("1) pour le nouurir")
    print("10) pour les info")
    action = str(input("Action : "))
    if action == "1":
        print("1) Herbe")
        print("2) Viande")
        action_nourrir = str(input("Action : "))
        if action_nourrir == "1":
            espece.nourrir(Herbe())
            jeu(espece)
        if action_nourrir == "2":
            espece.nourrir(Viande())
            jeu(espece)
    if action == "10":
        print("Nom   : " + str(espece.nom))
        print("Age   : " + str(espece.age))
        print("Faim  : " + str(espece.faim))
        print("Repos : " + str(espece.repos))
        jeu(espece)


def creer_animal():
    print("Creer un animal")
    #animal = str(input("Animal   : "))
    nom = str(input("Nom   : "))
    age = int(input("Age   : "))
    faim = int(input("Faim  : "))
    repos = True
    animal = Carnivore(nom="pierre", age=72, faim=2, repos=False)
    print("1) pour un Herbivore")
    print("2) pour un Carnivore")
    print("3) pour un Omnivore")
    action = str(input("Action : "))
    if action == "1":
        animal = Herbivore(nom=nom, age=age, faim=faim, repos=repos)
        jeu(animal)
    if action == "2":
        animal = Carnivore(nom=nom, age=age, faim=faim, repos=repos)
        jeu(animal)
    if action == "3":
        animal = Carnivore(nom=nom, age=age, faim=faim, repos=repos)
        jeu(animal)


creer_animal()
#jeu(animal)