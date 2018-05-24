

## 启动mysql数据库

1.运行窗口servers.msc

2.net start mysql57 

## SQL

### 1简述

```
-- SQL(Structured Query Language): 结构化查询语言(关系型数据库的编程语言)
-- DDL(数据定义语言): create(创建) / drop(删除) / alter(修改)
-- DML(数据操纵语言): insert(插入) / delete(删除) / update(更新) 
-- DQL(数据查询语言): select(选择)
-- DCL(数据控制语言): grant(授予权限) / revoke(召回权限) / begin(开启事务) / commit(提交事务) / rollback(回滚事务)

```

### 创建删除数据库

```
1.创建数据库并指定默认的字符集
create database school default charset utf8;
2.如果指定的数据库存在则删除该数据库
drop database if exists school;
3.切换到创建的数据库
use school;
```

### 关系型数据库的完整性指的是什么

```
1. 实体完整性: 每条记录都是独一无二的(主键/唯一约束/唯一索引)
2. 参照完整性: 表中的数据要参照其他表已有的数据(外键)
3. 域完整性: 数据是有效的(数据类型/非空约束/默认值约束/检查约束)
```

### 表的设计原则: 范式理论(1NF / 2NF / 3NF / BCNF)

```
范式级别指的是表设计的规范程度, 范式级别越高规范程度也就越高
-- 范式级别越高在插入/删除/更新数据时可能发生的问题就越少
-- 而且表中的数据冗余度(重复)也就越低
-- 实际开发中往往会降低范式级别来提升查询数据的性能
-- 1NF - 列的属性值不能够再拆分
-- 2NF - 除了主键列之外的列要完全依赖于主键
-- 场景: 不同学院的学生可能有相同的学号
-- 学生表(stuid, sname, ssex, did, dname, dtel)
-- 主键(stuid, did)
-- sname和ssex依赖于stuid, 而dname和dtel依赖于depid
-- 这种依赖是部分依赖而不是完全依赖所以不满足2NF
-- 3NF - 消除传递依赖
-- 场景: 整个学校学生的学号是唯一的
-- 学生表(stuid, sname, ssex, did, dname, dtel)
-- 主键(stuid)
```

### mysql实际应用(学校选课系统)

```
1.创建学生表
create table tb_student
(
stuid int not null comment '学号',
sname varchar(10) not null comment '姓名',
ssex bit default 1 comment '性别',
stel char(11) comment '联系电话',
sbirth date comment '出生日期',
primary key (stuid) -- 主键(primary key): 能够标识唯一一条记录的一个或多个列
);

2.修改学生表
-- 添加列
alter table tb_student add column saddr varchar(100);
-- 删除列
alter table tb_student drop column stel;

3.插入学生记录
-- 插入所有列
insert into tb_student values (1001, '王大锤', 1, '1990-2-12', '四川成都');
-- 插入指定列
insert into tb_student (sname, stuid) values ('骆昊', 1002);
insert into tb_student (stuid, sname, ssex) values (1003, '杨飘飘', 0);
-- 一次插入多行
insert into tb_student values 
(1004, '张三丰', 1, '1940-12-3', '湖北武汉'),
(1005, '黄蓉', 0, '1975-3-25', '山东东营'),
(1006, '杨过', 1, '1987-1-19', '湖南长沙');
-- 删除数据
-- delete from tb_student where stuid=1003;

4.更新数据
-- 通常情况下更新或删除单条数据都是以ID字段(主键)作为条件
update tb_student set sbirth='1980-11-28', saddr='四川德阳' 
where sname='骆昊';
-- update tb_student set saddr='四川绵阳' 
-- where stuid=1004 or stuid=1005 or stuid=1006;
update tb_student set saddr='四川绵阳' 
where stuid in (1004, 1005, 1006);

5.创建课程表
create table tb_course
(
courseid int not null comment '课程编号',
cname varchar(20) not null comment '课程名称',
ccredit int not null comment '学分',
primary key (courseid)
);

插入课程数据
insert into tb_course (courseid, cname, ccredit) values 
(1111, 'Python程序设计', 4),
(2222, 'HTML程序设计', 2),
(3333, 'Linux操作系统', 1),
(4444, '数据库基础', 1);

6.创建学生选课表
-- 关系型数据用两种表无法表示实体之间的多对多关联
-- 可以通过中间表来建立学生和课程之间的多对多关系
-- 在实际开发中不建议使用复合主键而且尽可能使用跟业务无关的列做主键
-- int类型的主键可以通过auto_increment设置为自增主键
create table tb_sc
(
scid int not null auto_increment comment '选课编号',
sid int not null comment '学生编号',
cid int not null comment '课程编号',
score float comment '考试成绩',
primary key (scid)
);
-- 添加外键约束
-- 学生选课表中的学生编号参照了学生表的学号
alter table tb_sc add constraint fk_sc_sid 
foreign key (sid) references tb_student (stuid);
-- 学生选课表中的课程编号参照了课程表的课程编号
alter table tb_sc add constraint fk_sc_cid 
foreign key (cid) references tb_course (courseid);
-- 插入学生选课数据
insert into tb_sc (sid, cid, score) values 
(1001, 1111, 90),
(1001, 2222, 80),
(1001, 3333, 70),
(1001, 4444, 60),
(1002, 1111, 60),
(1002, 3333, 95),
(1002, 4444, 68),
(1004, 1111, 55.5),
(1004, 4444, 45.5),
(1005, 1111, 87.5), 
(1005, 3333, 63),
(1005, 4444, 72.5),
(1006, 1111, 78.5),
(1006, 4444, 35);

查询:
-- 查询所有学生信息
select * from tb_student;
select * from tb_course;
select * from tb_student, tb_course; -- 笛卡尔积
-- 投影和别名: 查询所有课程名称和学分
select sname as 姓名, ssex as 性别 from tb_student;
select sname as 姓名, case ssex when 1 then '男' else '女' end  as 性别 from tb_student;

select cname as 课程名, ccredit as 学分 from tb_course;

-- 查询所有女学生的姓名和出生日期
select sname, sbirth from tb_student where ssex=0;
-- 查询所有学分大于2的课程
select courseid, cname from tb_course where ccredit>2;
-- 查询所有80后学生的姓名,性别和出生日期
select sname, ssex, sbirth from tb_student
where '1980-1-1'<=sbirth and sbirth<='1989-12-31';

select sname, ssex, sbirth from tb_student
where sbirth between '1980-1-1' and '1989-12-31';

-- 模糊查询:查询姓杨的学生姓名和性别
select * from tb_student where sname='杨过';
select * from tb_student where sname like '杨%';
-- 模糊查询: 查询姓杨的名字总共两个字的学生的姓名
select * from tb_student where sname like '杨_';
-- 模糊查询: 查询姓杨的名字总共三个字的学生的姓名
select * from tb_student where sname like '杨__';
-- 模糊查询: 查询带杨的名字的学生的姓名
select * from tb_student where sname like '%杨%';
-- 用正则表达式
-- select * from tb_student where sname regexp '^[骆杨].+';

-- 多条件和控制处理: 查询没有录入生日和家庭住址的学生姓名
-- 判断一个列是否为null的时候不能用=或<> 而要用is或者is not
select * from tb_student where sbirth is null or saddr is null;
-- 去重:查询学生的籍贯 关键字distinct
select DISTINCT saddr from tb_student where saddr is not null;
-- 排序 查询送学生的姓名和生日按年龄从大到小排列
select * from tb_student order by ssex asc, sbirth desc;
-- 筛和排序: 先筛选后排序
-- 查询所有录入了家庭地址的男学生的姓名,出生日期和家庭住址按年龄从小到大排列
select sname, sbirth, saddr from tb_student 
where saddr is not null and ssex=1
ORDER BY sbirth desc;
-- 聚合函数:查询年龄最大的学生的出生日期
-- max()/min()/sum/ avg()求平均/ count()计数
select min(sbirth) from tb_student;
select max(sbirth) from tb_student;
-- 查询男女学生的人数group by:分组,默认分组会排序,如果
-- 不需要排序,可以在后面增加order by null 增加语句性能
select count(stuid) from tb_Student;
select count(stuid) from tb_Student where ssex=1;
select ssex, count(stuid) from tb_student group by ssex;
select if(ssex, '男', '女') as 性别, count(*) as 人数
from tb_student group by ssex;
-- 先筛选(where) 再分组(group by)再筛选(having)再排序(order by)
select if(ssex, '男', '女') as 性别, count(*) as 人数
from tb_student where saddr is not null
group by ssex order by ssex desc;
-- 聚合函数:查询课程编号为1111的课程的平均成绩
select cid, avg(score) from tb_sc where cid=1111;
-- 查询所有课程编号的平均成绩
select cid, avg(score) from tb_sc group by cid;
-- where 子句构造的筛选是分组以前的筛选
-- 如果希望对分组后的数据进行筛选 那么要用having
select cid, avg(score) from tb_sc 
group by cid having avg(score)<60;
-- 聚合函数: 查询学号为1001 的学生所有的课程的平均成绩'
select sid, avg(score) from tb_sc where sid=1001;
-- 查询每个学生的学号和平均成绩 把不及格的列出来
select sid, avg(score) from tb_sc
group by sid having avg(score)<60;
-- 子查询 查询年龄最大的学生的姓名
select sname, sbirth from tb_student
where sbirth=(select min(sbirth) from tb_student);
select sname, sbirth from tb_student
where sbirth=(select max(sbirth) from tb_student);
-- 子查询 查询选了两门以上的课程的学生姓名
-- sql and 语句先执行and右边的语句
select sname from tb_student
where stuid in(
select sid from tb_sc
group by sid having count(sid)>2) and ssex=1;
-- 连接查询
select sname, cname,score
from tb_sc, tb_student, tb_course
where sid=stuid and cid=courseid;
-- 连接查询 查询选课学生的姓名和平均成绩
select sname, avgscore from tb_student,
(select sid, avg(score) as avgscore from tb_sc
group by sid) t
where stuid=sid;
-- 连接查询:查询每个学生的姓名和选课数量
select sname,count from tb_student,
(select sid, count(cid) as count from tb_sc group by
sid) t where stuid=sid;
-- 内连接
select sname,cname,score from tb_sc
inner join tb_student on sid=stuid
inner join tb_course on cid=courseid
-- 左外连接, 左表不满足连表条件的记录也要查询出来
select sname,count from tb_student t1 left outer join
(select sid, count(cid) as count from tb_sc group by
sid) t2 on t1.stuid=t2.sid;

select sname,ifnull(count,0) as count from tb_student t1 left outer join
(select sid, count(cid) as count from tb_sc group by
sid) t2 on t1.stuid=t2.sid;

-- 右外连接:
select sname,ifnull(count,0) as count from 
(select sid, count(cid) as count from tb_sc group by
sid) t2 right outer join tb_student t1  on t1.stuid=t2.sid;

-- 全外连接:full outer join ,mysql不支持全外连接

-- 分页查询,本语法只支持mysql,不支持其他数据库
select sname,cname,score from tb_sc
inner join tb_student on sid=stuid
inner join tb_course on cid=courseid
-- limit 5;     -- 查询前面5条
order by score desc
limit 0, 5;    -- 0可以设置偏移量
-- limit 5 offset 0;
```

### DCL(数据控制语言)

```
-- 创建用户并指定登录口令
create user hellokitty identified by '123123';
-- 授予权限和召回权限
grant all on school.tb_student to hellokitty;
revoke all on school.tb_student from hellokitty;
grant select on school.tb_student to hellokitty;
grant all on school.* to hellokitty;
grant all on *.* to 'hellokitty'@'%';
revoke all on *.* from hellokitty;
-- 删除用户
drop user hellokitty;
```

### mysql实际应用(人力管理系统)

```
-- 创建人力资源管理系统数据库
drop database if exists HRS;
create database HRS default charset utf8;
-- 切换数据库上下文环境
use HRS;
-- 删除表
drop table if exists TbEmp;
drop table if exists TbDept;
-- 创建部门表
create table TbDept
(
dno int,										-- 部门编号
dname varchar(10) not null,	-- 部门名称
dloc varchar(20) not null,	-- 部门所在地
primary key (dno)
);
-- 添加部门记录
insert into TbDept values 
(10, '会计部', '北京'),
(20, '研发部', '成都'),
(30, '销售部', '重庆'),
(40, '运维部', '深圳');
-- 创建员工表
create table TbEmp
(
empno int primary key,			-- 员工编号
ename varchar(20) not null,	 -- 员工姓名
job varchar(20) not null,		-- 员工职位
mgr int,					-- 主管编号
sal int not null,			-- 员工月薪
comm int,					-- 每月补贴
dno int not null			-- 部门编号
);
-- 添加外键约束
alter table TbEmp add constraint fk_emp_dno foreign key (dno) references TbDept(dno);
-- 添加员工记录
insert low_priority into TbEmp values 
(7800, '张三丰', '总裁', null, 9000, 1200, 20),
(2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
(3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
(3211, '张无忌', '程序员', 2056, 3200, null, 20),
(3233, '丘处机', '程序员', 2056, 3400, null, 20),
(3251, '张翠山', '程序员', 2056, 4000, null, 20),
(5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
(5234, '郭靖', '出纳', 5566, 2000, null, 10),
(3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
(1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
(4466, '苗人凤', '销售员', 3344, 2500, null, 30),
(3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
(3577, '杨过', '会计', 5566, 2200, null, 10),
(3588, '朱九真', '会计', 5566, 2500, null, 10);

-- 查询薪资最高的员工姓名和工资 
select ename, sal from tbemp where sal=(select max(sal) from
tbemp)
-- 查询员工的姓名和年薪((月薪+补贴)*13) 字符串连接 concat
select concat(job,':',ename) as title, (sal + ifnull(comm,0))*13 s from TBEmp order by s desc; 
-- 查询所有员工的部门的编号和人数
select dno, count(ename) from TBEmp group by dno;
-- 查询所有部门的名称和人数 , 用的左链接
select dname 部门名称, ifnull(count,0) 部门人数 from tbdept t1 left outer join
(select dno, count(ename) as count from TBEmp group by dno) 
t2 on t1.dno=t2.dno;

-- 查询除老板外薪资最高的员工的姓名和工资
select ename, sal from tbemp where sal=(select max(sal) from
tbemp where mgr is not null)
-- 查询薪水超过平均薪水的员工的姓名和工资
select ename,sal from tbemp
where sal>(select avg(sal) from tbemp)

select ename, sal, avgsal from tbemp t1
inner join (select avg(sal) as avgsal from tbemp)
t2 on sal>avgsal;
-- 查询薪水超过其所在部门平均薪水的员工的姓名、部门编号和工资
select ename, t1.dno,sal from tbemp t1 inner join
(select dno, avg(sal) as avgsal from tbemp group by
dno) t2 on t1.dno=t2.dno and sal>avgsal;
-- 查询部门中薪水最高的人姓名、工资和所在部门名称
select ename, sal, dname from tbemp t1 inner join(
 select max(sal) maxsal, dno from tbemp group by dno) t2
 on t1.dno=t2.dno inner join 
 tbdept t3 on t2.dno= t3.dno where sal=maxsal;
-- 查询主管的姓名和职位
-- SQL 优化
-- 尽可能不使用distinck去重和in集合运算 可以使用exists和not exists替代
select ename, job from tbemp
where empno in(
select distinct mgr from tbemp where mgr is not null
);
select ename, job from tbemp t1
where exists (select 'x' from tbemp t2 where t1.empno=t2.mgr)
-- 查询薪资排名4~6名的员工姓名和工资
select ename, sal from tbemp
order by sal desc
limit 3, 3;
```

### 索引:相当于是一个目录,可以提升查询的效率,牺牲空间,节省时间

```
创建索引
create index idx_emp_ename on tbemp(ename);
删除索引
drop index idx_emp_ename;
查看索引
show index from tbemp;
```

### 事务:必须几个语句同时执行或者不执行

```
begin
语句1
语句2
...
commit/rollback

事务的特点 acid特性
1.原子性:不可分割,要么全成功要么全失败
2.一致性:事务前后数据状态要保持一致
3.隔离性:多个事务不能看到对方的中间状态
4.持久性:事务完成后数据要持久化

```



