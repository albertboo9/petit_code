
#importation des modules
from tkinter import *
import math as m

#fenêtre
root = Tk()
root.title("CALCULATRICE SCIENTIFIQUE DU LYBIBEP")
root.geometry("442x600")
root.configure(background="#091821")
root.resizable(False, False)
e = Entry(root, width=100, font=("Sans serif", 27), fg='black', bg='white')
e.place(x=0, y=42, height=90)


lbl = Label(root, background="#091880", width=100,  text="LYCEE BILINGUE DE BEPANDA", font=("Sans-serif", 20),  fg="white", relief=SUNKEN)
lbl.place(x=0, y=0, width=442, height=40)


def click(tp):
    on=e.get()
    e.delete(0, END)
    e.insert(0, on+tp)
    return

def sc(event):
    key =event.widget
    text =key['text']
    no=e.get()
    result=''
    if text=='deg':
        result = str(m.degrees(float(no)))
    if text=='sin':
        w = m.radians(float(no))
        result = str(m.sin(float(w)))
    if text=='cos':
        w= m.radians(float(no))
        result = str(m.cos(float(w)))
    if text == 'part':
        result = str(m.modf(float(no)))
    if text=='tan':
        w = m.radians(float(no))
        result = str(m.tan(float(w)))
    if text=='abs':
        result = str(m.fabs(float(no)))
    if text=='log':
        result = str(m.log10(float(no)))
    if text=='ln':
        result = str(m.log(float(no)))
    if text=='Sqrt':
        result = str(m.sqrt(float(no)))
    if text=='x!':
        result = str(m.factorial(int(no)))
    if text=='1/x':
        result = str(1/(float(no)))
    if text == 'log2':
        result = str(m.log2(float(no)))
    if text =="R3":
        result = str(m.pow(float(no), 1/3))
    if text=='pow(2)':
        result = str(m.pow(float(no), 2))
    if text == 'pow(3)':
        result = str(m.pow(float(no), 3))
    if text == 'EXP':
        result = str(m.exp(float(no)))
    if text=='Pi':
        if no=="":
            result=str(m.pi)
        else:
            result=str(float(no)*m.pi)
    if text=='e':
        if no=="":
            result=str(m.e)
        else:
            result=str(m.e**float(no))
    e.delete(0, END)
    e.insert(0, result)
def clear():
    e.delete(0, END)
    return
def back():
    cur = e.get()
    length = len(cur)-1
    e.delete(length, END)

def evaluate():
    ans = e.get()
    res = eval(ans)
    e.delete(0, END)
    e.insert(0, res)
#fonction mathematique

log = Button(root, text="log", background="#099800", fg="white", font=("Sans-serif", 17), relief=RAISED)
log.bind("<Button-1>", sc)
log.place(x=2, y= 140, width=70, height=40)
ln=Button(root, text="ln", background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED)
ln.bind("<Button-1>", sc)
ln.place(x=74, y=140,width=70, height=40 )
par1 = Button(root, text="(",  background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED, command=lambda: click("("))
par1.place(x=147, y=140,width=70, height=40)
par2 = Button(root, text=")", background="#099800", fg="white", font=("Sans-serif", 17), relief=RAISED, command=lambda: click(")"))
par2.place(x=220, y=140,width=70, height=40)
inv = Button(root, text="1/x", background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED)
inv.bind("<Button-1>", sc)
inv.place(x=294, y=140,width=70, height=40)
rc= Button(root, text="Sqrt", background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED)
rc.bind("<Button-1>", sc)
rc.place(x=369, y=140,width=70, height=40)
si= Button(root, text="sin", background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED)
si.bind("<Button-1>", sc)
si.place(x=0, y= 188,width=70, height=40)
co = Button(root, text="cos", background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED)
co.bind("<Button-1>", sc)
co.place(x=74, y= 188,width=70, height=40)
ta = Button(root, text="tan", background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED)
ta.bind("<Button-1>", sc)
ta.place(x=147, y= 188,width=70, height=40)
fac = Button(root, text="x!", background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED)
fac.bind("<Button-1>", sc)
fac.place(x=220, y= 188,width=70, height=40)
deg= Button(root, text="deg", background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED)
deg.bind("<Button-1>", sc)
deg.place(x=294, y= 188,width=70, height=40)
ex2= Button(root, text="abs",background="#099800", fg="white", font=("Sans-serif", 17), relief=RAISED)
ex2.bind("<Button-1>", sc)
ex2.place(x=369, y= 188,width=70, height=40)
ex3= Button(root, text="log2",background="#099800", fg="white", font=("Sans-serif", 17), relief=RAISED)
ex3.bind("<Button-1>", sc)
ex3.place(x=2, y= 236,width=70, height=40)
ex4= Button(root, text="part",background="#099800", fg="white", font=("Sans-serif", 17), relief=RAISED)
ex4.bind("<Button-1>", sc)
ex4.place(x=74, y= 236,width=70, height=40)
ex7 = Button(root, text="R3", background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED)
ex7.bind("<Button-1>", sc)
ex7.place(x=147, y=236, width=70 , height=40 )
ex8 = Button(root, text="pow(2)", background="#099800", fg="white", font=("Sans-serif", 17),relief=RAISED)
ex8.bind("<Button-1>", sc)
ex8.place(x=220, y= 236,width=70, height=40)
ex9 = Button(root, text="pow(3)",background="#099800", fg="white", font=("Sans-serif", 17), relief=RAISED)
ex9.bind("<Button-1>", sc)
ex9.place(x=294, y= 236,width=70, height=40)
ex0= Button(root, text="e",background="#099800", fg="white", font=("Sans-serif", 17), relief=RAISED)
ex0.bind("<Button-1>", sc)
ex0.place(x=369, y= 236,width=70, height=40)

#chiffre

p = Button(root, text=".",  background="pink", font=("Sans-serif", 20), fg="white", relief=RAISED, command=lambda: click("."))
p.place(x=0, y=530, width=100, height=70)
b0= Button(root, text="0", fg="white", font=("Sans-serif", 20), relief=RAISED, background="#091880", command=lambda: click("0"))
b0.place(x=101, y=530, width=100, height=70)
ex1 = Button(root, text="Pi" , fg="white", font=("Sans-serif", 20), background="pink", relief=RAISED)
ex1.bind("<Button-1>", sc)
ex1.place(x=202, y=530, width=100, height=70)
b1= Button(root, text="1", fg="white", font=("Sans-serif", 20), relief=RAISED,background="#091880", command=lambda: click("1"))
b1.place(x=0, y=459, width=100, height=70)
b2= Button(root, text="2", fg="white", font=("Sans-serif", 20), relief=RAISED, background="#091880",command=lambda: click("2"))
b2.place(x=101, y=459, width=100, height=70)
p3= Button(root, text="3",fg="white", font=("Sans-serif", 20),  relief=RAISED,background="#091880", command=lambda: click("3"))
p3.place(x=202, y=459, width=100, height=70)
p4= Button(root, text="4", fg="white", font=("Sans-serif", 20), relief=RAISED,background="#091880", command=lambda: click("4"))
p4.place(x=0, y=388, width=100, height=70)
p5= Button(root, text="5",fg="white", font=("Sans-serif", 20),  relief=RAISED,background="#091880", command=lambda: click("5"))
p5.place(x=101, y=388, width=100, height=70)
p6= Button(root, text="6", fg="white", font=("Sans-serif", 20), relief=RAISED,background="#091880", command=lambda: click("6"))
p6.place(x=202, y=388, width=100, height=70)
p7= Button(root, text="7", fg="white", font=("Sans-serif", 20), relief=RAISED,background="#091880", command=lambda: click("7"))
p7.place(x=0, y=317, width=100, height=70)
p8= Button(root, text="8",  fg="white", font=("Sans-serif", 20),relief=RAISED,background="#091880", command=lambda: click("8"))
p8.place(x=101, y=317, width=100, height=70)
p9= Button(root, text="9", fg="white", font=("Sans-serif", 20), relief=RAISED,background="#091880", command=lambda: click("9"))
p9.place(x=202, y=317, width=100, height=70)

#fnction calc


egal=Button(root,  text="=", fg="white", font=("Sans-serif", 20),background="#091880", relief=RAISED, command=evaluate)
egal.place(x=304, y=530, width=135, height=70)

clr= Button(root, font=("Sans-serif", 20), fg="white",text="clear", relief=RAISED, bg="red" , command=clear)
clr.place(x=305, y=317, width=68, height=70)
bac= Button(root, font=("Sans-serif", 20),fg="white",text="back", relief=RAISED, bg="red", command=back)
bac.place(x=374, y=317, width=68, height=70)
add= Button(root, font=("Sans-serif", 20),fg="white", text="+", relief=RAISED, bg="pink", command=lambda: click("+"))
add.place(x=305, y=388, width=68, height=70)
sou= Button(root, font=("Sans-serif", 20), fg="white",text="-", relief=RAISED, bg="pink", command=lambda: click("-"))
sou.place(x=374, y=388, width=68, height=70)
di= Button(root, font=("Sans-serif", 20),fg="white", text="/", relief=RAISED, bg="pink", command=lambda: click("/"))
di.place(x=305, y=460, width=68, height=70)
mul= Button(root, font=("Sans-serif", 20), fg="white",text="x", relief=RAISED, bg="pink", command=lambda: click("*"))
mul.place(x=374, y=460, width=68, height=70)
root.mainloop()



