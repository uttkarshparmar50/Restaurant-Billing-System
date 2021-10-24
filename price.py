from tkinter import*
from tkinter import messagebox
import random
import time
import datetime

root=Tk()
root.state('zoomed')
root.title("Restaurant Billing System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',40,'bold'),text="RESTAURANT BILLING SYSTEM",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
	if (Idly.get()==""):
		CoIdly='0'
	else:
		CoIdly=Idly.get()
	f=open('idly.txt','wt')
	f.write(CoIdly)
	f.close()

	if (Dosa.get()==""):
		CoDosa='0'
	else:
		CoDosa=Dosa.get()
	f=open('dosa.txt','wt')
	f.write(CoDosa)
	f.close()

	if (Noodles.get()==""):
		CoNoodles='0'
	else:
		CoNoodles=Noodles.get()
	f=open('noodles.txt','wt')
	f.write(CoNoodles)
	f.close()

	if (Pulav.get()==""):
		CoPulav='0'
	else:
		CoPulav=Pulav.get()
	f=open('pulav.txt','wt')
	f.write(CoPulav)
	f.close()

	if (Sweet.get()==""):
		CoSweet='0'
	else:
		CoSweet=Sweet.get()
	f=open('sweet.txt','wt')
	f.write(CoSweet)
	f.close()

     
	if (Drinks.get()==""):
		CoD='0'
	else:
		CoD=Drinks.get()
	f=open('drinks.txt','wt')
	f.write(CoD)
	f.close()

	messagebox.showinfo('','Prices are set successfully')
    
def qExit():
    root.destroy()

def Reset():
	Idly.set("")
	Dosa.set("")
	Noodles.set("")
	Drinks.set("")
	Pulav.set("")
	Sweet.set("")
    
#====================================Restaraunt Info 1===========================================================
Idly=StringVar()
Dosa=StringVar()
Noodles=StringVar()
Drinks=StringVar()
Pulav=StringVar()
Sweet=StringVar()


lblIdly= Label(f1, font=('arial', 16, 'bold'),text="Idly",bd=16,anchor="w")
lblIdly.grid(row=0, column=0)
txtIdly=Entry(f1, font=('arial',16,'bold'),textvariable=Idly,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtIdly.grid(row=0,column=1)


lblDosa= Label(f1, font=('arial', 16, 'bold'),text="Dosa",bd=16,anchor="w")
lblDosa.grid(row=1, column=0)
txtDosa=Entry(f1, font=('arial',16,'bold'),textvariable=Dosa,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDosa.grid(row=1,column=1)


lblNoodles= Label(f1, font=('arial', 16, 'bold'),text="Noodles",bd=16,anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNoodles.grid(row=2,column=1)

lblPulav= Label(f1, font=('arial', 16, 'bold'),text="Pulav",bd=16,anchor="w")
lblPulav.grid(row=2, column=2)
txtPulav=Entry(f1, font=('arial',16,'bold'),textvariable=Pulav,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPulav.grid(row=2,column=3)

lblSweet= Label(f1, font=('arial', 16, 'bold'),text="Sweet",bd=16,anchor="w")
lblSweet.grid(row=1, column=2)
txtSweet=Entry(f1, font=('arial',16,'bold'),textvariable=Sweet,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSweet.grid(row=1,column=3)

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Set Price",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

root.mainloop()
