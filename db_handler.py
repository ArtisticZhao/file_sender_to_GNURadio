# coding:utf-8
import sqlite3
import os


class DBHandle(object):
    def __init__(self):
        # 检查文件是否存在, 如果不存在数据库的话则创建
        if not (os.path.exists('data/sys_status.db')):
            print('[INFO] Creating DataBase!')
            conn = sqlite3.connect('data/sys_status.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE [A_status]
            ( [timestamp] DEC PRIMARY KEY DESC NOT NULL UNIQUE,
            [recv_time] BLOB, [配置状态] BLOB,
            [工作模式] BLOB, [通道状态标识1] BLOB,
            [通道状态标识2] BLOB, [发射增益高字节] BLOB,
            [发射增益低字节] BLOB, [+5V接收电流] BLOB,
            [+5V接收电压] BLOB, [+5V发射电流] BLOB,
            [+5V发射电压] BLOB, [+3.3V电流] BLOB,
            [+3.3V电压] BLOB, [接收频偏1] BLOB,
            [接收频偏2] BLOB, [数字信号强度指示1] BLOB,
            [数字信号强度指示2] BLOB, [模拟信号强度指示] BLOB,
            [PCB温度1] BLOB, [PCB温度2] BLOB,
            [CAN发送包计数] BLOB, [CAN接收包计数] BLOB,
            [CAN错误包计数] BLOB, [CAN执行错误计数] BLOB,
            [CAN最近一条指令] BLOB, [CAN指令执行情况] BLOB,
            [RF发送包计数] BLOB, [RF发送抛弃包计数] BLOB,
            [RF接收包计数] BLOB, [RF接收错误包计数] BLOB,
            [RF接收执行错误计数] BLOB, [RF接收纠错失败计数] BLOB,
            [RF最近一条指令] BLOB, [RF指令执行情况] BLOB,
            [FTP当前接收文件序号] BLOB, [FTP当前接收文件长度] BLOB,
            [FTP当前接收文件校验值] BLOB, [FTP接收数据块大小] BLOB,
            [FTP接收成功包数] BLOB, [FTP接收缺失包数] BLOB,
            [FTP连续传输包数] BLOB,
            [目标CAN节点地址] BLOB, [当前发送文件序号] BLOB,
            [当前发送文件长度] BLOB, [当前发送文件校验值] BLOB,
            [FTP发送数据块大小] BLOB, [FTP发送成功包数] BLOB,
            [FTP发送缺失包数] BLOB, [读取数据包计数] BLOB,
            [复位计数] BLOB,
            [复位标识] BLOB,
            [ARM运行时间] BLOB, [AVR运行时间] BLOB) WITHOUT ROWID''')
            c.execute('''CREATE TABLE [B_status]
            ( [timestamp] DEC PRIMARY KEY DESC,
            [recv_time] BLOB, [配置状态] BLOB,
            [工作模式] BLOB, [通道状态标识1] BLOB, [接收速率] BLOB,
            [+1V内核电压] BLOB,
            [+1.8V IO电压] BLOB,
            [+1.5V DDR3电压] BLOB, [接收频偏1] BLOB,
            [接收频偏2] BLOB, [数字信号强度指示1] BLOB,
            [数字信号强度指示2] BLOB, [PCB温度2] BLOB,
            [剩余存储空间] BLOB, [CPU占用率] BLOB,
            [CAN发送包计数] BLOB, [CAN接收包计数] BLOB,
            [CAN错误包计数] BLOB, [CAN执行错误计数] BLOB,
            [CAN最近一条指令] BLOB, [CAN指令执行情况] BLOB,
            [RF发送包计数] BLOB, [RF发送抛弃包计数] BLOB,
            [RF接收包计数] BLOB, [RF接收错误包计数] BLOB,
            [RF接收执行错误计数] BLOB,
            [RF最近一条指令] BLOB, [RF指令执行情况] BLOB,
            [FTP连续传输包数] BLOB,
            [FTP当前接收文件序号] BLOB, [FTP当前接收文件长度] BLOB,
            [FTP当前接收文件校验值] BLOB, [FTP接收数据块大小] BLOB,
            [FTP接收成功包数] BLOB, [FTP接收缺失包数] BLOB,
            [目标CAN节点地址] BLOB, [当前发送文件序号] BLOB,
            [当前发送文件长度] BLOB, [当前发送文件校验值] BLOB,
            [FTP发送数据块大小] BLOB, [FTP发送成功包数] BLOB,
            [FTP发送缺失包数] BLOB, [读取数据包计数] BLOB,
            [复位计数] BLOB,
            [复位标识] BLOB,
            [ARM运行时间] BLOB, [AVR运行时间] BLOB)''')
            conn.commit()
        self.conn = sqlite3.connect('data/sys_status.db')
        self.cursor = self.conn.cursor()
        self.A_log_in_memory = list()
        self.B_log_in_memory = list()

    def __del__(self):
        self.conn.close()

    def get_all(self, table_name):
        cursor = self.cursor.execute("SELECT recv_time FROM " + table_name)
        return cursor.fetchall()

    def get_a_log(self, table_name, recv_time):
        SQL = "SELECT * from " + table_name + \
              " WHERE recv_time=\"" + recv_time + "\""
        cursor = self.cursor.execute(SQL)
        d_status = dict()
        ans = None
        for each in cursor:
            ans = each
        if ans is not None:
            cursor = self.cursor.execute(
                'PRAGMA table_info([' + table_name + '])')
            for index, val in enumerate(cursor):
                d_status[val[1]] = ans[index]
        return d_status

    def insert_a_log(self, table_name, data_dict):
        if table_name == 'A_status':
            self.A_log_in_memory.append(data_dict)
        else:
            self.B_log_in_memory.append(data_dict)

    def commit_all(self):
        for each in self.A_log_in_memory:
            self.conn.execute("INSERT INTO " + 'A_status' + " " + str(
                tuple(each.keys())) + " VALUES " + str(tuple(each.values())))
        for each in self.B_log_in_memory:
            self.conn.execute("INSERT INTO " + 'B_status' + " " + str(
                tuple(each.keys())) + " VALUES " + str(tuple(each.values())))
        self.conn.commit()
        self.A_log_in_memory.clear()
        self.B_log_in_memory.clear()


if __name__ == '__main__':
    dbh = DBHandle()
    dbh.get_a_log('A_status', '2019-05-05 10:22:03.488346')
