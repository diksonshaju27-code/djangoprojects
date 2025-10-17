import mysql.connector
con=mysql.connector.connect(user="root",password="root",host="localhost",database="mydb")
#
c=con.cursor()
#
# c.execute('create table person(id int primary key,name varchar(20),age int)')
#
# print("Database File Created")

i=int(input("Enter The ID:"))
n=input("Enter Your Name:")
a=int(input("Enter The Age:"))

c.execute('INSERT INTO person VALUES (%s, %s, %s)', (i, n, a))

con.commit()

i=int(input("Enter The Id:"))
c.execute('SELECT * FROM person WHERE id = %s', (i,))

print(c.fetchall())