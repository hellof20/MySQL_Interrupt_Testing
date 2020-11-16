CREATE TABLE `test` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `timestamp` varchar(30) DEFAULT NULL COMMENT '时间戳',
  `msg` varchar(255) DEFAULT NULL COMMENT '信息',
  `other` varchar(255) DEFAULT NULL COMMENT '随机字符',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33811 DEFAULT CHARSET=utf8mb4;
