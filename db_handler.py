# coding:utf-8
import sqlite3


class DBHandle(object):
    def __init__(self):
        self.conn = sqlite3.connect('sys_status.db')
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
