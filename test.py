# -*- coding:utf-8 -*-
#
import time
import random
import pymysql
import string

all_chs = string.digits + string.ascii_letters


def get_random_str(str_length):
    random_str_list = [random.choice(all_chs) for k in range(str_length)]
    return ''.join(random_str_list)


class RunSqlToMysql(object):
    def __init__(self):
        self.mysql_host = 'test-proxy.proxy-cxxaasocn4zh.us-west-1.rds.amazonaws.com'
        self.mysql_user = 'admin'
        self.mysql_password = '11111111'
        self.mysql_db_name = 'inputdb'

    def connect_db(self):
        con_engine = pymysql.connect(
            host=self.mysql_host,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_db_name,
            port=3306,
            charset='utf8mb4'
        )
        return con_engine

    @staticmethod
    def run_sql(db_connect, sql):
        # 使用cursor()方法获取游标
        cursor = db_connect.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
            db_connect.commit()  # 提交修改，类似github的commit操作
            print('Insert sql "%s" successfully' % sql)
        except:
            db_connect.rollback()  # 不成功则回滚
            print('Insert sql "%s" ERROR !!!' % sql)

    @staticmethod
    def get_sql(table_name):
        field_str = 'timestamp, msg, other'
        values_str = "'%s', '%s', '%s'" % (str(int(time.time())), get_random_str(64), get_random_str(200))
        sql_sentence = "insert into %s(%s) values (%s);" % (table_name, field_str, values_str)
        return sql_sentence

    def do(self):
        mysql_con = self.connect_db()
        while True:
            insert_sql = self.get_sql('new_tab')
            self.run_sql(mysql_con, insert_sql)
            time.sleep(0.1)


if __name__ == '__main__':
    do_sql = RunSqlToMysql()
    do_sql.do()

