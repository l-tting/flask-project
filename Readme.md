*INTRODUCTION TO GITHUB*
*Git* -> A version control system that keeps track of changes you make to your project over time
*Github* -> a cloud hosting / storage platform that hosts / stores git repositories

*repository* -> folder in Github

Github allows you to do the following:
1.store your projects securely online
2.back up your code
3.Collaborate with other developers
4.share your work with employers / clients
5.contribute to open source projects 


git config --global user.name " Your Name"
git config --global user.email " your email address"

*Pushing new code to Github*
1.Initializing git to track my files
**git init**

2.Connect local folder to my github repository
**git remote add origin https://github.com/l-tting/flask-project.git"**

3.Add files from local folder to my github repo
**git add .**

4.Commit before final push
 -> commit: a saved snapshot of your project
**git commit -m "My first commit"**


5.**git push origin main** or 
  **git push origin master**

  **master / main** -> branches -> 


*U* -> untracked
*A* -> added
*M* -> modified
 

*Updating existing code / repos in Github*
1.**git add .**
2.**git commit -m"added a p-tag in index"**
3.**git push origin master**


Run the following commands in your terminal:
1. pip install flask
2.pip install psycopg2-binary



create database flask_myduka;
\c flask_myduka

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    buying_price NUMERIC(20, 2) NOT NULL CHECK (buying_price >= 0),
    selling_price NUMERIC(20, 2) NOT NULL CHECK (selling_price >= 0)
);

CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);



insert into products(name,buying_price,selling_price)values('eggs',50,60);



**INTRODUCTION TO PSYCOPG2**
Psycopg2 is a driver that connects Python to a Postgres database
conn -> a avriable that represents our connection to Postgres
psycopg2.connect() -> a function that is used to establish a connection to the db

1.host -> where is my Postgres located? on what server is it located -> localhost
2.port -> where in my server is the Postgres service running
3.user -> default postgres user
4.password -> password attached to the user to allow login
5.dbname -> the name of the database you want to connect to


*ip addresses and domain names*
IP address -> a number used to uniquely identify a device on a network
types -> ipv4 and ipv6
    ipv4 -> 192.181.102.255
    google builds an app -> make it available to end users (deploy) -> server(ip address)

Domain name -> a human friendly name for an ip address
192.181.102.255 -> www.google.com

your local device has a default ip address of 127.0.0.1
127.0.0.1 -> ip address for your local device
localhost -> domain name for 127.0.0.1


*performing db operations using psycopg2*
-> to perform db operations in psycopg2 we use an object called cursor
cur -> object responsible for db operations; select , insert, update, delete
*cur.execute()* -> a function meant to execute sql queries
*cur.fetchall()* -> a function responsible for fetching data from Postgres to Python
*conn.commit()* -> permanently save your changes to the database


*task*
using functions write code that does the following:
1.fetches sales data
2.inserts sales data





