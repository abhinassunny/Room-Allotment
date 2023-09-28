DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS admin;
DROP TABLE IF EXISTS user;

CREATE TABLE rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    capacity INTEGER,
    location varchar
);

CREATE TABLE admin (
    a_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password varchar(20) NOT NULL
);

CREATE TABLE user (
    u_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password varchar(20) NOT NULL
);