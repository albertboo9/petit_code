from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os
import sqlite3
"""
#identifiants
identifiants=[username, password]
"""

#fenetre
root = Tk()
root.title("GESTION DES PATIENTS ")
root.geometry("1300x700")
root.configure(bg="#091821")
root.resizable(False, False)

# ajout des titres et label à la fenetre de gestion

ti = Label(text="GESTION DES PATIENTS DE L'HOPITAL LA MISERICODE DIVINE", bg="#192030", fg="white", font=("Arial", 29))
ti.place(x=0, y=0, width=1300, height=50)

titre= Label(text="LISTE  DES PATIENTS", bg="pink" ,fg="#391829", font=("Arial", 30))
titre.place(x=420, width=867, y=60, height=40)
inf1 = Label(text="Matricule", bg="#114630", fg="white", font=("Sans resif", 20))
inf1.place(x=0, width=200, y=60, height=40)
inf2 = Label(text="Nom", bg="#114630", fg="white", font=("Sans resif", 20))
inf2.place(x=0, width=200, y=110, height=40)
inf3 = Label(text="Prenom", bg="#114630", fg="white", font=("Sans resif", 20))
inf3.place(x=0, width=200, y=160, height=40)
inf4 = Label(text="Age", bg="#114630", fg="white", font=("Sans resif", 20))
inf4.place(x=0, width=200, y=210, height=40)
inf5 = Label(text="Sexe", bg="#114630", fg="white", font=("Sans resif", 20))
inf5.place(x=0, width=200, y=260, height=40)
inf6 = Label(text="N° Telephone", bg="#114630", fg="white", font=("Sans resif", 20))
inf6.place(x=0, width=200, y=310, height=40)
inf7 = Label(text="Quartier", bg="#114630", fg="white", font=("Sans resif", 20))
inf7.place(x=0, width=200, y=360, height=40)
inf_a = Label(text="Date d'entrée", bg="#114630", fg="white" , font=("Sans resif", 20))
inf_a.place(x=0, width=200, y=510, height=40)
inf7 = Label(text="Date de sortie", bg="#114630", fg="white" , font=("Sans resif", 20))
inf7.place(x=0, width=200, y=560, height=40)
inf8 = Label(text="Examen", bg="#114630", fg="white" , font=("Sans resif", 20))
inf8.place(x=0, width=200, y=410, height=40)
inf9 = Label(text="Frais total", bg="#114630", fg="white" , font=("Sans resif", 20))
inf9.place(x=0, width=200, y=460, height=40)

#ajout des entrées à la fenetre de gestion des patients

ent1 = Entry(root, bg="white", font=("Arial", 13))
ent1.place(x=205, y=60, width=200, height=40)
ent2 = Entry(root, bg="white", font=("Arial", 13))
ent2.place(x=205, y=110, width=200, height=40)
ent3 = Entry(root, bg="white", font=("Arial", 13))
ent3.place(x=205, y=160, width=200, height=40)
ent4= Entry(root, bg="white", font=("Arial", 13))
ent4.place(x=205, y=210, width=200, height=40)
genre =["M", "F"]
ent5 = Spinbox(root, bg="white", font=("Arial", 13), values=genre)
ent5.place(x=205, y=260, width=200, height=40)
ent6 = Entry(root, bg="white", font=("Arial", 13))
ent6.place(x=205, y=310, width=200, height=40)
ent7 = Entry(root, bg="white", font=("Arial", 13))
ent7.place(x=205, y=360, width=200, height=40)
ent8 = Entry(root, bg="white", font=("Arial", 13))
ent8.place(x=205, y=410, width=200, height=40)
ent9 = Entry(root, bg="white", font=("Arial", 13))
ent9.place(x=205, y=460, width=200, height=40)
ent10 = Entry(root, bg="white", font=("Arial", 13))
ent10.place(x=205, y=510, width=200, height=40)
ent11 = Entry(root, bg="white", font=("Arial", 13))
ent11.place(x=205, y=560, width=200, height=40)


#Tableau d'affichage des pients enregistrer
table= ttk.Treeview(root,  columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), height=5, show="headings")
table.place(x=420, width=847, y=110, height=550)

#barre de defilement
sbar = ttk.Scrollbar(root, command=table.yview)
sbar.place(height=550, x=1270, y=110)
table.config(yscrollcommand=sbar.set)
       #entête de la table

table.heading(1, text="Mat")
table.heading(2, text="Nom")
table.heading(3, text="Prenom")
table.heading(4, text="Age")
table.heading(5, text="Sexe")
table.heading(6, text="N° Telephone")
table.heading(7, text="Quartier")
table.heading(8, text="Examen")
table.heading(9, text="Frais")
table.heading(10, text="Date d'entrée")
table.heading(11, text="Date de sortie")

       #Dimensions des colonnes
table.column(1, width=40)
table.column(2, width=70)
table.column(3, width=60)
table.column(4, width=30)
table.column(5, width=40)
table.column(6, width=100)
table.column(7, width=100)
table.column(8, width=100)
table.column(9, width=100)
table.column(10, width=100)
table.column(11, width=100)

def ajouter():
    mat= ent1.get()
    nom = ent2.get()
    prenom=ent3.get()
    age = ent4.get()
    sexe = ent5.get()
    tel = ent6.get()
    quartier = ent7.get()
    exam = ent8.get()
    frais = ent9.get()
    entre = ent10.get()
    sortie = ent11.get()



    #creons la connexion
    con = sqlite3.connect('hopital.db')
    cur = con.cursor()
    cur.execute("insert into patient values(?,?,?,?,?,?,?,?,?,?,?);",(mat, nom, prenom, age, sexe, tel,quartier, exam, frais, entre, sortie))
    con.commit()
    con.close()
    messagebox.showinfo("Patient ajouter")

    #afficher
    con = sqlite3.connect('hopital.db')
    cur = con.cursor()
    select = cur.execute("select * from patient order by mat desc")
    select = list(select)
    table.insert('', END, values=select[0])
    con.close()
    ent1.delete(0, "end")
    ent2.delete(0, "end")
    ent3.delete(0, "end")
    ent4.delete(0, "end")
    ent5.delete(0, "end")
    ent6.delete(0, "end")
    ent7.delete(0, "end")
    ent8.delete(0, "end")
    ent9.delete(0, "end")
    en10.delete(0, "end")
    ent11.delete(0, "end")

def supprimer():
    codeselect = table.item(table.selection())['values'][0]
    con = sqlite3.connect("hopital.db")
    cur = con.cursor()
    delete = cur.execute('delete from patient where mat={}'.format(codeselect))
    con.commit()
    table.delete(table.selection())

def modifier():
        mat = ent1.get()
        nom = ent2.get()
        prenom = ent3.get()
        age = ent4.get()
        sexe = ent5.get()
        tel = ent6.get()
        quartier = ent7.get()
        exam = ent8.get()
        frais = ent9.get()
        entre = ent10.get()
        sortie = ent11.get()

        # creons la connexion
        codeselect = table.item(table.selection())['values'][0]

        con = sqlite3.connect('hopital.db')
        cur = con.cursor()
        cur.execute(
            'update patient set mat=?, nom=?, prenom=?, age=?, sexe=?, tel=?, quartier=?, exam=?, frais=?, entre=?, sortie=? where mat={}'.format(
                codeselect),
            (mat, nom, prenom, age, sexe, tel, quartier, exam, frais, entre, sortie)

        )
        con.commit()
        con.close()
        messagebox.showinfo("patient modifier")

        # afficher
        con = sqlite3.connect('hopital.db')
        cur = con.cursor()
        select = cur.execute("select * from patient order by mat desc")
        select = list(select)
        table.insert('', END, values=select[0])
        con.close()
        supprimer()
        ent1.delete(0, "end")
        ent2.delete(0, "end")
        ent3.delete(0, "end")
        ent4.delete(0, "end")
        ent5.delete(0, "end")
        ent6.delete(0, "end")
        ent7.delete(0, "end")
        ent8.delete(0, "end")
        ent9.delete(0, "end")
        en10.delete(0, "end")
        ent11.delete(0, "end")


#Afficher les infos de la table
con= sqlite3.connect('hopital.db')
cur = con.cursor()
select = cur.execute("select * from patient")
for row in select:
    table.insert('', END, value=row)
con.close()

# les boutons de commande de l'appli de gestion des patients

Bt1 = Button(root, text="ENREGISTRER", bg="pink", font=("sans serif", 15), borderwidth=5, command=ajouter )
Bt1.place(x=10, y=610, width=180, height=40 )
Bt1 = Button(root, text="MODIFIER", bg="pink", font=("sans serif", 15), borderwidth=5, command= modifier )
Bt1.place(x=220, y=610, width=180, height=40 )
Bt1 = Button(root, text="SUPPRIMER", bg="pink", font=("sans serif", 15), borderwidth=5, command=supprimer )
Bt1.place(x=50, y=655, width=305, height=40 )

root.mainloop()