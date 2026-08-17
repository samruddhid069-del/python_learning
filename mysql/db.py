# import mysql.connector
# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="sms"
# )

# print("database connected successfully")

# cursor.execute("""
# create table if not exists student (
#  id int auto_increment primary key,
#  name varchar(100) not null,
#  age int check(age > 18)
# )
# """)

# print("table created")


import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sms"
)

print("database connected successfully")

cursor = conn.cursor()   # ✅ FIRST create cursor

cursor.execute("""
create table if not exists student (
 id int auto_increment primary key,
 name varchar(100) not null,
 age int check(age > 18)
)
""")

print("table created")