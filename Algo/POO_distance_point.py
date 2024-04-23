class Point():
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def distance_origine_repere(self):
        distance = (self.x**2 + self.y**2)**0.5
        return distance

    def __repr__(self):
        #return "("+str(self.x)+" ; "+str(self.y)+")"
        return f"( {self.x}, {self.y} )"

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def distance_avec_point(self, p):
        distance_avec_point_sans_racine = (p.x-self.x)**2 + (p.y-self.y)**2
        distance_avec_point = distance_avec_point_sans_racine ** 0.5
        return distance_avec_point

#print(help(Point))
pa = Point(4,3)
pb = Point(4,3)



print(pa.distance_origine_repere())
print(pa.__repr__())
print(pa.__eq__(pb))
print(pa.distance_avec_point(pb))