import tkinter as tk
import asyncio

root = tk.Tk()

root.geometry("1000x1000")
root.title("Login Page")

label = tk.Label(root, text="AMZKART", font=('Arial',40))
label.pack(padx=20,pady=20)

label = tk.Label(root, text = "Login", font=('Arial', 16))
label.pack(padx=100,pady=100)

label = tk.Label(root, text = "Username", font=('Arial', 14))
label.place(x=350, y=335)

options = [
    "Customer",
    "Admin",
    "Supplier"
]

clicked = tk.StringVar(root)


label = tk.Label(root, text = "Login As", font=('Arial', 14))
label.place(x=350, y=270)

drop = tk.OptionMenu( root , clicked , *options)
drop.place(x=500,y=270)

def retrieve_input():
    inputName=textBox1.get()
    inputPwd=textBox2.get()
    accType = clicked.get()
    count1 = 0
    import mysql.connector 

    conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Ecommerce')

    if(conn):
        print('connection successfull')

    else:
        print('connection failed')

    mycursor = conn.cursor()

    

    
    inputName = '"'+inputName+'"'
    inputPwd = '"'+inputPwd+'"'
    mycursor.execute('Select Lname from Customer where Fname = '+inputName+' AND Password = '+inputPwd)

    myresult = mycursor.fetchall()
    
    print

    for row in myresult:
        count1 = count1+1
        

    if count1 > 0:
        print('Login Succesfull')
    else:
        print('Invalid credetials')  

textBox1=tk.Entry(root,width=20)
textBox1.place(x=500,y=342)

label = tk.Label(root, text = "Password", font=('Arial', 14))
label.place(x=350, y=400)

textBox2=tk.Entry(root,width=20)
textBox2.place(x=500,y=405)



buttonCommit=tk.Button(root, height=1, width=10, text="Login", 
                    command=lambda: retrieve_input())

buttonCommit.place(x=450, y=500)


label = tk.Label(root, text = "Password", font=('Arial', 14))
label.place(x=350, y=400)



root.mainloop()























































