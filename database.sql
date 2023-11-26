create table graphs
(
    `index`  int auto_increment comment '序号'
        primary key,
    id       int    not null comment 'ID',
    name     text   not null comment '姓名',
    gender   text   not null comment '性别',
    age      double not null comment '年龄',
    nation   text   not null comment '民族',
    position text   not null comment '地区',
    location text   not null comment '文件地址',
    kind     text   not null comment '影像数据类型'
);