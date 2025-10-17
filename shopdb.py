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

con=mysql.connector.connect(user="root",password="root",host="localhost",database="shopdb")
c=con.cursor()
# c.execute("create database library")
# print('tasksql created')

# c.execute("create table Author (author_id int primary key,name varchar(20),nationality varchar(15),birthyear date)")
# c.execute("create table Books (bookno int primary key,title varchar(20),author_id int,price int,pages int,published_year int,foreign key (author_id) references author(author_id))")
#
# c.execute("insert into Author values(1,'john','American','1995-02-20'),(2,'Arun','Indian','1998-04-20'),(3,'jacob','Italian','1990-07-26')")
# con.commit()
#
# c.execute("insert into Books values(1,'Python',1,2000,100,2005),(2,'DSA',2,500,150,2010),(3,'django',1,1000,150,2019),(4,'OOP',3,1200,120,2018)")
# con.commit()
#
# c.execute("select * from Author inner join Books on Author.author_id=Books.author_id where Author.author_id=1")
# k=c.fetchall()
# print(k)

# c.execute("select published_year from Books where bookno=1")
# k=c.fetchall()
# print(k)
#
# c.execute("select name from Author where birthyear=(select max(birthyear) from Author)")
# k=c.fetchall()
# print(k)

# c.execute("select title,name from Author inner join Books on Author.author_id=Books.author_id where Books.title like ('%yt%')")
# k=c.fetchall()
# print(k)

c.execute("select name from Author inner join Books on Author.author_id=Books.author_id where Books.published_year>2005")
k=c.fetchall()
print(k)