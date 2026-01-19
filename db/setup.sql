create database bookstore character set utf8;

 create user 'baolinh'@'localhost' identified by 'Baolinh56';
 grant all on bookstore.* to 'baolinh'@'localhost';