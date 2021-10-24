from tkinter import *

def login():
	u=e1.get()
	p=e2.get()
	if(u=='admin' and p=='admin'):
		root.destroy()
		import welcome
	else:
		l4.configure(text='Invalid Username/Password',fg='red')
root=Tk()
root.state('zoomed')
root.resizable(width=False,height=False)

l=Label(root,font=('arial',40,'bold'),text="RESTAURANT BILLING SYSTEM",fg="Steel Blue",bd=10,anchor='w')
l.pack()

l2=Label(root,text='Username:',font=('',20,'bold'))
l2.place(x=420,y=200)

l3=Label(root,text='Password:',font=('',20,'bold'))
l3.place(x=420,y=300)

l4=Label(root,text='',font=('',20,'bold'))
l4.place(x=520,y=120)

e1=Entry(root,font=('arial',16,'bold'),bg="powder blue",bd=10)
e1.place(x=600,y=200)

e2=Entry(root,font=('arial',16,'bold'),bg="powder blue",bd=10)
e2.place(x=600,y=300)

b=Button(root,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Login",bg="powder blue",command=login)

b.place(x=500,y=400)

root.mainloop()
