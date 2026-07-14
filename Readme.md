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


*Data format of data fetched using psycopg2*
-> Our data from cur.fetchall() is returned in a list of tuples
list-> contains all rows returned from the database
tuple -> represents a single row of record

*function* - reusable block of code meant to perform a specific task
To make functions reusable we use parameters
*parameters & arguments*
*parameter* - a placeholder variable meant to make a function reusable
*argument* - a real value passed in place of a parameter when calling the function


*fetching data from two tables*

1.sales per product


sales per product -> sales & product name
sales (products & sales) -> selling_price * quantity -> product name

select products.name as p_name , sum(products.selling_price * sales.quantity) as total_sales from products join sales on sales.pid = products.id group by p_name;

*multiline strings* -> allow us to have strings that traverse more than one line by
using tripple openinng and closing quotations

*task*
Using functions write code that fetches the following data:
    2.sales per day
    3.profit per product
    4.profit per day

*must know* 
1.SQL - basic queries ,pk & fk , joins , aggregate functions, filter clauses , group by 
2.Python - data types , data structures(lists and tuples), conditional statements , loops, functions(emphasis)



*OOP*
-> Object Oriented Programming : a paradigm / concept where programs are built around 
classes and objects
-> We have 2 broad classifications of data types in Python
1.Inbuilt data types : come with the programming language
2.user defined / custom data types: -> built using classes and objects


*class* - a blueprint / template for creating objects
*object* - an instance of a class

class -> sketch of the building 
object -> real building created from the sketch

-> Any class has the following 3 things:
1.Identity - the unique name of a class
2.State - defined by attributes of a class
        -> answers the question: what does a class have?
        *attribute* - a variable inside a class
3.Behaviour -> defined by methods of a class 
        -> answers the question: what can a class do? 
        *method* - a function inside a class


class Car:
identity -> Car
state -> make, model, yom, is_imported,colour,no_of_doors
behaviour -> move, stop , carry goods, 


Define the following classes with their identity, state and behavior:
-> class Student
      identity -> Student
      state -> name,age , course
      behaviour -> study, eat ,sleep, walk

-> class Phone
-> class Dog

def __init__() -> a constructor
*Constructor* -> a special method that is automatically called when creating
objects used to initialize these objects with some data 
*self* - references an object itself
*dunder method* -> double underscore methods


*task*
OOP Task 1.Create a class called BankAccount with the following attributes: -account number -balance -owner name -date opened 2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() -display_info() 3.Create two BankAccount objects that can deposit, withdraw and display_info


**OOP Concepts**
-> Inheritance -> method overriding
-> Polymorphism -> method overloading
-> Abstraction
-> Encapsulation


*FLASK*
-> A python framework used to build robust web applications

*framework vs library*
Analogy: Building a house

Scenario 1:
David intends to build a house.he recognizes that he is not an expert in this field and decides to seek the help of
professionals(architrect,engineers,construction workers). The process ends up becoming simpler since these experts have
domain knowledge and experience in this field but David has to do everything exactly as advised by these experts.
Conclusion: Process is simpler and faster but very strict guidelines must be followed
----> Framework

Scenario 2:
Jerry also intends to build a house. He decides not to seek the help of any professional but rather he does everything 
by himself. The process is much harder but very flexible because he gets to decide what to do at every stage.
Conclusion: process is much harder but flexible
-----> Library

*framework* - a prebuilt structure of code and tools used to help developers build applications by making the development
process much easier where they dont have to build the application from scratch but it enforces very strict guidelines
that must be followed.

*Examples of frameworks*
1.Python -> Flask, Django, FastAPI
2.JavaScript -> React , Angular , Vue, Svelte
3.Java -> Spring
4.C# -> .NET
5.PHP -> Laravel
6.Go -> Chi, Gin
7.Ruby -> Ruby on Rails


*Flask*
*Routing in Flask*
-> Routing is a mechanism that maps or connects urls to Python functions
*url* -> uniform resource locator -> the full address used to access and application
e.g. https://meet.google.com/dsh-idtb-oqb

**Parts of a url**
1.protocol -> tells the browser how to communicate (http or https)
        *http* -> hypertext transfer protocol (transfers data as raw text)
        *https* -> hypertext transfer protocol secure (transfers data in encrypted format)
        *http -> https* -> ssl / tls certificate(free)
2.domain name -> human friendly name used in place of an ip address
3.Path/Rule -> specific resource to be accessed in an appliation
4.Port(optional)

 https://meet.google.com/
https://meet.google.com/dsh-idtb-oqb
 


 www.instagram.com/profile







