# -*- coding:utf-8 -*-
import time
import random
import pymysql
import string
import datetime

all_chs = string.digits + string.ascii_letters


def get_random_str(str_length):
    random_str_list = [random.choice(all_chs) for k in range(str_length)]
    return ''.join(random_str_list)


class RunSqlToMysql(object):
    def __init__(self):
        self.mysql_host = 'pproxy.proxy-cdagscjv6mu0.ap-southeast-1.rds.amazonaws.com'
        #self.mysql_host = 'aurora.cluster-cdagscjv6mu0.ap-southeast-1.rds.amazonaws.com'
        #self.mysql_host = 'pm1.cdagscjv6mu0.ap-southeast-1.rds.amazonaws.com'
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
            
    @staticmethod
    def get_sql(table_name,server_id):
        field_str = 'timestamp, msg, other'
        values_str = "'%s', '%s', '%s'" % (datetime.datetime.now(), get_random_str(64), server_id)
        sql_sentence = "insert into %s(%s) values (%s);" % (table_name, field_str, values_str)
        return sql_sentence

    def do(self):
        while True:
            try:
                time.sleep(0.1)
                mysql_con = self.connect_db()
                serverid = self.run_sql(mysql_con, "show variables like'server_id';")
                print(datetime.datetime.now(),':'.join(serverid))
                insert_sql = self.get_sql('test',':'.join(serverid))
                self.run_sql(mysql_con, insert_sql)
                mysql_con.close()
            except:
                print('connect fail')
            continue

if __name__ == '__main__':
    do_sql = RunSqlToMysql()
    do_sql.do()