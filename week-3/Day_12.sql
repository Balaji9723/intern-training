create table users(
id int, 
name varchar(50),
age int);

insert into users values(101,'suresh', 28);
insert into users values(102,'ram', 33);
insert into users values(103,'ravi', 30);
insert into users values(104,'raju', 18);
insert into users values(105,'bai', 40);
insert into users values(106,'sankar', 50);

select * from users;


create table posts(
post_id serial primary key,
title varchar(100) not null,
content text,
user_id int,
foreign key (user_id) references users(id) );

insert into posts (title, content, user_id)
values('python','xxxxx', 101);

insert into posts (title, content, user_id)
values('java','wwwww', 102);
insert into posts (title, content, user_id)
values('python','zzzz', 103);
insert into posts (title, content, user_id)
values('HHHH','pppp', 101);
insert into posts (title, content, user_id)
values('IIII','oooo', 101);
insert into posts (title, content, user_id)
values('JJJ','nnnn', 102);
insert into posts (title, content, user_id)
values('KKKKK','mmmm', 103);

insert into posts (title, content, user_id)
values('QQQQ','qqqq', 104);
insert into posts (title, content, user_id)
values('XX','xxxx', 106);

select * from posts;

update posts set title = 'fastapi' 
where post_id = 5;

delete from posts
where post_id=5;

select * from users inner join posts
on users.id=posts.user_id;

select * from users left join posts
on users.id=posts.user_id;

select * from users right join posts
on users.id=posts.user_id;

select users.name, count (posts.user_id) from users join posts
on users.id=posts.user_id
group by users.name;


select * from users left join posts
on users.id=posts.user_id;

select users.name, posts.title from users right join posts on users.id=posts.user_id order by users.name;


select users.name, posts.title from users join posts on users.id=posts.user_id order by users.name;
