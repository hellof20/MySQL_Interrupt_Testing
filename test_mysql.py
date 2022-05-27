# -*- coding:utf-8 -*-
import time
import random
import pymysql
import string
import datetime
import os

all_chs = string.digits + string.ascii_letters


def get_random_str(str_length):
    random_str_list = [random.choice(all_chs) for k in range(str_length)]
    return ''.join(random_str_list)


class RunSqlToMysql(object):
    def __init__(self):
        self.mysql_host = os.environ.get('host')
        self.mysql_user = os.environ.get('user')
        self.mysql_password = os.environ.get('password')
        self.mysql_db_name = 'testdb'

    def connect_db(self):
        con_engine = pymysql.connect(
            host=self.mysql_host,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_db_name,
            port=3306,
            charset='utf8mb4',
            connect_timeout=1,
            read_timeout=1,
            write_timeout=1
        )
        return con_engine

    @staticmethod
    def run_sql(db_connect, sql):
        cursor = db_connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        db_connect.commit()
        return result
            
    @staticmethod
    def get_sql(table_name,server_id):
        field_str = 'timestamp, msg, other'
        values_str = "'%s', '%s', '%s'" % (datetime.datetime.now(), get_random_str(64), server_id)
        sql_sentence = "insert into %s(%s) values (%s);" % (table_name, field_str, values_str)
        return sql_sentence

    def do(self):
        while True:
            print('----------------------------')
            print(datetime.datetime.now())
            try:
                time.sleep(0.5)
                try:
                    mysql_con = self.connect_db()
                    print('connect successful')
                except:
                    print('connect error')
                try:
                    serverid = self.run_sql(mysql_con, "show variables like'server_id';")
                    print('read successful: ',':'.join(serverid))
                except:
                    print('read error')
                try:
                    insert_sql = self.get_sql('test',':'.join(serverid))
                    self.run_sql(mysql_con, insert_sql)
                    print('insert successful')
                except:
                    print('insert error')
                mysql_con.close()
            except:
                pass
            continue

if __name__ == '__main__':
    do_sql = RunSqlToMysql()
    do_sql.do()
