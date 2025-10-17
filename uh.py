import mysql.connector
con=mysql.connector.connect(user='root',password='root',host='localhost')
c=con.cursor()
c.execute('create database shopdb')
print('shopdb created')
# #
# con=mysql.connector.connect(user='root',password='root',host='localhost',database='shopdb')
# c=con.cursor()
# c.execute("""create table product
#              (pid int primary key,
#               pname varchar(20),
#               price int)""")
# print("table created")

# c.execute("""create table Order_details
#              (orderid int primary key,
#               pid int,
#               order_date date,
#               quantity int,
#               foreign key(pid) references product(pid))""")
# print("table created")
# c.execute('''insert into product values(1,"prodA",200),
#                                         (2,"prodB",500),
#                                         (3,"prodC",300),
#                                         (4,"prodD",1000)''')
# print("inserted data")
# c.execute('''insert into Order_details values
#              (100301,3,"2025-08-13",2),
#              (100302,2,"2025-08-16",3)''')
# print("inserted data")
# c.execute("select * from employee")
# k=c.fetchall()
# print(k)
# con.commit()