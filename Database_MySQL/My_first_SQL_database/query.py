import mysql.connector
from passwords import password1

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password1
)

mycursor = db.cursor()
mycursor.execute("select * from test1.test_table1")
for i in mycursor.fetchall():
    print(i)
