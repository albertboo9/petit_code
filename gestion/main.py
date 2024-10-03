from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import sqlite3

"""
    #dimension de la fenetre

    #base de données des mot de passe et nom d'utilisateur
    con=sqlite3.connect('password.db')
    cursor=con.cursor()
    cursor.execute(
    "
        CREATE TABLE client IF NOT EXISTS(id PRIMARY KEY INTEGER, password INTEGER, username TEXT)
    "
    )
"""

root = Tk()

root.title("FENETRE DE CONNEXION")
root.geometry("400x300+450+200")
root.resizable(False,False )
root.configure(background="#091821")

#fonctions

def Seconnecter():
    surnom=txt_Nomutil.get()
    pw=txt_password.get()

    if (surnom =="" and pw==""):
        messagebox.showerror("", "Il faut entrer les données")
        txt_password.delete(0, "end")
        txt_Nomutil.delete(0, "end")
    elif (surnom=="albert" and pw=="9999"):
        messagebox.showinfo("", f"BIENVENUE {surnom}")
        txt_Nomutil.delete(0, "end")
        txt_password.delete(0, "end")
        root.destroy()
        call(["python","gestion_patients.py"])

    else:
        messagebox.showwarning("", "Erreur de connexion")
        txt_password.delete(0, "end")
        txt_Nomutil.delete(0, "end")

#ajout des titres et des labels
a_titre = Label(root, borderwidth=3, relief= SUNKEN, text="FORMULAIRE DE CONNEXION", font=("Sans serif", 20), background="#091821", fg="white")
a_titre.place(x=0, y=0, width=400)

a_Nomutilisateur=Label(root, text="NOM UTILISATEUR", font=("Arial", 12), fg="white", bg="#091821")
a_Nomutilisateur.place(x=5, y=100, width=150)

txt_Nomutil=Entry(root, bd=4, font=("Arial", 13))
txt_Nomutil.place(x=155, y=100, width=200, height=30)

a_password= Label(root, text="MOT DE PASSE", font=("Arial", 12), bg="#091821", fg="white" )
a_password.place(x=0, y=150, width=160)
txt_password = Entry(root, bd=4,font=("Arial", 13))
txt_password.place(x=155, y=150, width=200, height=30)

#bouton connecter
btnenregistrer = Button(root, text="CONNEXION", font=("Arial", 16 ), bg="blue", fg="white", command=Seconnecter)
btnenregistrer.place(x=150, y=200, width=200)




root.mainloop()