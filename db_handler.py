# coding:utf-8
import sqlite3


class DBHandle(object):
    def __init__(self):
        self.conn = sqlite3.connect('sys_status.db')
        self.cursor = self.conn.cursor()

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
        self.cursor.execute(
            "INSERT INTO " + table_name + " " + str(tuple(data_dict.keys())) +
            " VALUES " + str(tuple(data_dict.values())))
        self.conn.commit()


if __name__ == '__main__':
    dbh = DBHandle()
    dbh.get_a_log('A_status', '2019-05-05 10:22:03.488346')
