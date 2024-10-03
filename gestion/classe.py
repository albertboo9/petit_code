class CompteBancaire():
    def __init__(self, n='dupont', s=1000):
        self.nom=n
        self.solde=s

    def retrait(self, m=0):
        self.solde=self.solde - m

    def depot(self, m=0):
        self.solde = self.solde + m

    def affiche(self):
        print(f'le titulaire du compte s\'appelle {self.nom} son solde est de {self.solde}')

class voiture(object):
    def __init__(self, ma='ford', cou='rouge'):
        self.marque=ma
        self.couleur=cou

    def choix_conducteur(self, no='personne'):
        self.nom=no

    def accelerer(self, t=0, du=0):
        if self.nom=='personne':
            self.vitesse=0
        else:
            self.vitesse=t*du

    def affiche_tout(self):
        print(f'{self.marque} {self.couleur} pilotée par {self.nom}, vitesse = {self.vitesse}m/s.')




