# # Books  --bookno,title,author id(foreign),price,pages,published year
# #
# # Author ---author_id,name,nationality,birthyear
# #
# # 1,Find all books of specific author

# # 2.Find the publication year of a particular book

# # 3.Find the youngest author

# # 4.List books with their corresponding author where booktitle contains a specific keyword
#

#
# # 5.list all authors who have written books published after a particular year.
#

import mysql.connector
# con=mysql.connector.connect(user='root',password='root',host='localhost')
# c=con.cursor()
# c.execute('create database tasksql')
print('tasksql created')

# import mysql.connector
con=mysql.connector.connect(user="root",password="root",host="localhost",database="tasksql")
#
c=con.cursor()

# c.execute('CREATE TABLE author (author_id INT PRIMARY KEY, name VARCHAR(20), nationality VARCHAR(20), birth_year INT)')
#
# print("Database File Created")

# i=int(input("Enter The Author ID:"))
# n=input("Enter Your Name:")
# a=input("Enter The Nationality:")
# d=int(input("Enter the birth year:"))
#
# c.execute('INSERT INTO author VALUES (%s, %s, %s, %s)', (i, n, a, d))
#
#
# con.commit()
