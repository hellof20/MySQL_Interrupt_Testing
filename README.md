# MySQL_Interrupt_Testing
**MySQL_Interrupt_Testing** is a simple tool used to evaluate the time when the client connection is interrupted in the case of reboot, resize instance size, failover, read replica promotion, DNS switch, etc. of the MySQL database.

## Installation
```
$ git clone https://github.com/hellof20/MySQL_Interrupt_Testing.git
$ cd MySQL_Interrupt_Testing
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage
- create testing table
```
$ export mysql_host=your_mysql_host
$ export mysql_user=your_mysql_user
$ export mysql_password=your_mysql_password
$ export mysql_db_name=your_mysql_db_name
$ mysql -h$mysql_host -u$mysql_user -p$mysql_password $mysql_db_name < test_table.sql
```

- run testing tool
```
$ nohup python testwrite.py > testresult.log 2>&1 &
```
## Display of test results

test mysql server reboot interrupt time , about 6 seconds

```
(venv) pwmglobal:~/environment/MySQL_Interrupt_Testing (master) $ cat testresult.log |grep -B 4 'connect error'                                                     
read successful:  server_id:1494392185
insert successful
----------------------------
2021-08-22 15:42:39.668227
connect error
read error
insert error
----------------------------
2021-08-22 15:42:39.769548
connect error
read error
insert error
----------------------------
。。。

----------------------------
2021-08-22 15:42:45.120825
connect error
read error
insert error
----------------------------
2021-08-22 15:42:45.221682
connect error
```

## Stop Testing
```
pkill python
```
