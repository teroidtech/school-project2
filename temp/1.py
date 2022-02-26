import mysql.connector as mysql

connectr = mysql.connect(host="localhost", passwd="admin", user="root")
cursor = connectr.cursor()
a = cursor.execute("show databases")
# cursor.execute("use school")
# c = cursor.fetchall()
print(a)

