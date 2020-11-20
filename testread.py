# -*- coding:utf-8 -*-
import time
import random
import pymysql
import string
import datetime

class RunSqlToMysql(object):
    def __init__(self):
        self.mysql_host = 'pproxy.proxy-cdagscjv6mu0.ap-southeast-1.rds.amazonaws.com'
        self.mysql_user = 'admin'
        self.mysql_password = 'Pjy#0618'
        self.mysql_db_name = 'pp'

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

    def do(self):
        while True:
            try:
                time.sleep(0.3)
                mysql_con = self.connect_db()
                serverid = self.run_sql(mysql_con, "show variables like'server_id';")
                mysql_con.close()
                print(datetime.datetime.now(),':'.join(serverid))
            except:
                print('connect fail')
            continue

if __name__ == '__main__':
    do_sql = RunSqlToMysql()
    do_sql.do()
