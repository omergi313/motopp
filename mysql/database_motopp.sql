USE motopp;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    name VARCHAR(1000)
);


CREATE TABLE bike (
    id SERIAL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    description VARCHAR(1000),
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);