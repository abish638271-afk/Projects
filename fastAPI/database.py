import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dsec@123",
    database="testdb"
)

cursor = conn.cursor()
print("successfully connected")