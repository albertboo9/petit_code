class Rectangle(object):
    "Classe de rectangles"
    def __init__(self, longueur=0, largeur=0):
        self.L=longueur
        self.l=largeur
        self.nom="rectangle"
    def perimetre(self):
        return"({0:d} + {1:d})*2={2:d}".\
            format(self.L, self.l, (self.l +self.L)*2)
    def surface(self):
        return "{0:d}*{1:d}={2:d}".format(self.L, self.l, self.l*self.L)
    def mesures(self):
        print("un {0} de {1:d} sur {2:d}".format(self.nom, self.L, self.l))
        print("a une surface de {0}".format(self.surface()))
        print("et un perimètre de {0}\n".format(self.perimetre()))

class Carre(Rectangle):
    "classe de carrés"
    def __init__(self,cote):
        Rectangle.__init__(self, cote, cote)
        self.nom="carré"


class Cercle(object):
    def __init__(self, rayon=0):
        self.rayon=rayon

    def surface(self):
        return 3.14*(self.rayon)**2

class Cylindre(Cercle):
    def __init__(self,rayon, hauteur):
        Cercle.__init__(self, rayon)
        self.hauteur=hauteur

    def volume(self):
        return self.surface()*self.hauteur


class Cone(Cylindre):
    def __init__(self,rayon,hauteur):
        Cylindre.__init__(self,rayon,hauteur)
    def volumes(self):
        return (Cylindre.volume(self))/3

if __name__=="__main__":
    r1=Rectangle(15, 30)
    r1.mesures()
    c1=Carre(13)
    c1.mesures()