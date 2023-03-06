import mysql.connector
from passwords import password1

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password1
)

mycursor = db.cursor()
mycursor.execute("insert into test1.test_table1 values(345, 'Himraj', 56, 45.67, 'sudh')")
db.commit()
db.close()
