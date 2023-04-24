import tkinter as tk

root = tk.Tk()

root.geometry("1000x1000")
root.title("Signup Page")

label = tk.Label(root, text="AMZKART - Sign up!", font=('Arial',40))
label.pack(padx=20,pady=20)

label = tk.Label(root, text = "Account Type", font=('Arial', 14))
label.place(x=350, y=200, height = 300)

options = [
    "Customer",
    "Admin",
    "Supplier"
]

clicked = tk.StringVar()
clicked.set("Customer")

drop = tk.OptionMenu( root , clicked , *options )
drop.place(x=500,y=342)

root.mainloop()