from tkinter import*
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
        CoIdly=0
    else:
        CoIdly=float(Idly.get())


    
    if (Dosa.get()==""):
        CoDosa=0
    else:
        CoDosa=float(Dosa.get())



    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())



    if (Pulav.get()==""):
        CoPulav=0
    else:
        CoPulav=float(Pulav.get())

        
    if (Sweet.get()==""):
        CoSweet=0
    else:
        CoSweet=float(Sweet.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofIdly =CoIdly * float(open('idly.txt').read())
    CostofDrinks=CoD * float(open('drinks.txt').read())
    CostofDosa = CoDosa* float(open('dosa.txt').read())
    CostofNoodles = CoNoodles * float(open('noodles.txt').read())
    CostPulav = CoPulav* float(open('pulav.txt').read())
    CostSweet=CoSweet * float(open('sweet.txt').read())

    CostofMeal= "Rs", str('%.2f' % (CostofIdly+CostofDrinks+CostofDosa+CostofNoodles+CostPulav+CostSweet))

    PayTax=((CostofIdly+CostofDrinks+CostofDosa+CostofNoodles+CostPulav+CostSweet) * 0.2)

    TotalCost=(CostofIdly+CostofDrinks+CostofDosa+CostofNoodles+CostPulav+CostSweet)
 
    Ser_Charge= ((CostofIdly+CostofDrinks+CostofDosa+CostofNoodles+CostPulav+CostSweet)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
	x=random.randint(10908,500876)
	randomRef=str(x)
	rand.set(randomRef)
	Idly.set("")
	Dosa.set("")
	Noodles.set("")
	SubTotal.set("")
	Total.set("")
	Service_Charge.set("")
	Drinks.set("")
	Tax.set("")
	Cost.set("")
	Pulav.set("")
	Sweet.set("")
    
#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Idly=StringVar()
Dosa=StringVar()
Noodles=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Pulav=StringVar()
Sweet=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Bill No",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

x=random.randint(10908,500876)
randomRef=str(x)
rand.set(randomRef)

lblIdly= Label(f1, font=('arial', 16, 'bold'),text="Idly",bd=16,anchor="w")
lblIdly.grid(row=1, column=0)
txtIdly=Entry(f1, font=('arial',16,'bold'),textvariable=Idly,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtIdly.grid(row=1,column=1)


lblDosa= Label(f1, font=('arial', 16, 'bold'),text="Dosa",bd=16,anchor="w")
lblDosa.grid(row=2, column=0)
txtDosa=Entry(f1, font=('arial',16,'bold'),textvariable=Dosa,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDosa.grid(row=2,column=1)


lblNoodles= Label(f1, font=('arial', 16, 'bold'),text="Noodles",bd=16,anchor="w")
lblNoodles.grid(row=3, column=0)
txtNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNoodles.grid(row=3,column=1)

lblPulav= Label(f1, font=('arial', 16, 'bold'),text="Pulav",bd=16,anchor="w")
lblPulav.grid(row=4, column=0)
txtPulav=Entry(f1, font=('arial',16,'bold'),textvariable=Pulav,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPulav.grid(row=4,column=1)

lblSweet= Label(f1, font=('arial', 16, 'bold'),text="Sweet",bd=16,anchor="w")
lblSweet.grid(row=5, column=0)
txtSweet=Entry(f1, font=('arial',16,'bold'),textvariable=Sweet,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSweet.grid(row=5,column=1)

#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)


root.mainloop()


