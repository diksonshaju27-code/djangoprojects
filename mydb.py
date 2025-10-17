import mysql.connector
from twisted.internet.defer import passthru

# con=mysql.connector.connect(user="root",password="root",host="localhost")
#
# c=con.cursor()
#
# c.execute("create database mydb")
#
# print("Database File Created")

con=mysql.connector.connect(user="root",password="root",host="localhost",database="company")

c=con.cursor()

# c.execute("""create table employee
#           (empid int primary key,
#            name varchar(20),age int,
#            place varchar(20),salary int,
#            gender varchar(10))""")
#
# print("Table Created")



# c.execute('''insert into employee values(100,"arun",23,"ekm",30000,"male"),
#                                         (101,"amal",25,"tvm",35000,"male"),
#                                         (103,"nourin",22,"ekm",25000,"female"),
#                                         (104,"vimal",23,"klm",30000,"male"),
#                                         (105,"malavika",25,"kzk",30000,"female")''')
# print("inserted data")
# con.commit()


c.execute('select * from employee')
k=c.fetchall()
print(k)


