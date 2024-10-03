
#importation des modules
from tkinter import *
import math as m

#fenêtre
root = Tk()
root.title("CALCULATRICE SCIENTIFIQUE")
root.geometry("442x600")
root.configure(background="#091821")
root.resizable(False, False)
e = Entry(root, width=100, font=("Sans serif", 27), fg='black', bg='white')
e.place(x=0, y=0, height=90)





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
        result = str(m.sin(float(no)))
    if text=='cos':
        result = str(m.cos(float(no)))
    if text=='tan':
        result = str(m.tan(float(no)))
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
    if text=='Pi':
        if no=="":
            result=str(m.pi)
        else:
            result=str(float(no)*m.pi)
    if text=='E':
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
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)

log = Button(root, text="log", relief=RAISED)
log.bind("<Button-1>", sc)
log.place(x=2, y= 140, width=70, height=40)
ln=Button(root, text="ln", relief=RAISED)
ln.bind("<Button-1>", sc)
ln.place(x=74, y=140,width=70, height=40 )
par1 = Button(root, text="(",  relief=RAISED, command=lambda: click("("))
par1.place(x=147, y=140,width=70, height=40)
par2 = Button(root, text=")",  relief=RAISED, command=lambda: click(")"))
par2.place(x=220, y=140,width=70, height=40)
inv = Button(root, text="1/x", relief=RAISED)
inv.bind("<Button-1>", sc)
inv.place(x=294, y=140,width=70, height=40)
rc= Button(root, text="Sqrt", relief=RAISED)
rc.bind("<Button-1>", sc)
rc.place(x=369, y=140,width=70, height=40)
si= Button(root, text="sin", relief=RAISED)
si.bind("<Button-1>", sc)
si.place(x=0, y= 188,width=70, height=40)
co = Button(root, text="cos", relief=RAISED)
co.bind("<Button-1>", sc)
co.place(x=74, y= 188,width=70, height=40)
ta = Button(root, text="tan", relief=RAISED)
ta.bind("<Button-1>", sc)
ta.place(x=147, y= 188,width=70, height=40)
fac = Button(root, text="x!", relief=RAISED)
fac.bind("<Button-1>", sc)
fac.place(x=220, y= 188,width=70, height=40)
deg= Button(root, text="deg", relief=RAISED)
deg.bind("<Button-1>", sc)
deg.place(x=294, y= 188,width=70, height=40)
ex = Button(root, text="E", relief=RAISED)
ex.bind("<Button-1>", sc)
ex.place(x=369, y= 188,width=70, height=40)









root.mainloop()



