import mysql.connector
from passwords import password1

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password1
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test1")
mycursor.execute("CREATE TABLE if not exists test1.test_table1 (c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(30))")
mydb.close()