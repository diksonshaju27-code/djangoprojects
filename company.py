import sqlite3
con=sqlite3.connect("company.db")


# sql_command="create table employee(empid int primary key,name varchar(20),age int,gender varchar(10),salary int,place varchar(20))"
#
#
# con.execute(sql_command)
#
# print("Table Created!!!!1")

#
# con.execute("insert into employee(empid,name,age,gender,salary,place)values(100,'Dikson',20,'male',20000,'EKM')")
# con.execute("insert into employee(empid,name,age,gender,salary,place)values(101,'Greeshma',21,'female',15000,'IDK')")
# con.execute("insert into employee(empid,name,age,gender,salary,place)values(102,'Pranji',20,'male',25000,'EKM')")
# con.execute("insert into employee(empid,name,age,gender,salary,place)values(103,'Anusree',22,'female',25000,'IDK')")
# con.execute("insert into employee(empid,name,age,gender,salary,place)values(104,'Darshana',20,'female',280000,'EKM')")
# con.execute("insert into employee(empid,name,age,gender,salary,place)values(105,'Athulya',20,'female',34000,'UAE')")
# con.execute("insert into employee(empid,name,age,gender,salary,place)values(106,'Blessy',20,'female',37000,'EKM')")

# con.commit()

# #read operations
#
# k=con.execute('select * from employee')
# print(k.fetchall())
#
# k=con.execute('select name,age from employee')
# print(k.fetchall())
#
# k=con.execute('select name,age from employee where empid=100')
# print(k.fetchall())


#   LIMIT AND OFFSET
#read first row
#
# k=con.execute('select * from employee limit1')
# print(k.fetchall())
#
# #read first two  row
#
# k=con.execute('select * from employee limit2')
# print(k.fetchall())
#
# #read one row after skipping first row
#
# k=con.execute('select * from employee limit 1 offset 1')
# print(k.fetchall())
#
# #read one row after skipping first 2 rows
#
# k=con.execute('select * from employee limit 2 offset 2')
# print(k.fetchall())
#


# =,!=,<,>,>=,<= ,and,or,not,like,between,distint,orderby

#records having empid other than 102

# k=con.execute('select * from employee where empid!=102')
# print(k.fetchall())
#
# #records having salary >25000
#
# k=con.execute('select * from employee where salary>25000')
# print(k.fetchall())
#
# # #records hgaving age<27 or place ekm
# # k=con.execute('select * from employee where age<27 or place ekm')
# # print(k.fetchall())
#
# #records having age va;ue other than 27
# k=con.execute('select * from employee where not(age=27)')
# print(k.fetchall())
#
#

#BETWEEN-->

#record having age betwen 27 and 35

# k=con.execute('select * from employee where age between 27 and 35')
# print(k.fetchall())
#
# #records having salary between 20000 and 300000
#
# k=con.execute('select * from employee where salary between 20000 and 30000')
# print(k.fetchall())
#
# #record with salary 20000 or 30000
#
# k=con.execute('select * from employee where salary in(20000,30000)')
# print(k.fetchall())
#
# #records with salary other than 20000 and 30000
#
# k=con.execute('select * from employee where salary not in(20000,30000)')
# print(k.fetchall())
# #


# %--> 0 or more character
# _--> exactly one character

#3 letter name ending with U

# k=con.execute('select * from employee where name like "__U"')
# print(k.fetchall())
#
# #name ending with U
#
# k=con.execute('select * from employee where name like "%U"')
# print(k.fetchall())
#
# # 4letter starting with 'a'
#
# k=con.execute('select * from employee where name like "A___"')
# print(k.fetchall())
#
# # place name staring with letter k
#
# k=con.execute('select * from employee where name like "A%"')
# print(k.fetchall())
#
#
# #name contains letter n
#
# k=con.execute('select * from employee where name like "%n%"')
# print(k.fetchall())

#ORDER BY

#read recordds based on names

# k=con.execute('select * from employee order by name')
# print(k.fetchall())
#
# #read records based on salary
#
# k=con.execute('select * from employee order by salary')
# print(k.fetchall())
#
#
# #read recors based on slaray desending order
# k=con.execute('select * from employee order by salary desc')
# print(k.fetchall())
#
# #distint
#
# k=con.execute('select distinct(place) from employee')
# print(k.fetchall())


# print("Before Updation")
# k=con.execute('select * from employee')
# print(k.fetchall())
#
# con.execute('update employee set age=28,salary=40000 where empid=101')
# con.commit()
#
# print("After Updation")
# k=con.execute('select * from employee')
# print(k.fetchall())

#
# print("Before Deletion")
# k=con.execute('select * from employee')
# print(k.fetchall())
#
# con.execute('delete from employee where empid=103')
# con.commit()
#
# print("After Deletion")
# k=con.execute('select * from employee')
# print(k.fetchall())


# To add new collumn Email

# con.execute('alter table employee add column email varchar(30)')
# k=con.execute('select *  from employee')
# print(k.fetchall())

# To Deleete A comlum
#
# con.execute('alter table employee drop column email')

#Aggeragate functions

# k=con.execute('select sum(salary),min(age),max(age),count(*),avg(salary) from employee')
# print(k.fetchall())

#group by having

#
# k=con.execute('select place,sum(salary) from employee group by place')
# print(k.fetchall())

k=con.execute('select gender,max(age) from employee group by gender')
print(k.fetchall())