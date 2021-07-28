import tkinter as tk
import csv
db=tk.Tk(__name__)
db.title('DATA FORM')
db.geometry('260x250')
db.config(bg='Black')
name=tk.Variable(db)
name.set('')
email=tk.Variable(db)
email.set('')
mobile=tk.Variable(db)
mobile.set('+91')
    
tk.Label(db, text="Name: ",font=('Arial',14,"bold"),bg='Black',fg='White',height=1).place(x=0,y=0)
tk.Entry(db,textvariable= name,font=('Times New Roman',13)).place(x=70,y=0)
tk.Label(db, text="Email: ",font=('Arial',14,"bold"),bg='Black',fg='White').place(x=0,y=30)
tk.Entry(db,textvariable= email,font=('Times New Roman',13),fg='Gray').place(x=70,y=30)
tk.Label(db, text="Mobile: ",font=('Arial',12,"bold"),bg='Black',fg='White').place(x=0,y=60)
tk.Entry(db,textvariable= mobile,font=('Times New Roman',13),fg='Gray').place(x=70,y=60)
   
def store():
    Name=name.get()
    Email=email.get()
    Mobile=mobile.get()
    with open('sris_data.csv','a') as data:
        datawriter=csv.writer(data)
        datawriter.writerow([Name,Email,Mobile])
        data.close()
    print("Submitted")
    name.set('')
    email.set('')
    mobile.set('+91')

tk.Button(db,text="SUBMIT",command=store,font=('Arial',16,"bold"),width=8,bg='Black',fg='White').place(x=120,y=150,anchor='center')    
db.mainloop()
