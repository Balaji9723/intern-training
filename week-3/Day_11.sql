
-- Day-11 postgresql

create table users(
id serial primary key,
name varchar(100) not null,
emailid varchar(100) unique
);

select * from users;


insert into users values(1,"balaji","aaaa@gmail.com");

select * from users;

insert into users values(1,'balaji','aaaa@gmail.com');


insert into users values(2,'karthi','bbbb@gmail.com');
insert into users values(3,'harish','cccc@gmail.com');
insert into users values(4,'aakash','dddd@gmail.com');
insert into users values(5,'arun','eeee@gmail.com');
select * from users;



select * from users
where name like 'a%';

SELECT *
FROM users
ORDER BY name DESC;

SELECT *
FROM users
WHERE emailid like '%gmail.com'
ORDER BY id;

select * from users
where name like '%i';

SELECT *
FROM users
WHERE id > 2;






