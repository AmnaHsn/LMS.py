import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",port=3306,password="",database="library management system")
cursor= conn.cursor()
selectquery="select * from librarian"
cursor.execute(selectquery)
records=cursor.fetchall()
print("librarian", cursor.rowcount)

for row in records:
  print("Librarian_name",row[0])
  print("Librarian_ID",row[1])
  print()

cursor.close()
conn.close()
