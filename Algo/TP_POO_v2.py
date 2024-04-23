class Animal():
    def __init__(self, nom, age, faim, repos, sante=100):
        self.nom = nom
        self.age = age
        self.__faim = faim
        self.__repos = repos
        self.__sante = sante

    def get_faim(self):
        return self.__faim

    def get_repos(self):
        return self.__repos
    
    def manger(self)->None:
        if self.__repos == False:
            self.__faim = self.__faim + 5
            return None
        else:
            print("Je suis en train de dormir, je ne peux pas manger")
            return None


    def dormir(self)->None:
        self.__faim = self.__faim - 1
        self.__repos = True
        print("Bonne nuit !!")
        return None

    def eveiller(self)->None:
        self.__repos = False
        print("Ah quel belle journée !!")
        return None

    def manger_herbe(self)->None:
        raise PasBon()

    def manger_viande(self)->None:
        raise PasBon()

    def nourrir(self, nourriture): #le self fait reférance à l'animal, Viande
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


class Herbe():
    def nourrir(self, a)->None:
        try:
            a.manger_herbe()
            print("Miam miam !!")
        except PasBon:
            print("Je refuse cette nourriture")

class Viande():
    def nourrir(self, a)->None:
        try:
            a.manger_viande()
            print("Miam miam !!")
        except PasBon:
            print("Je refuse cette nourriture")

class PasBon(Exception):
    pass


def jeu(espece):
    print(f"\n1) Pour nourir {espece.nom}")
    print(f"2) M'endormir ou me réveiller")
    print(f"9) Pour les info liées à {espece.nom}")
    action = str(input("Action : "))
    if action == "1":
        nourir_animal(espece)
        jeu(espece)
    if action == "2":
        print("\n1) me réveiller")
        print("2) m'endormir")
        action_dormir = str(input("Action : "))
        if action_dormir == "1":
            espece.eveiller()
            jeu(espece)
        if action_dormir == "2":
            espece.dormir()
            jeu(espece)
    if action == "9":
        print("\nNom   : " + str(espece.nom))
        print("Age   : " + str(espece.age))
        print("Faim  : " + str(espece.get_faim()))
        if espece.get_repos() == True:
            print("Repos : Je suis en train de dormir")
        else:
            print("Repos : Je suis éveillé")
        jeu(espece)


def nourir_animal(espece):
    print("\n1) Herbe")
    print("2) Viande")
    action_nourrir = str(input("Me nourrir avec :"))
    if action_nourrir == "1":
        nourriture = Herbe()
        espece.nourrir(nourriture)
    elif action_nourrir == "2":
        nourriture = Viande()
        espece.nourrir(nourriture)


'''
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

#creer_animal()
'''

lion = Carnivore(nom="pierre", age=72, faim=2, repos=False)
jeu(lion)