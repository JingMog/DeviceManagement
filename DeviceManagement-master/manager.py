import conn
import datetime
import numpy as np

### 普通管理员,处理设备相关请求,身份为manager_person
# - 处理借用设备申请
# - 处理维修申请
# - 查看设备的所有情况
# - 统计信息(本月借用次数,本月维修次数)
# - 查询操作 (所有设备信息,借用记录)
# - 统计数据，本月借用次数,违规情况统计

class manager:
    connect = conn.connect()
    account = ''
    password = ''
    phone = ''
    name = ''

    def __init__(self, account):
        self.account = account
        self.__get_managerinfo()


    # 获取管理员个人信息
    # 返回工号，姓名，电话，所属部门
    def get_person_info(self):
        # 获取管理员信息
        list = []
        list.append(self.account)
        list.append(self.name)
        list.append(self.phone)
        # 查询管理员部门
        sql = "select department_name from department,manager_person where manager_person.manager_person_department = department.department_id and manager_person.manager_person_id = '%s'" % self.account
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        list.append(result[0][0])
        return list
    


    # 获取所有个人信息
    def __get_managerinfo(self):
        sql = "select * from manager where manager_account = '%s'" % self.account
        sql_name = "select manager_person_name from manager_person where manager_person_id = '%s'" % self.account
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()

        cursor = self.connect.cursor()
        cursor.execute(sql_name)
        result_name = cursor.fetchone()
        cursor.close()


        self.name = result_name[0]
        self.password = result[1]
        self.phone = result[2]
        # print(self.name)
    
    # 查询该管理员处理的所有记录
    # 返回使用id,设备id，设备名，借用人，借用日期，预估使用日期，返回日期，是否超时
    def sql_all_del_record(self):
        sql = "select use_id,device.device_id,device.device_name,use_person.use_person_name,use_date,estimate_time,return_date,overtime from use_record,device,use_person where approver_id = '%s' and use_record.device_id = device.device_id and use_record.use_person_id = use_person.use_person_id" % self.account
        cursor = self.connect.cursor()
        cursor.execute(sql)
        all_del_record = cursor.fetchall()
        cursor.close()
        return all_del_record

    # 查询所有已完成的借用记录
    def sql_use_record(self):
        sql_use = "select use_record.use_id,device.device_name,use_person.use_person_name,use_date,estimate_time,return_date,return_state,overtime,manager_person_name from use_record,device,manager_person,use_person where return_date is not null and approver_id is not null and use_record.device_id = device.device_id and use_record.use_person_id = use_person.use_person_id and use_record.approver_id = manager_person.manager_person_id"
        cursor = self.connect.cursor()
        cursor.execute(sql_use)
        use_record = cursor.fetchall()
        # print(use_record)
        cursor.close()
        return use_record
    
    # 查询所有未归还的记录
    def sql_unreturn_record(self):
        sql_unreturn = "select use_id,device.device_name,device.device_id,use_person.use_person_id,use_person.use_person_name,use_date,estimate_time,manager_person_name from use_record,use_person,device,manager_person where return_date is null and approver_id is not null and use_record.device_id = device.device_id and use_record.use_person_id = use_person.use_person_id and use_record.approver_id = manager_person.manager_person_id"
        cursor = self.connect.cursor()
        cursor.execute(sql_unreturn)
        unreturn_record = cursor.fetchall()
        cursor.close()
        return unreturn_record
    

    # 查询所有未批准的借用记录
    def sql_unapprove_record(self):
        sql_unapprove = "select use_id,device.device_name,device.device_id,use_person.use_person_id,use_person.use_person_name,use_date,estimate_time from use_record,device,use_person where return_date is null and approver_id is null and device.device_id = use_record.device_id and use_record.use_person_id = use_person.use_person_id"
        cursor = self.connect.cursor()
        cursor.execute(sql_unapprove)
        unapprove_record = cursor.fetchall()
        cursor.close()
        return unapprove_record
    

    # 查询所有已完成的维修记录
    def sql_repair_record(self):
        sql_repair = """
                    select repair.repair_id,device.device_name,device.device_id,repair_person.repair_person_name,repair.repair_date,repair.repair_result,use_person.use_person_id,use_person.use_person_name
                    from repair,device,use_person,repair_person
                    where repair_date is not null and repair_result is not null and repair.device_id = device.device_id and repair.repair_person_id = repair_person.repair_person_id and repair.apply_person_id = use_person.use_person_id
                    """
        cursor = self.connect.cursor()
        cursor.execute(sql_repair)
        repair_record = cursor.fetchall()
        # print(repair_record)
        cursor.close()
        return repair_record
    

    # 查询所有未完成的维修记录
    def sql_unrepair_record(self):
        sql_unapprove = """select repair_id,repair.device_id,device.device_type,use_person.use_person_name,use_person.use_person_id from repair,use_person,device where repair_person_id is null and repair.device_id = device.device_id and repair.apply_person_id = use_person.use_person_id"""
        cursor = self.connect.cursor()
        cursor.execute(sql_unapprove)
        unapprove_repair = cursor.fetchall()
        cursor.close()
        return unapprove_repair

    #0,1,2,3,4,5,6,8
    # 查询所有设备信息
    def sql_device(self):
        sql_device = """select device_id,device_name,device_type,device_importance_level,device_price,manager_person.manager_person_name,device_state,device_attribute,supplier.supplier_name
        from device,supplier,manager_person
        where device.device_charge_person = manager_person.manager_person_id and device.device_supplier_id = supplier.supplier_id and device.device_charge_person = '%s'
        """ % self.account
        cursor = self.connect.cursor()
        cursor.execute(sql_device)
        device_info = cursor.fetchall()
        cursor.close()
        return device_info

    # 处理借用编号为use_id的申请
    # 设置其申请人为当前登录的管理员
    def deal_use_apply(self, use_id):
        unapprove_record = self.sql_unapprove_record()
        unapprove_use_id = []
        for row in unapprove_record:
            unapprove_use_id.append(row[0])
        if use_id not in unapprove_use_id:
            print("处理失败,该设备不存在借用情况或已被批准")
            return False
        sql_use_apply = "update use_record set approver_id = '%s' where use_id = '%s'" % (self.account, use_id)
        cursor = self.connect.cursor()
        cursor.execute(sql_use_apply)
        self.connect.commit()
        print("处理成功")
        cursor.close()
        return True

    # 处理维修编号为repair_id的维修申请
    # 随机为其分配一个维修人员，设置维修日期为当前日期，设置维修结果为成功
    # 同时将对应设备的状态设置为良好
    def deal_repair_apply(self, repair_id):
        sql_repair_person = "select repair_person_id from repair where repair_person_id is not null"
        cursor = self.connect.cursor()
        cursor.execute(sql_repair_person)
        all_repair_person = cursor.fetchall()
        cursor.close()
        repair_person_id_list = []
        for row in all_repair_person:
            repair_person_id_list.append(row[0])
        num = np.random.randint(0,len(repair_person_id_list))
        repair_person_id = repair_person_id_list[num]
        # 检查是否存在该维修记录
        unrepair_record = self.sql_unrepair_record()  # 未完成的维修申请
        unrepair_record_id = []
        for row in unrepair_record:
            unrepair_record_id.append(row[0])
        if repair_id not in unrepair_record_id:
            print("处理失败,该设备不存在维修情况或已被维修")
            return False
        # 处理该维修记录
        repair_date = datetime.datetime.now().strftime('%Y-%m-%d')
        # 设置维修记录repair_id的维修人为repair_person_id,维修日期为repair_date
        sql_repair_apply = "update repair set repair_person_id = '%s', repair_date = '%s', repair_result = '%s' where repair_id = '%s'" % (repair_person_id, repair_date, "成功", repair_id)
        cursor = self.connect.cursor()
        cursor.execute(sql_repair_apply)
        self.connect.commit()
        print("处理成功")
        cursor.close()

        # 获取对应repair_id的device_id
        device_id = ""
        for row in unrepair_record:
            if row[0] == repair_id:
                device_id = row[1]
        print(device_id)
        # 设置device表中对应设备状态为良好
        sql_device_status = "update device set device_state = '良好' where device_id = '%s'" % device_id
        cursor = self.connect.cursor()
        cursor.execute(sql_device_status)
        self.connect.commit()
        cursor.close()

    # 统计各种设备的借阅情况
    def device_use_statistics(self):
        # 使用多表查询和聚集函数
        sql = "select device.device_type,count(use_record.device_id) from use_record,device where device.device_id = use_record.device_id group by device.device_type"

        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
    

    # 统计各种设备的维修情况
    # 使用多表查询和聚集函数
    def device_repair_statistics(self):
        sql = "select device.device_type,count(repair.device_id) from repair,device where device.device_id = repair.device_id group by device.device_type"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    # 统计维修人员维修情况
    def repair_person_statistics(self):
        sql = "select repair_person.repair_person_name,count(repair.repair_person_id) from repair,repair_person where repair.repair_person_id = repair_person.repair_person_id group by repair.repair_person_id"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result


    # 查询所有违规情况
    # 返回借用记录，设备名id,设备名，借用人，借用时间，预计使用时间，归还时间，归还状态，是否超时，批准人
    def sql_all_violate(self):
        sql = "select use_id,use_record.device_id,device.device_name,use_person.use_person_name,use_date,estimate_time,return_date,return_state,overtime,manager_person.manager_person_name from use_record,device,use_person,manager_person where use_record.device_id = device.device_id and use_record.use_person_id = use_person.use_person_id and use_record.approver_id = manager_person.manager_person_id and overtime = '是'"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

if __name__ == "__main__":

    m1 = manager('manager001')
    result = m1.sql_unrepair_record()
    # result = m1.sql_device()

    print(result)

    # m1.get_managerinfo()
    # print("所有已完成的申请记录")
    # use_info =  m1.sql_use_record()
    # for row in use_info:
    #     print(row)

    # print("未处理的申请记录")
    # unapprove_info = m1.sql_unapprove_record()
    # for row in unapprove_info:
    #     print(row)
    # ok = m1.deal_use_apply("use784335")

    # print("所有未归还的记录")
    # unreturn_info = m1.sql_unreturn_record()
    # for row in unreturn_info:
    #     print(row)
    # device_info = m1.sql_device()
    # for row in device_info:
    #     print(row)

    # print("所有已完成的维修记录")
    # repair_info = m1.sql_repair_record()
    # for row in repair_info:
    #     print(row)

    # print("所有未完成的维修记录")
    # repair_info = m1.sql_unrepair_record()
    # for row in repair_info:
    #     print(row)
    # ok = m1.deal_repair_apply("repair8001")

    # unapprove_info = m1.sql_unapprove_repair()
    # for row in unapprove_info:
    #     print(row)

    # np.random.randint(1,3)
