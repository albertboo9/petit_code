
from tkinter import *
from math import sqrt
fenetre=Tk()

def aff(n):
	a=myEntry.get()
	var.set(a+n)

def retour():
	a=myEntry.get()
	l=""
	for i in range(len(a)-1):
		l+=a[i]
	var.set(l)

def dernier_index(L,c):
	i=len(L)-1
	while i>=0:
		if L[i]==c:
			return i
		i=i-1

def pro(L,a):
	for i in range(len(L)):
		if L[i]==a:
			return 1
	return 0

def sansop(L):
	op1=['+','-','÷','×','√','²',',','%']
	for i in range(len(L)-1):
		if ((L[i] in op1) or  (L[i+1] in op1))==False:
			return 1
	return 0

def nchiffre(n):
	i=0
	while n!=0:
		i+=1
		n=n//10
	return i


def operation(L):
	op=['+','-','÷','×','%',',']
	op1=['+','-','÷','×','√','²',',','%']
	op2=['÷','×','%','²']
	(a,b,c,d,e)=(0,0,0,0,0)
	k=0
	if L[0] in op2:
		return None
	for i in range(len(L)-1):
		if L[i] in op and L[i+1] in op:
			return None
	
	for i in range(len(L)-2):
		if L[i] ==',' and L[i+2]==',':
			return None
	while '(' in L:
		l=[]
		j=dernier_index(L,'(')+1
		if L[j]==')':
			return None
		while  j<=len(L)-1:
			if L[j]!=')':
				l.append(L[j])
				del L[j]
			if j==len(L):
				j-=1
				k=1
			if (k==0 and L[j]==')') or k==1 :
				re=operation(l)
				if re==None:
					return None
				else:
					L[dernier_index(L,'(')]=re
					break
		if k==0:
			del L[j]
	while len(L)!=1:
		j=0
		while pro(L,',')==1:
			if L[j]==',':
				if j!=0 and ((L[j-1] in op1)==False):
					L[j-1]+=L[j+1]/pow(10,nchiffre(L[j+1]))
					del L[j]
					del L[j]
				elif j!=0 and L[j-1] in op1:
					L[j]=L[j+1]/pow(10,nchiffre(L[j+1]))
					del L[j+1]
				else:
					L[j]=L[j+1]/pow(10,nchiffre(L[j+1]))
					del L[j+1]
			else:
				j+=1
		while pro(L,'√')==1:
			j=dernier_index(L,'√')
			if L[j]=='√':
				if L[j+1] in op1 or L[j+1]<0:
					return None
				else:
					L[j]=sqrt(L[j+1])
					del L[j+1]
			else:
				j+=1
		j=1
		while pro(L,'²')==1:
			if L[j]=='²':
				L[j-1]=pow(L[j-1],2)
				del L[j]
			else:
				j+=1
		j=0
		while pro(L,'%')==1:
			if L[j]=='%':
				L[j-1]=L[j-1]%L[j+1]
				del L[j]
				del L[j]
			else:
				j+=1
		j=0
		while  sansop(L)==1:
			if ((L[j] in op1) or  (L[j+1] in op1))==False:
				L[j]=L[j]*L[j+1]
				del L[j+1]
			else:
				j+=1
		j=0
		while pro(L,'÷')==1:
			if L[j]=='÷':
				if L[j+1]==0:
					return None
				if L[j-1]/L[j+1]-int(L[j-1]/L[j+1])==0:
					L[j-1]=int(L[j-1]/L[j+1])
				else:
					L[j-1]=L[j-1]/L[j+1]
				del L[j]
				del L[j]
			else:
				j+=1
		j=0
		while  pro(L,'×')==1:
			if L[j]=='×' :
				L[j-1]=L[j-1]*L[j+1]
				del L[j]
				del L[j]
			else:
				j+=1
		j=0
		while pro(L,'-')==1:
			if L[j]=='-':
				if j!=0:
					L[j-1]=L[j-1]-L[j+1]
					del L[j]
					del L[j]
				else:
					L[j]=-L[j+1]
					del L[j+1]
			else:
				j+=1
		j=0
		while pro(L,'+')==1:
			if L[j]=='+':
				if j!=0:
					L[j-1]=L[j-1]+L[j+1]
					del L[j]
					del L[j]
				else:
					L[j]=L[j+1]
					del L[j+1]
			else:
				j+=1
	return L[0]

def egal():
	n=0
	resul=0
	j=0
	k=0
	op=['+','-','÷','×',')','(','√','²',',','%']
	op1=['+','-','÷','×','(','√',',','%']
	op2=['÷','×','%',')','²']
	possible=['0','1','2','3','4','5','6','7','8','9','+','-','÷','×','√','²',',','%',')','(']
	l=[]
	a=myEntry.get()
	for i in range(len(a)):
		if (a[i] in possible)==False:
			return None
	for i in range(len(a)):
		if (a[i] in op)==False:
			n*=10
			n+=int(a[i])
			k=1
		elif  a[i] in op:
			if k==1:
				l.append(n)
				k=0
			l.append(a[i])
			n=0
		if i==len(a)-1 :
			if (a[i] in op):
				pass
			else:
				l.append(n)
	i=len(l)-1
	if len(l)!=0:
		if l[i] in op1 or l[0] in op2:
			resul=None
		else:
			resul1=operation(l)
			resul=resul1
			if resul1!=None:
				if resul1-int(resul1)==0:
					resul1=str(int(resul1))
				else:
					resul1=str(resul1)
				resul=""
				for i in range(len(resul1)):
					if resul1[i]=='.':
						resul+=","
					else:
						resul+=resul1[i]
				
		if resul==None:
			message["text"]="error"
		else:
			message["text"]="{}  =   {} ".format(a, resul)
	

def boutton():
	# premiere colone
	boutton=Button(fenetre, text='0',command=lambda x="0":aff(x))
	boutton.place(width=60,height=30, x=10, y=310)
	boutton=Button(fenetre, text='1',command=lambda x="1":aff(x))
	boutton.place(width=60,height=30, x=10, y=275)
	boutton=Button(fenetre, text='4',command=lambda x="4":aff(x))
	boutton.place(width=60,height=30, x=10, y=240)
	boutton=Button(fenetre, text='7',command=lambda x="7":aff(x))
	boutton.place(width=60,height=30, x=10, y=205)
	# deuxieme colone
	boutton=Button(fenetre, text=',',command=lambda x=",":aff(x))
	boutton.place(width=60,height=30, x=75, y=310)
	boutton=Button(fenetre, text='2',command=lambda x="2":aff(x))
	boutton.place(width=60,height=30, x=75, y=275)
	boutton=Button(fenetre, text='5',command=lambda x="5":aff(x))
	boutton.place(width=60,height=30, x=75, y=240)
	boutton=Button(fenetre, text='8',command=lambda x="8":aff(x))
	boutton.place(width=60,height=30, x=75, y=205)
	# troisieme colone
	boutton=Button(fenetre, text='%',command=lambda x="%":aff(x))
	boutton.place(width=60,height=30, x=140, y=310)
	boutton=Button(fenetre, text='3',command=lambda x="3":aff(x))
	boutton.place(width=60,height=30, x=140, y=275)
	boutton=Button(fenetre, text='6',command=lambda x="6":aff(x))
	boutton.place(width=60,height=30, x=140, y=240)
	boutton=Button(fenetre, text='9',command=lambda x="9":aff(x))
	boutton.place(width=60,height=30, x=140, y=205)
	# quatrieme colone
	boutton=Button(fenetre, text='+',command=lambda x="+":aff(x))
	boutton.place(width=60,height=30, x=205, y=310)
	boutton=Button(fenetre, text='-',command=lambda x="-":aff(x))
	boutton.place(width=60,height=30, x=205, y=275)
	boutton=Button(fenetre, text='×',command=lambda x="×":aff(x))
	boutton.place(width=60,height=30, x=205, y=240)
	boutton=Button(fenetre, text='÷',command=lambda x="÷":aff(x))
	boutton.place(width=60,height=30, x=205, y=205)
	# les deux dernieres colones
	boutton=Button(fenetre, text='=',command=egal)
	boutton.place(width=60*2+5,height=30, x=270, y=310)
	boutton=Button(fenetre, text='x²',command=lambda x="²":aff(x))
	boutton.place(width=60,height=30, x=270, y=275)
	boutton=Button(fenetre, text='√',command=lambda x="√":aff(x))
	boutton.place(width=60,height=30, x=335, y=275)
	boutton=Button(fenetre, text='c',command=lambda : var.set(""))
	boutton.place(width=60,height=30, x=335, y=205)
	boutton=Button(fenetre, text='(',command=lambda x="(":aff(x))
	boutton.place(width=60,height=30, x=270, y=240)
	boutton=Button(fenetre, text=')',command=lambda x=")":aff(x))
	boutton.place(width=60,height=30, x=335, y=240)
	boutton=Button(fenetre, text='←',command=retour)
	boutton.place(width=60,height=30, x=270, y=205)

message=Label(fenetre, text="")
message.place(width=402.5,height=30, x=20, y=110)
var=StringVar()
myEntry=Entry(fenetre,textvariable=var,width=40)
myEntry.place(width=402.5,height=60, x=0, y=140)
boutton()
fenetre.geometry("405x350")
fenetre.mainloop()
