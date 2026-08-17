from db import conn,cursor

# data insert
def add_stud():
    name=input("enter your name:")
    age=int(input("enter your age:"))
    cursor.execute("insert into student(name,age) values(%s,%s)",(name,age))
    conn.commit()
    print("data saved")
    print("======================================")


def get_stud():
    cursor.execute("select * from student")
    rows=cursor.fetchall()
    print("student details are:")
    for row in rows:
        print(row)
    print("======================================")


def get_names_age():
    cursor.execute("select name from student where age > 5")
    rows = cursor.fetchall()
    print("student names whose age is greater than 5:")
    for row in rows:
        print(row[0])
    print("======================================")


def id_age():
    cursor.execute("select id,age from student where name like '%a%'")
    rows = cursor.fetchall()
    print("student id and age whose name contains 'a':")
    for row in rows:
        print(row[0], row[1])
    print("======================================")


def even_id():
    cursor.execute("select * from student where id%2=0")
    rows = cursor.fetchall()
    print("student details whose id is even:")
    for row in rows:
        print(row)
    print("======================================")


def count_total_students():
    cursor.execute("select count(*) from student")
    total = cursor.fetchone()[0]
    print("total number of students:", total)
    print("======================================")

def max_age():
    cursor.execute("select max(age) from student")
    max_age = cursor.fetchone()[0]
    print("maximum age of students:", max_age)
    print("======================================")
