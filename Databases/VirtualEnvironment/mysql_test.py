import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='northwind'
)

mycursor = mydb.cursor()

sql = 'INSERT INTO northwind.Categories (CategoryID, CategoryName, Description, Picture) VALUES (%s, %s, %s, %s)'
val = (0,'Energy bar','I have the power', '')

mycursor.execute(sql, val)
mydb.commit()