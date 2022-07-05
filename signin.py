# 登录
# 注册
from sqlalchemy import false, true
import conn
connect = conn.connect()


def signin_common_user(account,password):
    # 查询账号对应的密码
    sql = "select user_password from user where user_account = '%s' " % account
    cursor = connect.cursor() # 创建游标对象cursor
    try:
        # 执行sql语句
        cursor.execute(sql)
        result = cursor.fetchone()
        if password == result[0]:
            print("登录成功！")
            return True
        else:
            print("密码错误,请重新输入")
            return False
    except:
        # 查询失败，不存在该账号
        print("账号不存在,请检查后重试")
        return False
    finally:
        cursor.close()

def signin_manager(account,password):
    # 查询账号对应的密码
    sql = "select manager_password from manager where manager_account = '%s' " % account
    cursor = connect.cursor() # 创建游标对象cursor
    try:
        # 执行sql语句
        cursor.execute(sql)
        result = cursor.fetchone()
        if password == result[0]:
            print("登录成功！")
            return True
        else:
            print("密码错误,请重新输入")
            return False
    except:
        # 查询失败，不存在该账号
        print("账号不存在,请检查后重试")
        return False
    finally:
        cursor.close()

def register(account, password, phone):
    cursor = connect.cursor() # 创建游标对象
    sql = "insert into user values('%s', '%s', '%s')" % (account, password, phone)
    try:
        cursor.execute(sql)
        connect.commit()
        print("创建成功,请重新登录")
        return True
    except:
        print("创建失败,请检查账号是否正确")
        return False
    finally:
        cursor.close()







if __name__ == '__main__':
    
    # ok = signin("useperson001","123456")
    # ok = register("useperson005", "123456", "684a3d")
    # signin_manager("managser001", "12ad456")
    pass
    

