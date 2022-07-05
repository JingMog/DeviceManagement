import pymysql


connect = pymysql.connect(
        host= '121.37.88.160',
        user= 'DeviceManagement',
        password= 'DiiCKMXkYtxDsMzk',
        port= 3306,
        db= 'devicemanagement'
    )

cursor = connect.cursor()

# 用户表
create_table_user = """create table user(
            user_account char(20) primary key,
            user_password char(20) not null,
            phone char(11),
            foreign key(user_account) references use_person(use_person_id)

            )"""

create_table_manager = """create table manager(
            manager_account char(20) primary key,
            manager_password char(20) not null,
            phone char(11),
            foreign key(manager_account) references manager_person(manager_person_id)
            )"""


# 供应商表
create_table_supplier = """create table supplier(
            supplier_id char(20) primary key,
            supplier_name char(20) not null,
            supplier_phone char(15),
            supplier_mail char(20)
            )"""

# 设备表
create_table_device = """create table device(
            device_id char(20) primary key,
            device_name char(20),
            device_importance_level int not null,
            device_price double,
            device_charge_person char(20) not null,
            device_state char(20),
            device_attribute char(20),
            device_supplier_id char(20),
            foreign key(device_supplier_id) references supplier(supplier_id),
            foreign key(device_charge_person) references manager_person(manager_person_id),
            )"""

# 维修人员表
create_table_repair_person = """create table repair_person(
            repair_person_id char(20) primary key,
            repair_person_name char(20) not null,
            repair_person_department char(20),
            repair_person_sex char(10),
            foreign key(repair_person_department) references department(department_id)
            )"""

# 维修记录表
create_table_repair = """create table repair(
            repair_id char(20),
            device_id char(20), 
            repair_person_id char(20),
            repair_date date,
            repair_result char(20),
            primary key(repair_id),
            foreign key(device_id) references device(device_id),
            foreign key(repair_person_id) references repair_person(repair_person_id)
            )"""

# 使用表
create_table_use_record = """create table use_record(
            use_id char(20),
            device_id char(20),
            use_person_id char(20),
            use_date date,
            estimate_time int,
            return_date date,
            return_state char(20),
            overtime char(10),
            approver_id char(20),
            primary key(use_id,device_id,use_person_id),
            foreign key(device_id) references device(device_id),
            foreign key(use_person_id) references use_person(use_person_id),
            foreign key(approver_id) references manager_person(manager_person_id)
            )"""

# 使用人员表
create_table_use_person = """create table use_person(
            use_person_id char(20) primary key,
            use_person_name char(20),
            use_person_department char(20),
            use_person_power int,
            use_person_integrity int,
            foreign key(use_person_department) references department(department_id)
            )"""

# 部门表
create_table_department = """create table department(
            department_id char(20) primary key,
            department_name char(20) not null,
            department_charge_person char(20),
            department_charge_phone char(15),
            department_location char(20)
            )"""

create_table_supply = """create table supply(
            supplier_id char(20),
            device_id char(20),
            primary key(supplier_id,device_id),
            foreign key(supplier_id) references supplier(supplier_id),
            foreign key(device_id) references device(device_id),
            )"""

drop = "drop table device"

add_foreign_key = "alter table use_record add constraint use_record_ibfk_3 foreign key(approver) references manager_person(manager_person_name)"

create_table_manager_person = """
            create table manager_person(
            manager_person_id char(20) primary key,
            manager_person_name char(20) not null,
            manager_person_department char(20),
            foreign key(manager_person_department) references department(department_id)
            )"""

add_column = """
            alter table device add constraint fk_st_score2 
            foreign key(device_charge_person) references manager_person(manager_person_id)
            """

create_view_common_user_device = """
            create view device_common_user as select device_id,device_name,device_type,device_state,device_attribute,device_importance_level from device
            """

create_view_manager_device = """
            create view device_manager as 
            select device_id,device_name,device_type,device_state,device_attribute,device_importance_level
            from device
            """

create_view_common_user_use = """create view common_user_use as 
            select use_id,device.device_name,device.device_id,use_date,estimate_time 
            from use_record,device
            where return_state is null and return_date is null and device.device_id = use_record.device_id"""

create_view_common_user_repair = """create view common_user_repair as 
            select repair_id,device.device_name,repair.device_id,repair.repair_date,repair.repair_result,repair_person.repair_person_name 
            from device,repair,repair_person
            where device.device_id = repair.device_id and repair.repair_person_id = repair_person.repair_person_id
"""

create_view_manager_device = """create view manager_device as 
        select device_id,device_name,device_type,device_importance_level,device_price,manager_person.manager_person_name,device_state,device_attribute,supplier.supplier_name 
        from device,supplier,manager_person 
        where device.device_charge_person = manager_person.manager_person_id and device.device_supplier_id = supplier.supplier_id
"""

create_view_supply = """create view supply as 
        select supplier.supplier_name,device.device_name,device.device_type,device.device_price 
        from device,supplier
        where device.device_supplier_id = supplier.supplier_id"""

        
# cursor.execute(create_table_device)
cursor.execute(create_view_supply)

connect.commit()
cursor.close()

