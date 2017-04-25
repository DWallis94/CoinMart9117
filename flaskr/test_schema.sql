drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
drop table if exists users;
create table users (
  username text primary key,
  password text not null
);

insert into users values('admin', 'default');

insert into users values('test', 'test123');

