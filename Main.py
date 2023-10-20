
### ALBERT

# petit programme python qui calcule le périmètre, l'air, et le volume de la pluspart des figure géométrique

from math import *

class aires():
	def __init__():
		print("Aires : CARRE - RECTANGLE - TRIANGLE - CERCLE - TRAPEZE")
		a = input("Que voulez-vous choisir ? : ")
		if a.upper() == "CARRE":
			aires.carre()
		elif a.upper() == "RECTANGLE":
			aires.rectangle()
		elif a.upper() == "TRIANGLE":
			aires.triangle()
		elif a.upper() == "CERCLE":
			aires.cercle()
		elif a.upper() == "TRAPEZE":
			aires.trapeze()
		else:
			print("Requête non-comprise")
	def rectangle():
		print("Veuillez donner une Longueur X largeur")
		rectlo = input("Longueur : ")
		rectla = input("Largeur : ")
		rectloc = int(rectlo)
		rectlac = int(rectla)
		rect = rectloc * rectlac
		print("Votre Rectangle a {} d'Aire".format(rect))
	def carre():
		h = input("Un côté : ")
		hc = int(h)
		hcalc = hc * hc
		print("Votre Carré a {} d'Aire".format(hcalc))
	def triangle():
		h = input("La Base : ")
		hh = input("La Hauteur : ")
		hc = int(h)
		hhc = int(hh)
		calc = hc * hhc /2
		print("Votre rectangle a {} d'Aire".format(calc))
	def cercle():
		h = input("(D)emi-Cercle ou (C)ercle : ")
		if h.upper() == "D":
			hv = input("Votre rayon : ")
			hvc = int(hv)
			hcalc = 3.14 * (hvc * hvc) /2
			print("Votre Demi-Cercle a {} d'Aire".format(hcalc))
		elif h.upper() == "C":
			hv = input("Votre rayon : ")
			hvc = int(hv)
			hcalc = 3.14 * (hvc * hvc)
			print("Votre Cercle a {} d'Aire".format(hcalc))
	def trapeze():
		h = input("Longueur de la Grande Base : ")
		hb = input("Longueur de la petite base : ")
		hh = input("Hauteur du Trapèze : ")
		hc = int(h)
		hbc = int(hb)
		hhc = int(hh)
		hcalc = (hc + hbc) * hhc /2
		print("Le Trapèze a {} d'Aire".format(hcalc))
class perimetres():
	def __init__():
		print("Périmètres : CARRE - RECTANGLE - LOSANGE - CERCLE")
		h = input("Choix : ")
		if h.upper() == "CARRE":
			perimetres.carre()
		elif h.upper() == "RECTANGLE":
			perimetres.rectangle()
		elif h.upper() == "LOSANGE":
			perimetres.losange()
		elif h.upper() == "CERCLE":
			perimetres.cercle()
		else:
			print("Requête non-comprise")
	def carre():
		h = input("Votre Côté : ")
		hc = int(h)
		calc = hc * 4
		print("Périmètre = {}".format(calc))
	def rectangle():
		h = input("Largeur(l) : ")
		hb = input("Longueur(L) : ")
		hc = int(h)
		hbc = int(hb)
		calc = (hc * 2) + (hbc * 2)
		print("Périmètre Rectangle = {}".format(calc))
	def losange():
		h = input("Grande Diagonale : ")
		hp = input("petite diagonale : ")
		hc = int(h)
		hpc = int(hp)
		calc = ((hc * 2) + (hpc * 2)) /2
		print("Le losange a {} de Périmètre ".format(calc))
	def cercle():
		h = input("(D)emi-Cercle ou (C)ercle : ")
		if h.upper() == "D":
			hv = input("Votre Rayon : ")
			hvc = int(hv)
			calc = 2 * 3.14 * hvc /2
			print("Votre Demi-Cercle a {} de Périmètre".format(calc))
		elif h.upper() == "C":
			hv = input("Votre Rayon : ")
			hvc = int(hv)
			calc = 2 * 3.14 * hvc
			print("Votre cercle a {} de Périmètre".format(calc))
class volumes():
	def __init__():
		print("Volumes : CUBE - PRISME - CYLINDRE - CONE - PAVE(Parallélépipède)")
		h = input("Votre Choix : ")
		if h.upper() == "CUBE":
			volumes.cube()
		elif h.upper() == "PRISME":
			volumes.prisme()
		elif h.upper() == "CYLINDRE":
			volumes.cylindre()
		elif h.upper() == "CONE":
			volumes.cone()
		elif h.upper() == "PAVE":
			volumes.pave()
		else:
			print("Requête non-comprise")
	def cube():
		h = input("Arête : ")
		hc = int(h)
		calcv = hc * hc * hc
		calca = 6 * (hc * hc)
		print("Volume = {}".format(calcv))
		print("Aire Totale = {}".format(calca))

	def prisme():
		print("Il faudra la base d'aire de 6 côtés")
		h = input("Un côté de la base : ")
		hc = int(h)
		calcp = 6 * hc
		print("Périmètre de la base = {}".format(calcp))
		calca = ((3 * sqrt(3) ) / 2) * hc
		print("Aire de la base = {}".format(calca))
		haut = input("Hauteur : ")
		hautc = int(haut)
		calcal = calcp * hautc
		print("Aire Latérale = {}".format(calcal))
		calcv = calca * hautc
		print("Volume = {}".format(calcv))
        
	def cylindre():
		h = input("Rayon : ")
		ha = input("Hauteur : ")
		hc = float(h)
		hac = int(ha)
		calcair = 3.14 * (hc * hc)
		calcvo = 3.14 * (hc * hc) * hac
		calcaire = (2 * 3.1416) * hc * hac
		print("L'aire de la base = {}".format(calcair))
		print("L'aire Latérale = {}".format(calcaire))
		print("Volume = {}".format(calcvo))
        
	def cone():
		r = input("Votre Rayon : ")
		h = input("Votre Hauteur : ")
		rc = int(r)
		hc = int(h)
		calcair = 3.14 * (rc * rc)
		calcper = 2 * 3.14 * rc
		calcvol = (1 / 3) * calcair * hc
		print("Aire de la base = {}".format(calcair))
		print("Périmètre de la base = {}".format(calcper))
		print("Volume = {}".format(calcvol))
        
	def pave():
		longu = input("Longueur(L) : ")
		large = input("Largeur(l) : ")
		haut = input("Hauteur : ")
		longuc = int(longu)
		largec = int(large)
		hautc = int(haut)
		aireto = 2 (longuc * largec + longuc * hautc + largec * hautc)
		volume = longuc * largec * hautc
		print("L'aire Totale est de = {}".format(aireto))
		print("Le volume est de = {}".format(volume))
print("GEOMETRIE : VOLUMES - AIRES - PERIMETRES")
start = input("faites votre choix")
if start.upper() == "VOLUMES":
	volumes.__init__()
elif start.upper() == "AIRES":
	aires.__init__()
elif start.upper() == "PERIMETRES":
	perimetres.__init__()
else:
	print("ERREUR")
