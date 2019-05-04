# coding:utf-8
import sqlite3


class DBHandle(object):
    def __init__(self):
        self.conn = sqlite3.connect('sys_status.db')
        self.cursor = self.conn.cursor()

    def get_all(self, table_name):
        cursor = self.cursor.execute("PRAGMA table_info(B_status)")
        print(cursor.fetchall())

    def insert_a_log(self, table_name, data_dict):
        pass


if __name__ == '__main__':
    dbh = DBHandle()
    dbh.get_all('aa')
