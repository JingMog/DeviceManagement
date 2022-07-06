import pymysql

host = 'your host'
user = 'your username'
password = 'your password'

# 连接数据库
def connect():
    connect = pymysql.connect(
        host= host,
        user=user,
        password= password,
        port= 3306,
        db= 'devicemanagement')
    return connect

#创建表
def createTable(conn):
    cursor = conn.cursor()
    sql_createtable = """create table test(
        id char(20) primary key,
        name char(20) not null,
        age int,
        sex char(10)
    )"""
    cursor.execute(sql_createtable)  # 执行SQL语句
    conn.commit()  # 提交事务
    cursor.close() # 关闭cursor

#向表中插入记录
def insert(conn,id,name,age,sex):
    cursor = conn.cursor()
    sql_insert = "insert into test (id, name, age, sex) values ('%s','%s', %s, '%s')" % (id,name,age,sex)
    cursor.execute(sql_insert)
    conn.commit()
    cursor.close()

def deleteById(conn, id):
    cursor = conn.cursor()
    sql_delete = "delete from test where id= '%s'" % id
    cursor.execute(sql_delete)
    conn.commit()
    cursor.close() 

def sql_select(conn):
    cursor = conn.cursor()
    sql_select = "select * from test"
    cursor.execute(sql_select)
    result = cursor.fetchall()
    for row in result:
        id = row[0]
        name = row[1]
        age = row[2]
        sex = row[3]
        print("id = {}, name = {}, age = {}, sex = {}".format(id,name,age,sex))


if __name__ == '__main__':
    pass




