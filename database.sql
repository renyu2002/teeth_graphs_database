create table graphs
(
    `index`  int auto_increment comment '���'
        primary key,
    id       int    not null comment 'ID',
    name     text   not null comment '����',
    gender   text   not null comment '�Ա�',
    age      double not null comment '����',
    nation   text   not null comment '����',
    position text   not null comment '����',
    location text   not null comment '�ļ���ַ',
    kind     text   not null comment 'Ӱ����������'
);