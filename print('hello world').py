import mysql.connector 

conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'NEW')

if(conn):
    print('connection successfull')

else:
    print('connection failed')

accType = 'Customer'

mycursor = conn.cursor()

mycursor.execute('Select * from Customer')

myresult = mycursor.fetchall()


for row in myresult:
    print(row)

