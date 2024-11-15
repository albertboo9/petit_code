from random import randrange

#Création d'une classe jeu de cartes

class JeuCartes(object):

    def __init__(self):
        
        
        
        
        self.jeu=[]
        for i in range(0,4):
            for j in range(2,15) :
                self.jeu.append((j,i))

    def battre(self):
        l=len(self.jeu)
        for i in range(l):
            #tirage aléatoire de 2 emplacements dans le jeu
            h1,h2=randrange(l),randrange(l)
            #échange des valeurs presente dans ces emplacements
            self.jeu[h1], self.jeu[h2] = self.jeu[h2], self.jeu[h1]


    def tirer(self):
        t=len(self.jeu)
        if t>0 :
            carte=self.jeu[0]
            del(self.jeu[0])
            return carte
        else:
            return None

    def NomCartes(self,ind=()):
        nom=""
        nom1=""

        self.indice=ind

        if self.indice[0] in range(2,11):
            nom=self.indice[0]
        if self.indice[0]== 11:
            nom= "valet"
        if self.indice[0]==12:
            nom="dame"
        if self.indice[0]==13:
            nom = "roi"
        if self.indice[0]==14:
            nom ="as"

        if self.indice[1]==0:
            nom1="coeur"
        if self.indice[1]==1:
            nom1="carreau"
        if self.indice[1]==2:
            nom1="trèfle"
        if self.indice[1]==3:
            nom1="pique"


        return f'{nom} de {nom1}'


if __name__=="__main__":
    jeu1=JeuCartes()
    jeu2=JeuCartes()
    jeu2.battre()
    jeu1.battre()
    A=0
    B=0
    for i in range (53):
        carte1=jeu1.tirer()
        carte2=jeu2.tirer()
        if carte1[0] < carte2[0]:
            B+=1
        else:
            if carte1[0]>carte2[0]:
                A+=1
            else:
                None

    if A<B:
        print("le joueur A a gagné la manche")
    else:
        if A>B:
            print("le joueur B a gagné la manche")
        else:
            print("c'est un match nul")



