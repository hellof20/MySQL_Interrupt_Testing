# MySQL_Interrupt_Testing
**MySQL_Interrupt_Testing** is a simple tool used to evaluate the time when the client connection is interrupted in the case of reboot, resize instance size, failover, read replica promotion, DNS switch, etc. of the MySQL Server.

The tool will perform three operations of connecting to the database, reading data and inserting data every 0.1 seconds. By observing whether these three operations are successful, it can judge whether the database is unable to connect, read data and write.

## Installation
```
$ git clone https://github.com/hellof20/MySQL_Interrupt_Testing.git
$ cd MySQL_Interrupt_Testing
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage
- prepare, create testing table
```
export host=your_mysql_host
export user=your_mysql_user
export password=your_mysql_password
mysql -h$host -u$user -p$password < prepare.sql
```

- run testing tool
```
$ python test_mysql.py
$ tail -f result.log
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
$ pkill python
```
