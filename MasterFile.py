import tkinter as tk
from tkinter import ttk

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Login, SignUpIntro, SignUpCustomer, SignUpAdmin, SignUpSupplier, SignUpComplete):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Login)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AMZKART", font=('Arial',40))
        label.pack(padx=20,pady=20)
        label = tk.Label(self, text = "Login", font=('Arial', 16))
        label.pack(padx=100,pady=100)

        label = tk.Label(self, text = "Username", font=('Arial', 14))
        label.place(x=350, y=335)

        options = [
            "Customer",
            "Admin",
            "Supplier"
        ]

        clicked = tk.StringVar(self)
        clicked.set("Customer")


        label = tk.Label(self, text = "Login As", font=('Arial', 14))
        label.place(x=350, y=270)

        drop = tk.OptionMenu( self , clicked , *options)
        drop.place(x=500,y=270)

        def retrieve_input():
            inputName=textBox1.get()
            inputPwd=textBox2.get()
            accType = clicked.get()
            print(inputName, inputPwd, accType)

            import mysql.connector 

            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')

            if(conn):
                print('connection successfull')

            else:
                print('connection failed')

            mycursor = conn.cursor()

            
            count1 = 0
            
            inputName = '"'+inputName+'"'
            inputPwd = '"'+inputPwd+'"'
            mycursor.execute('Select * from Login where Username = '+inputName+' AND Password = '+inputPwd)

            myresult = mycursor.fetchall()
            

            for row in myresult:
                count1 = count1+1
                

            if count1 > 0:
                print('Login Succesfull')
            else:
                print('Invalid credetials')  

        textBox1=tk.Entry(self,width=20)
        textBox1.place(x=500,y=342)

        label = tk.Label(self, text = "Password", font=('Arial', 14))
        label.place(x=350, y=400)

        textBox2=tk.Entry(self,width=20, show="*")
        textBox2.place(x=500,y=405)



        buttonCommit=tk.Button(self, height=1, width=10, text="Login", 
                    command=lambda: retrieve_input())

        buttonCommit.place(x=450, y=500)

        label = tk.Label(self, text = "Not a Member? Sign up!", font=('Arial', 14))
        label.place(x=200, y=600)

        buttonCommit=tk.Button(self, height=1, width=10, text="SignUp", 
                    command=lambda: controller.show_frame(SignUpIntro))
        buttonCommit.place(x=550, y=600)

class SignUpIntro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AMZKART - Sign up!", font=('Arial',40))
        label.pack(padx=20,pady=20)

        label = tk.Label(self, text = "Account Type", font=('Arial', 14))
        label.place(x=350, y=270)

        options = [
            "Customer",
            "Admin",
            "Supplier"
        ]

        clicked = tk.StringVar(self)
        clicked.set("Customer")

        drop = tk.OptionMenu(self, clicked , *options)
        drop.place(x=500,y=270)

        def retrieve_input():
            accType = clicked.get()
            if accType == "Customer":
                controller.show_frame(SignUpCustomer)
            elif accType == "Admin":
                controller.show_frame(SignUpAdmin)
            elif accType == "Supplier":
                controller.show_frame(SignUpSupplier)

        buttonCommit = tk.Button(self, height=1, width=10, text="Continue",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=450, y=400)

class SignUpCustomer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="AMZKART - Customer Sign up!", font=('Arial',40))
        label.pack(padx=20,pady=20)

        label = tk.Label(self, text = "Personal Details", font=('Arial', 15))
        label.place(x=250, y=125)
        
        label = tk.Label(self, text = "Create Username", font=('Arial', 10))
        label.place(x=350, y=175)

        textBox1=tk.Entry(self,width=20)
        textBox1.place(x=550,y=175)

        label = tk.Label(self, text = "Create Password", font=('Arial', 10))
        label.place(x=350, y=200)

        textBox2=tk.Entry(self,width=20, show="*")
        textBox2.place(x=550,y=200)

        label = tk.Label(self, text = "First Name", font=('Arial', 10))
        label.place(x=350, y=225)

        textBox3=tk.Entry(self,width=20)
        textBox3.place(x=550,y=225)

        label = tk.Label(self, text = "Last Name", font=('Arial', 10))
        label.place(x=350, y=250)

        textBox4=tk.Entry(self,width=20)
        textBox4.place(x=550,y=250)

        label = tk.Label(self, text = "Phone", font=('Arial', 10))
        label.place(x=350, y=275)

        textBox5=tk.Entry(self,width=20)
        textBox5.place(x=550,y=275)

        label = tk.Label(self, text = "Email", font=('Arial', 10))
        label.place(x=350, y=300)

        textBox6=tk.Entry(self,width=20)
        textBox6.place(x=550,y=300)

        label = tk.Label(self, text = "Add Primary Delivery Address", font=('Arial', 15))
        label.place(x=250, y=335)

        label = tk.Label(self, text = "Street Address", font=('Arial', 10))
        label.place(x=350, y=385)

        textBox7=tk.Entry(self,width=20)
        textBox7.place(x=550,y=385)

        label = tk.Label(self, text = "City", font=('Arial', 10))
        label.place(x=350, y=410)

        textBox8=tk.Entry(self,width=20)
        textBox8.place(x=550,y=410)

        label = tk.Label(self, text = "Postal Code", font=('Arial', 10))
        label.place(x=350, y=435)

        textBox9=tk.Entry(self,width=20)
        textBox9.place(x=550,y=435)

        label = tk.Label(self, text = "Country", font=('Arial', 10))
        label.place(x=350, y=460)

        textBox10=tk.Entry(self,width=20)
        textBox10.place(x=550,y=460)

        label = tk.Label(self, text = "Add Primary Debit/Credit Card", font=('Arial', 15))
        label.place(x=250, y=495)

        label = tk.Label(self, text = "Card Number", font=('Arial', 10))
        label.place(x=350, y=545)

        textBox11=tk.Entry(self,width=20)
        textBox11.place(x=550,y=545)

        label = tk.Label(self, text = "Card Expiry Date", font=('Arial', 10))
        label.place(x=350, y=570)

        textBox12=tk.Entry(self,width=20)
        textBox12.place(x=550,y=570)

        label = tk.Label(self, text = "CVV/Pin", font=('Arial', 10))
        label.place(x=350, y=595)

        textBox13=tk.Entry(self,width=20)
        textBox13.place(x=550,y=595)

        def retrieve_input():
            
            Username = '"'+textBox1.get()+'"'
            Password = '"'+textBox2.get()+'"'
            Fname  = '"'+textBox3.get()+'"'
            Lname = '"'+textBox4.get()+'"'
            Phone = '"'+textBox5.get()+'"'
            Email = '"'+textBox6.get()+'"'
            Address = '"'+textBox7.get()+'"'
            City = '"'+textBox8.get()+'"'
            Pcode = textBox9.get()
            Country = '"'+textBox10.get()+'"'
            Cno =  textBox11.get()
            Cexp = '"'+textBox12.get()+'"'
            Cpin = textBox13.get()


            import mysql.connector 

            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')

            if(conn):
                print('connection successfull')

            else:
                print('connection failed')

            mycursor = conn.cursor()

            mycursor.execute('INSERT INTO Customer (FirstName,LastName,Phone,Email,Address,City,PostalCode,Country) VALUES ('+Fname+','+Lname+','+Phone+','+Email+','+Address+','+City+','+Pcode+','+Country+');')
            
            conn.commit()

            

            Result = mycursor.execute('Select CustomerID from Customer where Email = '+Email)

            Result = mycursor.fetchone()
            
            TypeID = Result[0]

            

            mycursor.execute('INSERT INTO Login (Username,Password,Acc_Type,ReferenceID) VALUES ('+Username+','+Password+',"Customer",'+str(TypeID)+');')

            conn.commit()

            mycursor.execute('INSERT INTO CARD_Details (CustomerID,Card_Number,Card_Pin,Card_Exp_Date,Name_On_Card,Billing_Addr) VALUES ('+str(TypeID)+','+Cno+','+Cpin+','+Cexp+','+Fname+','+Address+');')


            conn.commit()


            controller.show_frame(SignUpComplete)

        buttonCommit = tk.Button(self, height=1, width=10, text="Sign Up",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=450, y=800)

class SignUpComplete(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Sign Up Complete!", font=('Arial',40))
        label.pack(padx=20,pady=20)
        label = tk.Label(self, text = "Please go to Login page and Sign in with your created details", font=('Arial', 16))
        label.pack(padx=100,pady=100)

        def retrieve_input():
            #accType = clicked.get()
            controller.show_frame(Login)

        buttonCommit = tk.Button(self, height=1, width=10, text="Login",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=450, y=400)

class SignUpAdmin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AMZKART - Admin Sign up!", font=('Arial',40))
        label.pack(padx=20,pady=20)

        label = tk.Label(self, text = "Account Type", font=('Arial', 14))
        label.place(x=350, y=270)

        def retrieve_input():
            #accType = clicked.get()
            print("hello")

        buttonCommit = tk.Button(self, height=1, width=10, text="Continue",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=450, y=400)

import tkinter as tk
from tkinter import ttk

class SignUpSupplier(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AMZKART - Supplier Sign up!", font=('Arial',40))
        label.pack(padx=20,pady=20)

        label = tk.Label(self, text = "Account Type", font=('Arial', 14))
        label.place(x=350, y=270)

        def retrieve_input():
            #accType = clicked.get()
            print("hello")

        buttonCommit = tk.Button(self, height=1, width=10, text="Continue",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=450, y=400)
root = tkinterApp()
root.geometry("1000x1000")
root.mainloop()