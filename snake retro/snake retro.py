
import pygame
from pygame.locals import *
pygame.init()

from random import randint

#fichier = open("score.txt", "w")
#fichier.write("KAV:5\n")

#fichier.close()

lSCORE = []
lNAME = []

# IMAGES :
##########
HEAD = pygame.image.load("head.png")
FOND_B = pygame.image.load("fond.png")
BODY = pygame.image.load("body.png")
POMME = pygame.image.load("pomme.png")
CADRE = pygame.image.load("cadre.png")
LOGO = pygame.image.load("logo.png")
MAP = pygame.image.load("map.png")
FOND_W = pygame.image.load("fond_w.png")
OVER = pygame.image.load("over.png")
I_FOND = pygame.image.load("intro_f.png")
I_LOGO = pygame.image.load("intro_s.png")
I_IMAGE = pygame.image.load("intro_i.png")

# SON :
#######
son_intro = pygame.mixer.Sound("intro.wav")
son_eat = pygame.mixer.Sound("eat.wav")
son_gOver = pygame.mixer.Sound("gameover.wav")
# TEXTE :
#########
font = pygame.font.Font(None,20)
SCORE = font.render("SCORE : ", True, (133,83,15))

# FONCTION :
############
def restart() :
    # CHARGEMENT des donées :
    #########################
    fichier = open("score.txt", "r")
    for ligne in fichier :
        ligne.strip()
        ligne = ligne.split(":")
        lSCORE.append(int(ligne[1]))
        lNAME.append(ligne[0])
    fichier.close()
    print(lSCORE)
    SCOREMAX = font.render(str(lSCORE[0]), True, (133, 83, 15))
    MAXNAME = font.render("MAX : ", True, (133, 83, 15))

    fenetre.blit(CADRE, (0,0))
    fenetre.blit(LOGO, (210,96))
    fenetre.blit(MAP, (148,170))
    fenetre.blit(SCORE, (148,445))
    fenetre.blit(FOND_W,(148,465))
    fenetre.blit(MAXNAME, (148,465))
    fenetre.blit(SCOREMAX,(210,465))

    # SNAKE :
    #######
    global corps
    corps = [(310,310),(300,310)] # coordonnées corps de SNAKE
    
    # VARIABLES :
    #############
    global game
    game = True
    global x_head
    x_head = 310 # coordonnée de la tête
    global y_head
    y_head = 310 #

    global indice
    indice = len(corps) - 1 # taille du corps

    global touche
    touche = False # boucle effet mémoire
    global clavier
    clavier = "NONE" # touche effet mémoire
    global FPS
    FPS = 3 # vitesse du jeu

    global x_pomme
    x_pomme = -10 # cordonnée des pommes
    global y_pomme
    y_pomme = -10 #
    global pomme
    pomme = False # verifie les pomme sur le jeu
    global mange
    mange = 0 # le score

    global de
    de = 0 # choix hasard couleur corps

    global game_d # posibilité de redémarrer
    game_d = 0 

    # AFFICHAGE SNAKE INITIALE :
    fenetre.blit(HEAD,(310,310))
    fenetre.blit(BODY,(300,310))
    return

def intro() :
    # VARIABLES :
    intro = True
    image_pos = 0
    
    # INTRO:
    son_intro.play()
    while intro == True :
        pygame.time.Clock().tick(image_pos)

        if image_pos <50 :
            image_pos += 1
        # Instruction
        for event in pygame.event.get() :
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    intro = False
            if event.type == QUIT :
                pygame.quit()
        #clignotement des images
        fenetre.blit(I_FOND, (148,170))
        if (image_pos % 2) == 1:
            fenetre.blit(I_LOGO, (236,199))
        elif (image_pos % 2) == 0:
            fenetre.blit(I_IMAGE, (161,258))
        if image_pos == 50 :
            fenetre.blit(I_FOND, (148,170))
            fenetre.blit(I_LOGO, (236,199))
            fenetre.blit(I_IMAGE, (161,258))
            
        pygame.display.update()
    son_intro.stop()
    # initialisation fenêtre :
    restart()    
    

# FENETRE :
###########
fenetre = pygame.display.set_mode((600,600))
pygame.display.set_caption("SNAKE")

# initialisation fenêtre :
restart()

# introduction :
intro()

# PROGRAMME :
#############
while game == True : # Tant que le serpent est vivant
    pygame.time.Clock().tick(FPS + mange)

    # On capte les instrucrions :
    for event in pygame.event.get(): 
        if event.type == QUIT :
            pygame.quit()
        if event.type == KEYUP or event.type == KEYDOWN :
            if event.key == K_UP : # Montée
                if clavier != "DOWN":
                    clavier = "UP"
            elif event.key == K_DOWN  : # Descente
                if clavier != "UP":
                    clavier = "DOWN"
            elif event.key == K_RIGHT : # Aller à droite
                if clavier != "LEFT":
                    clavier = "RIGHT"
            elif event.key == K_LEFT : # Aller à gauche
                if clavier != "RIGHT":
                    clavier = "LEFT"
            touche = True
            
    # Effet mémoire :
    if clavier == "UP" :
        y_head -= 10
    elif clavier == "DOWN" :
        y_head += 10
    elif clavier == "RIGHT" :
        x_head += 10
    elif clavier == "LEFT" :
        x_head -= 10
        
    #Defaite :
    if (x_head < 148) or (x_head >463) or (y_head < 170) or (y_head > 439): # sortit écran
        game_d = "wait"
    elif (x_head, y_head) in corps[1:indice]: # mirdre la queue
        game_d = "wait"
    #Redémarrage :
    if game_d == "wait" :
        son_gOver.play()
        fichier = open("score.txt","w")
        for i in range(len(lSCORE)):
            if mange>int(lSCORE[i]):
                lSCORE[i] = str(mange)
                
        for i in range(len(lSCORE)):
            fichier.write(lNAME[i] +":"+str(lSCORE[i])+"\n")
        fichier.close()
        SCOREMAX = font.render(str(lSCORE[0]), True, (133, 83, 15))
        MAXNAME = font.render("MAX : ", True, (133, 83, 15))
        while  game_d == "wait" :
            fenetre.blit(OVER,(148,170))
            pygame.display.update()
            for event in pygame.event.get() :
                if event.type == KEYDOWN :
                    if event.key == K_SPACE:
                        restart()
                        game_d = "restart"
                    elif event.key == K_ESCAPE :
                        pygame.quit()
            

    # Changement positions corps :           
    if touche == True :
        effacer = corps[indice]
        for indice_corps in range(indice): # on change les cordonnées du corps à chaque déplacement
            new_value = corps[indice_corps+1]
            corps[indice_corps+1] = corps[0]
            corps[0] = new_value  
    indice = len(corps)-1

    corps[0]=(x_head,y_head) # la nouvelle position de la tête

    # cordonnés Pomme :
    if pomme == False  :
        x_pomme = randint(16,45)*10
        y_pomme = randint(18,42)*10
        
        if (x_pomme,y_pomme) in corps :
            pomme = False
        else:
            pomme = True

    # Manger pomme : 
    if corps[0] == (x_pomme,y_pomme): # grandir le corps
        son_eat.play()
        x,y=corps[indice-1]
        x-=10
        new_cord = (x,y)
        corps.append(new_cord)
        pomme = False
        mange += 1 # le score
        MANGE = font.render(str(mange), True, (133, 83, 15))
        fenetre.blit(FOND_W,(210,445))
        fenetre.blit(MANGE,(210,445))
    # Affichage de Snake :
    if touche == True :
        fenetre.blit(FOND_B,(effacer)) # On efface l'ecran 
        for i in range(indice+1) : # on met les partie du corps
               
            if i!=0 :
                fenetre.blit(BODY, corps[i])
            elif i==0:
                fenetre.blit(HEAD, corps[i])
            if pomme == True : # placement de la pomme
                fenetre.blit(POMME,(x_pomme,y_pomme))
                
    pygame.display.update()

    
    
            
        



