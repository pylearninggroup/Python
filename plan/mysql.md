```
mysql -u root -p 

 mysql >
 
 
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| meeting            |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

mysql> create database hello;
Query OK, 1 row affected (0.01 sec)

mysql> drop database hello;
Query OK, 0 rows affected (0.01 sec)

mysql> use hello;
Database changed


mysql> create table world(id int, name varchar(40),age int);
Query OK, 0 rows affected (0.01 sec)

mysql> show tables;
+-----------------+
| Tables_in_hello |
+-----------------+
| world           |
+-----------------+
1 row in set (0.00 sec)


mysql> drop table wo2rld;
Query OK, 0 rows affected (0.01 sec)

mysql> show tables;
+-----------------+
| Tables_in_hello |
+-----------------+
| world           |
+-----------------+
1 row in set (0.00 sec)

mysql> desc world;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int         | YES  |     | NULL    |       |
| name  | varchar(40) | YES  |     | NULL    |       |
| age   | int         | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.01 sec)


mysql> select * from world;
Empty set (0.01 sec)

mysql>
mysql> insert into world values(1,'benny',11);
Query OK, 1 row affected (0.00 sec)

mysql> insert into world values(2,'benny2',11);
Query OK, 1 row affected (0.01 sec)

mysql> insert into world values(3,'benny2',11);
Query OK, 1 row affected (0.00 sec)

mysql> select * from world;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    1 | benny  |   11 |
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
+------+--------+------+
3 rows in set (0.00 sec)


mysql> select * from world where id=1 and age >=22;
Empty set (0.00 sec)

mysql> select * from world where id=1 and age >=10;
+------+-------+------+
| id   | name  | age  |
+------+-------+------+
|    1 | benny |   11 |
+------+-------+------+
1 row in set (0.00 sec)


mysql> select * from world where id=1 or age >=11;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    1 | benny  |   11 |
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
+------+--------+------+
3 rows in set (0.00 sec)


mysql> select * from world limit 1;
+------+-------+------+
| id   | name  | age  |
+------+-------+------+
|    1 | benny |   11 |
+------+-------+------+
1 row in set (0.00 sec)

mysql> select * from world limit 10;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    1 | benny  |   11 |
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
+------+--------+------+
3 rows in set (0.00 sec)

mysql> select * from world order by age;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    1 | benny  |   11 |
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
|    1 | benny  |   33 |
|    1 | benny  |  314 |
+------+--------+------+
5 rows in set (0.01 sec)

mysql> select * from world order by age desc;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    1 | benny  |  314 |
|    1 | benny  |   33 |
|    1 | benny  |   11 |
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
+------+--------+------+
5 rows in set (0.00 sec)

mysql> select * from world order by name;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    1 | benny  |   11 |
|    1 | benny  |   33 |
|    1 | benny  |  314 |
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
+------+--------+------+
5 rows in set (0.00 sec)

mysql> select * from world order by name desc;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
|    1 | benny  |   11 |
|    1 | benny  |   33 |
|    1 | benny  |  314 |
+------+--------+------+
5 rows in set (0.00 sec)

mysql>


mysql> select * from world order by name desc limit 3;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
|    1 | benny  |   11 |
+------+--------+------+
3 rows in set (0.00 sec)

mysql> select * from world where age > 22 limit 3;
+------+-------+------+
| id   | name  | age  |
+------+-------+------+
|    1 | benny |   33 |
|    1 | benny |  314 |
+------+-------+------+
2 rows in set (0.00 sec)

mysql> select * from world where age > 22 order by name;
+------+-------+------+
| id   | name  | age  |
+------+-------+------+
|    1 | benny |   33 |
|    1 | benny |  314 |
+------+-------+------+
2 rows in set (0.00 sec)

mysql>

mysql> select name,id from world;
+--------+------+
| name   | id   |
+--------+------+
| benny  |    1 |
| benny2 |    2 |
| benny2 |    3 |
| benny  |    1 |
| benny  |    1 |
+--------+------+
5 rows in set (0.00 sec)

mysql> select name,id as 'student_id' from world;
+--------+------------+
| name   | student_id |
+--------+------------+
| benny  |          1 |
| benny2 |          2 |
| benny2 |          3 |
| benny  |          1 |
| benny  |          1 |
+--------+------------+
5 rows in set (0.00 sec)

mysql>


mysql> update world set name='benny3' where age=314;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from world;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    1 | benny  |   11 |
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
|    1 | benny  |   33 |
|    1 | benny3 |  314 |
+------+--------+------+
5 rows in set (0.00 sec)

mysql> update world set name='benny3',id=333 where age=314;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from world;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    1 | benny  |   11 |
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
|    1 | benny  |   33 |
|  333 | benny3 |  314 |
+------+--------+------+
5 rows in set (0.00 sec)

mysql>

mysql>
mysql> delete from world where id=333;
Query OK, 1 row affected (0.00 sec)

mysql> select * from world;
+------+--------+------+
| id   | name   | age  |
+------+--------+------+
|    1 | benny  |   11 |
|    2 | benny2 |   11 |
|    3 | benny2 |   11 |
|    1 | benny  |   33 |
+------+--------+------+
4 rows in set (0.00 sec)

mysql>


mysql> delete from world;
Query OK, 4 rows affected (0.01 sec)

mysql> truncate world;
Query OK, 0 rows affected (0.01 sec)

mysql> select world.id,world2.name from world,world2 where world.name=world2.name;
Empty set (0.00 sec)





```

