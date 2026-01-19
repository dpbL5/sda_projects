create database bookstore character SET utf8;

create user 'baolinh'@'localhost' identified by 'password';

grant all on bookstore.* to 'baolinh'@'localhost';