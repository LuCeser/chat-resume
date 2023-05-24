CREATE TABLE `tb_position` (
	id INT auto_increment NOT NULL,
	name VARCHAR(100) DEFAULT '' NOT NULL COMMENT '发布的岗位名',
	requirements json NULL COMMENT '岗位要求',
	qualifications json NULL COMMENT '任职资格',
	create_dt DATETIME NOT NULL COMMENT '创建日期',
	update_dt DATETIME NOT NULL COMMENT '最后更新日期',
	PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;
