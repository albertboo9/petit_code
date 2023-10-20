#B.A.E


code=[
  ".-", 
  "-...",  "-.-.","-..",  ".",  "..-.",  "--.","....","..",
  ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
  "-","..-","...-",".--","-..-","-.--","--..",
  "-----",
  ".----","..---","...--","....-",".....","-....","--...","---..","----."] 
ascii="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
xx=""".--. --- ..- .-.  ...- .- .-.. .. -.. . .-.  .. .-..  - .  ... ..- ..-. ..-. .. -  -.. .  - .- .--. . .-.  ... .- -- ..- . .-..  ... ..- .. ...- ..  -.. .  ... --- -.  -. --- --  -.. .  ..-. .- -- .. .-.. .-.. .  .-.. .  - --- ..- -  .- - - .- -.-. .... .  . -  . -.  -- .. -. ..- ... -.-. ..- .-.. . ...  """


import winsound
import time
def point():
      winsound.Beep(1500,100)
def trait():
      winsound.Beep(1500,200)
x='... --- ... '
def joue(x):          #jouer et traduire un code morse (dans x='-- ..
      print ('\ndecodage du morse')
      x=x+' '
      codage=""
      message=""
      messagePartiel=""
      affichage=""             #message affiché à  l'écran
      debut=False
      for i in range(len(x)):  #
            if x[i]=='.':
                  point()
                  codage+=x[i]
                  affichage+='.'
                  debut=True
            elif x[i]=='-':
                  trait()
                  codage+=x[i]
                  affichage+='-'
                  debut=True
            elif ((x[i]==' ')|(x[i]=='|')):
                  time.sleep(0.5)
                  if debut:
                        print ('[',codage,']',)
                        debut=False
                  texte=''
                  trouve=False
                  for cad in enumerate(code):
                        if cad[1]==codage:
                              texte=ascii[cad[0]]
                              message+=texte
                              messagePartiel+=texte
                              affichage+=texte
                              trouve=True
                              print (texte,)
                  if not trouve :
                        print ('??',)
                  codage=""
                  if i+1<len(x):
                        if x[i+1]==' ':
                              message+='  '
                              print ('\n\t\t\t\t\t',messagePartiel)
                              messagePartiel=""
      print ('\ntraduction '+message)
      return message

def codage(texte):      #code un texte en clair (texte)en morse (return x)
      print ('\ncodage du texte')
      x=''
      texte=texte.upper()
      for position in range(len(texte)):
            entree=texte[position]
            print (entree,)
            trouve=False
            for numero in range (len(ascii)):
                  if ascii[numero]==entree:
                        x+=code[numero]+' '
                        print (code[numero],'   ',)
                        trouve=True
            if not trouve:
                  print ('???',)
            if entree==' ':
                  x+='  '
                  print ('\n',)
      print ('')
      return x

for i in range(len(ascii)): #affichage du code morse
      print ('[',code[i],']=',ascii[i],'  ',)
      if not (i+1)%9:
            print
print("-----------------------------------------------------------------------------------------------------------------------------")
x=codage('hello')
joue (x)
texte='non vide'
while texte!='':
      texte=raw_input('\n entrer votre message en clair : ')
      texte=texte.upper()
      x=codage(texte)
      joue (x)
      
texte='non vide'
#texte=texte.upper()
while texte!="":
      texte=raw_input('\nentrer votre message en morse : ')
      joue(texte)
      print (texte)
print ("message � d�coder : ", xx)
joue(xx)




            
            
            
