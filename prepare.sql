CREATE DATABASE testdb;
CREATE TABLE testdb.test(
  id int(12) NOT NULL AUTO_INCREMENT,
  timestamp varchar(50) DEFAULT NULL,
  msg varchar(255) DEFAULT NULL,
  other varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=33811 DEFAULT CHARSET=utf8mb4;