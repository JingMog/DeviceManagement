# ### ROOT用户
# - 管理员维护情况,每个管理员批准的请求数,负责的设备数,负责的设备名称
# - 设备供应情况,每个厂家供应的设备名称,供应的设备种类数
# - 购买新设备
# - 设备信息的修改
# - 查看公司各部门情况


from unittest import result
import conn
import numpy as np

class root:
    connect = conn.connect()
    account = 'root'
    password = 'root'

    # 统计管理员批准用户请求情况
    # 每个管理员批准了多少申请
    def manager_statistics(self):
        sql = """select manager_person.manager_person_id,manager_person.manager_person_name,count(use_record.approver_id) 
        from use_record,manager_person 
        where use_record.approver_id is not null and use_record.approver_id = manager_person.manager_person_id group by use_record.approver_id"""
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    # 获取管理员负责的各种设备名称
    # 每个管理员负责的设备名称
    def manager_respon_device(self):
        sql = "select manager_person.manager_person_name,manager_person.manager_person_id,device.device_id,device.device_name,device.device_type from device,manager_person where device.device_charge_person = manager_person.manager_person_id"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    # 统计管理员负责的设备数量
    # 每个管理员负责的设备数量
    def manager_person_device_statistics(self):
        sql = "select manager_person.manager_person_name,manager_person.manager_person_id,count(device.device_charge_person) from device,manager_person where device.device_charge_person = manager_person.manager_person_id group by device.device_charge_person"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    # 统计设备供应商的供应数量
    # 每个供应商供应的设备数量
    def supplier_statistics(self):
        sql = "select supplier.supplier_id,supplier.supplier_name,count(device.device_supplier_id) from device,supplier where device.device_supplier_id = supplier.supplier_id group by device.device_supplier_id"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    # 查询供应商供应设备信息
    def sql_supplier_info2(self):
        sql = "select supplier.supplier_name,device.device_name,device.device_type,device.device_price from device,supplier where device.device_supplier_id = supplier.supplier_id"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def sql_supplier_info(self):
        sql = "select supplier.supplier_id,supplier.supplier_name,device.device_name,device.device_type,device.device_price from device,supplier where device.device_supplier_id = supplier.supplier_id"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    # 查看所有设备的所有情况
    def sql_device_info(self):
        sql  = """select device_id,device_name,device_type,device_importance_level,device_price,manager_person.manager_person_name,device_state,device_attribute,supplier.supplier_name
        from device,supplier,manager_person
        where device.device_charge_person = manager_person.manager_person_id and device.device_supplier_id = supplier.supplier_id
        """
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    # # 统计设备使用次数
    # def device_use_statistics(self):
    #     # 使用多表查询和聚集函数
    #     sql = "select device.device_name,count(use_record.device_id) from use_record,device where device.device_id = use_record.device_id group by use_record.device_id"
    #     cursor = self.connect.cursor()
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     cursor.close()
    #     return result


    # 增加新设备
    def add_device(self, device_type, device_importance_level, device_price, device_charge_person, supplier_name):
        device_name = device_type + str(np.random.randint(0,9999))

        # 生成设备序号
        # 检查是否存在该设备类型
        sql = "select distinct device_type from device"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        device_list = []
        for i in result:
            device_list.append(i[0])
        if device_type not in device_list:
            print("不存在该设备类型")
            return False

        sql = "select max(device_id) from device"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        sql_result = cursor.fetchall()
        max_device_id = sql_result[0][0]
        num = int(max_device_id[6:])
        num += 1
        device_id = 'device' + str(num)

        # 获取管理员名对应的管理员id
        # 检查对应管理员是否存在
        sql = "select manager_person_name from manager_person"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        sql_result = cursor.fetchall()
        manager_person_name_list = []
        for i in sql_result:
            manager_person_name_list.append(i[0])
        if device_charge_person not in manager_person_name_list:
            print("管理员不存在")
            return False
        
        sql = "select manager_person_id from manager_person where manager_person_name = '%s'" % device_charge_person
        cursor.execute(sql)
        sql_result = cursor.fetchall()
        manager_person_id = sql_result[0][0]

        # 获取供应商对应的id
        # 检查供应商是否存在
        sql = "select supplier_name from supplier"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        sql_result = cursor.fetchall()
        cursor.close()
        supplier_name_list = []
        for i in sql_result:
            supplier_name_list.append(i[0])
        if supplier_name not in supplier_name_list:
            print("供应商不存在")
            return False

        sql = "select supplier_id from supplier where supplier_name = '%s'" % supplier_name
        cursor = self.connect.cursor()
        cursor.execute(sql)
        sql_result = cursor.fetchall()
        supplier_id = sql_result[0][0]
        print(supplier_id)

        # 插入数据
        sql = "insert into device(device_id,device_name,device_type,device_importance_level,device_price,device_charge_person,device_state,device_attribute,device_supplier_id) values('%s','%s','%s', '%s', '%s', '%s', '良好', '空闲', '%s')" % (device_id, device_name,device_type, device_importance_level, device_price, manager_person_id, supplier_id)
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()
        
    
    # 统计使用人员部门分布情况
    def department_stastics(self):
        
        sql = "select department.department_name, count(use_person_department) from department,use_person where use_person.use_person_department = department.department_id group by use_person.use_person_department"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        use_result = cursor.fetchall()
        cursor.close()

        # 统计维修人员部门分布情况
        sql = "select department.department_name, count(repair_person_department) from department,repair_person where repair_person.repair_person_department = department.department_id group by repair_person.repair_person_department"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        repair_result = cursor.fetchall()
        cursor.close()

        # 统计管理人员部门分布情况
        sql = "select department.department_name, count(manager_person_department) from department,manager_person where manager_person.manager_person_department = department.department_id group by manager_person.manager_person_department"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        manager_result = cursor.fetchall()
        cursor.close()
        
        use_result_list = []
        for i in use_result:
            use_result_list.append([i[0],i[1]])
        for i in range(len(use_result_list)):
            for row in repair_result:
                if use_result_list[i][0] == row[0]:
                    use_result_list[i][1] = use_result_list[i][1] + row[1]
        
        for i in range(len(use_result_list)):
            for row in manager_result:
                if use_result_list[i][0] == row[0]:
                    use_result_list[i][1] = use_result_list[i][1] + row[1]
        return use_result_list

# 展示所有供应商信息
    # 包括编号，名称，电话，邮箱
    def sql_all_supplier_info(self):
        sql = "select * from supplier"
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result


if __name__ == '__main__':
    r1 = root()
    # result = r1.device_info()
    # for row in result:
    #     print(row)

    # device_info = root.device_info()
    # for row in device_info:
    #     print(row)

    # device_use_statistic = root.device_use_statistics()
    # for row in device_use_statistic:
    #     print(row)

    # manager_person_device_statistics = root.manager_person_device_statistics()
    # for row in manager_person_device_statistics:
    #     print(row)


    # supplier_statistics = root.supplier_statistics()
    # for row in supplier_statistics:
    #     print(row)

    # manager_respon_device = root.manager_respon_device()
    # for row in manager_respon_device:
    #     print(row)

    # supplier_info = root.supplier_info()
    # for row in supplier_info:
    #     print(row)

    r1.add_device("螺丝刀",2,20,"刘启龙","华为")
    # result = root.department_stastics()
    # for i in result:
    #     print(i)