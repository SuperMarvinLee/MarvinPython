import mysql.connector

mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    passwd='marvinlee'
)

mycursor = mydb.cursor()
mycursor.execute('show databases')

for item in mycursor:
    print(item)