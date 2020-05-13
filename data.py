import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="p4m18@bd"
)
print(mydb)
