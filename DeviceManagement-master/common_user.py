import conn
import numpy as np
import time
import datetime

#普通用户：
# 1.查看自己的借阅情况
# 2.查看目前可借出的设备
# 3.申请借用
# 4.申请维修，查看维修结果
# 5.查看待归还设备
# 6.统计信息


class common_user:
    
    user_id = ''            # 用户id
    user_name = 'name'          # 用户名
    user_department = ''    # 用户部门
    user_power = ''         # 用户权力
    user_integrity = 100    # 用户诚信值

    _connect = conn.connect()

    use_device_id = ''
    use_device_name = ''
    use_date = ''

    repair_id = ''          # 维修id
    repair_device_id = ''
    repair_device_name = ''
# 从数据库中获取用户的个人信息
    def get_person_information(self):
        list = []
        list.append(self.user_name)
        list.append(self.user_id)
        list.append(self.user_department)
        list.append(self.user_power)
        list.append(self.user_integrity)
        return list


    def getperson_info(self):
        sql = "select * from use_person where use_person_id = '%s'"% self.user_id
        cursor = self._connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) != 0:
            self.user_name = result[0][1]
            self.user_department = result[0][2]
            self.user_power = result[0][3]
            self.user_integrity = result[0][4]

    # 构造函数
    def __init__(self,user_id):
        self.user_id = user_id
        self.getperson_info()

    def __sql_device_name(self,deivce_id):
        sql = "select device_name from device where device_id = '%s'" % deivce_id
        cursor = self._connect.cursor()
        cursor.execute(sql)
        device_name = cursor.fetchall()
        cursor.close()
        return device_name[0][0]

    # 借用操作
    def __use(self, device_id, estimate_time):
        # 首先生成use_id
        cursor = self._connect.cursor()
        sql_useid = "select use_id from use_record"
        cursor.execute(sql_useid)
        useid = cursor.fetchall()
        # 生成随机序号
        list_id = []
        for row in useid:
            list_id.append(row[0])  # 获取所有的id号
        while 1:   # 生成一个不在
            idnum = np.random.randint(0,999999)
            id = "use" + str(idnum)
            if id in list_id:   # 如果id 在list_id中就重新生成序号，否则跳出循环，此时id为唯一的
                continue
            else:
                break
        # print(id)
        nowtime = time.localtime()
        _use_date = str(nowtime.tm_year) + '-' + str(nowtime.tm_mon) + '-' + str(nowtime.tm_mday)
        self.use_date = _use_date
        self.use_device_id = device_id
        self.use_device_name = self.__sql_device_name(device_id)
        sql_apply = "insert into use_record (use_id,device_id,use_person_id,use_date,estimate_time) values('%s','%s','%s','%s', %s)" % (id, device_id, self.user_id, _use_date,estimate_time)
        # print(sql_apply)
        cursor.execute(sql_apply)   
        self._connect.commit()
        cursor.close()
        # 修改device表中设备状态
        sql_device = "update device set device_attribute = '%s' where device_id = '%s'" % ('占用', device_id)
        cursor = self._connect.cursor()
        cursor.execute(sql_device)
        self._connect.commit()
        cursor.close()



    # 查看自己的借阅情况
    def sql_use_record(self):
        # 执行查询语句
        sql = "select use_id,use_record.device_id,device.device_name,use_date,estimate_time,return_date,return_state,overtime,manager_person.manager_person_name from use_record,device,manager_person where use_person_id = '%s' and device.device_id = use_record.device_id and manager_person.manager_person_id = use_record.approver_id" % self.user_id
        cursor = self._connect.cursor()
        cursor.execute(sql)
        record1 = cursor.fetchall()  #获取查询得到的所有结果，为一个元组
        cursor.close()

        sql = "select use_id,use_record.device_id,device.device_name,use_date,estimate_time,return_date,return_state,overtime,approver_id from use_record,device where use_person_id = '%s' and device.device_id = use_record.device_id and approver_id is null" % self.user_id
        cursor = self._connect.cursor()
        cursor.execute(sql)
        record2 = cursor.fetchall()
        cursor.close()
        record = record1 + record2

        return record


    # 查看所有目前可借出的设备
    def sql_all_useabledevice(self):
        # print("查询目前所有可以借出的设备")
        sql = "select device_id,device_name,device_type,device_state,device_attribute from device where device_importance_level<='%s' " % self.user_power
        cursor = self._connect.cursor()
        cursor.execute(sql)
        useabledevice = cursor.fetchall()
        cursor.close()
        return useabledevice
    

    
    # 申请借用
    def apply_use(self, device_id, estimate_time):
        # print("申请借用",device_id)
        # 获取所有可以借用的设备
        useable_device = self.sql_all_useabledevice()
        # 检查设备状况是否良好以及是否空闲
        for row in useable_device:
            if device_id == row[0]:
                if row[3] == "良好" and row[4] == "空闲":
                    # 借用操作
                    # 发出请求,向use_record中添加一条记录
                    self.__use(device_id=device_id, estimate_time=estimate_time) # 申请借用
                    print("借用",row[1])
                    return True
                else:
                    print("借用失败,当前设备状态不可借用")
                    return False

    # 获取所有未归还设备
    def get_unreturn_device(self):
        cursor = self._connect.cursor()
        # 获取该用户所有未归还的设备编号,借用时间,预估使用时间
        sql = "select use_id,device.device_name,device.device_id,use_date,estimate_time from use_record,device where return_state is null and return_date is null and use_person_id = '%s' and device.device_id = use_record.device_id" % self.user_id
        cursor.execute(sql)
        unreturn_device = cursor.fetchall()
        list = []
        for i in unreturn_device:
            list.append([i[0],i[1],i[2],i[3],i[4]])
        # print(list)
        cursor.close()
        for i in range(len(list)):
            date_estimate = list[i][3] + datetime.timedelta(days=list[i][4])
            list[i][4] = date_estimate
        # print(list)
        return list



    # 归还设备
    # 先判断该设备是否被自己借用,然后判断是否超时,之后更新use_record表中的相关信息
    def return_device(self, use_id, return_state):
        # 获取所有未归还设备
        sql = "select use_id,use_date,device_id from use_record where return_date is null and use_person_id = '%s'" % self.user_id
        cursor = self._connect.cursor()
        cursor.execute(sql)
        unreturn_device = cursor.fetchall()
        cursor.close()
        list = []
        for i in unreturn_device:
            list.append(i[0])
        print(list)
        if use_id not in list:
            print("归还失败,该设备未借用")
            return False
        for row in unreturn_device:
            if use_id == row[0]:
                # 找到该设备，就执行归还操作
                # 判断是否超时
                use_date = row[1]  # 借用日期
                # 获取estimate_time
                sql = "select estimate_time from use_record where use_id = '%s'" % use_id
                cursor = self._connect.cursor()
                cursor.execute(sql)
                estimate_time = cursor.fetchone()[0]
                cursor.close()
                # estimate_time = row[2] # 预计使用时间
                nowtime = time.localtime()
                return_date = datetime.date(nowtime.tm_year,nowtime.tm_mon,nowtime.tm_mday)       # 归还日期
                duringtime = (return_date - use_date).days # 实际使用时间

                # 判断是否超时
                if duringtime > estimate_time:
                    overtime = "是"
                else:
                    overtime = "否"
                # 执行归还操作
                sql_return = "update use_record set return_date = '%s', return_state = '%s', overtime='%s' where use_id = '%s'" % (return_date, return_state, overtime,use_id)
                cursor = self._connect.cursor()
                cursor.execute(sql_return)
                self._connect.commit()
                cursor.close()


                sql = "select device_id from use_record where use_id = '%s'" % use_id
                cursor = self._connect.cursor()
                cursor.execute(sql)
                device_id = cursor.fetchone()[0]
                cursor.close()
                print(device_id)
                sql = "update device set device_attribute = '%s' where device_id = '%s'" % ("空闲",device_id)
                cursor = self._connect.cursor()
                cursor.execute(sql)
                self._connect.commit()
                cursor.close()
                
         
                
    # 申请维护设备
    # 先判断该设备是否可以维修,然后生成一条repair_id并插入repair表中
    def apply_repair(self, device_id):
        self.repair_device_id = device_id
        repair_device = "select device_id,device_name,device_state,device_attribute from device where device_importance_level<='%s' and device_state = '故障'" % self.user_power
        cursor = self._connect.cursor()
        cursor.execute(repair_device)
        _repair_device = cursor.fetchall()
        repair_device = []
        for row in _repair_device:
            repair_device.append(row[0])
        print(repair_device)
        if device_id not in repair_device:
            print("申请维护失败,该设备无需维护")
            return False
        
        # 申请维护
        # 生成随机序号，并将序列号和device_id存入repair表中
        list_id = []
        sql_repair = "select repair_id from repair"
        cursor.execute(sql_repair)
        repair_id = cursor.fetchall()
        for row in repair_id:
            list_id.append(row[0])
        # print(list_id)
        while True:
            repairnum = np.random.randint(1, 10000)
            repair_id = 'repair' + str(repairnum)
            if repair_id in list_id:
                continue
            else:
                print("repair_id",repair_id) 
                break
        self.repair_id = repair_id
        sql_apply = "insert into repair (repair_id,device_id,apply_person_id) values('%s','%s','%s')" % (repair_id, device_id,self.user_id)
        cursor.execute(sql_apply)
        self._connect.commit()
        cursor.close()
        print("维修申请成功")


    # 查询个人所有维修申请记录
    def sql_all_repair_apply(self):
        sql = "select repair_id,device.device_name,repair.device_id,repair.repair_date,repair.repair_result,repair_person.repair_person_name from device,repair,repair_person where device.device_id = repair.device_id and repair.repair_person_id = repair_person.repair_person_id and repair.apply_person_id = '%s'" % self.user_id

        cursor = self._connect.cursor()
        cursor.execute(sql)
        all_repair_apply = cursor.fetchall()

        sql = "select repair_id,device.device_name,repair.device_id,repair.repair_date,repair.repair_result,repair_person_id from device,repair where device.device_id = repair.device_id and repair.apply_person_id = '%s' and repair_date is null" % self.user_id
        cursor = self._connect.cursor()
        cursor.execute(sql)
        all_unrepair_apply = cursor.fetchall()
        all_repair_apply = all_repair_apply + all_unrepair_apply
        return all_repair_apply
    
    # 查询已维修的申请记录
    def sql_all_repair_record(self):
        sql = "select repair_id,device.device_name,repair.device_id,repair.repair_date,repair.repair_result,repair_person.repair_person_name from device,repair,repair_person where device.device_id = repair.device_id and repair.repair_person_id = repair_person.repair_person_id and repair.apply_person_id = '%s' and repair.repair_person_id is not null and repair.repair_date is not null and repair.repair_result is not null" % self.user_id
        cursor = self._connect.cursor()
        cursor.execute(sql)
        all_repair_apply = cursor.fetchall()
        return all_repair_apply

    # 申请使用的结果
    # def get_apply_use_result(self):
    #     list = []
    #     list.append(self.user_name)
    #     list.append(self.user_id)
    #     list.append(self.use_device_name)
    #     list.append(self.use_device_id)
    #     list.append(self.use_date)
    #     return list
    def get_apply_use_result(self):
        list = []
        list.append(self.user_name)
        list.append(self.user_id)
        list.append(self.use_device_name)
        list.append(self.use_device_id)
        # 字符串转化为时间
        list.append(self.use_date)
        return list

    # 申请维修的结果
    def get_apply_repair_result(self):
        list = []
        list.append(self.user_name)
        list.append(self.user_id)
        list.append(self.repair_id)
        list.append(self.repair_device_id)
        sql = "select device_name from device where device_id = '%s'" % self.repair_device_id
        cursor = self._connect.cursor()
        cursor.execute(sql)
        self.repair_device_name = cursor.fetchall()[0][0]
        list.append(self.repair_device_name)
        return list

# if __name__ == '__main__':
#     u1 = common_user("useperson001")
#     result = u1.get_unreturn_device()
#     for row in result:
#         print(row)
#     u1.return_device("use68745","良好")
#     print("==================")
#     result = u1.get_unreturn_device()
#     for row in result:
#         print(row)



    # result = u1.sql_all_repair_apply()
    # # print(result)
    # for row in result:
    #     print(row)
    # print('========')
    # result = u1.sql_all_repair_record()
    # print(result)
    # for row in result:
    #     print(row)
    # u1.apply_use("device6546",10)
    # print(u1.get_apply_use_result())
    # u1.apply_repair("device001")
    # result = u1.sql_use_record()
    # for row in result:
    #     print(row)
    # # print(u1.user_power)
    # useable_device = u1.sql_all_useabledevice()
    # for row in useable_device:
    #     print(row)
    # u1.apply_use("device001",10)



