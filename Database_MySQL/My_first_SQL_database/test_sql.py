import mysql.connector
from passwords import password1

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password1,
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
    