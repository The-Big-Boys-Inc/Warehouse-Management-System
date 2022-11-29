drop database if exists Warehouze;
create database if not exists Warehouze;
show databases;
use Warehouze;
CREATE TABLE Address (
  Address_id INT AUTO_INCREMENT,
  Country varchar(20) NOT NULL,
  Street varchar(20) NOT NULL ,
  City varchar(20) NOT NULL ,
  State varchar(20) NOT NULL ,
  Zip char(20) NOT NULL,
  PRIMARY KEY (Address_id)
);
insert into Address(Country,street,city,state,zip) values ('rwanda','45lake','kigali','Kimironko',0000),
('USA','45lake','NY','Poughkeepsie',2435),
('USA','75clark','NY','fishkill',7890),
('Belgium','45AVE','La ville','manic',335),
('USA','45lake','NY','Poughkeepsie',2435),
('USA','45lake','NY','Poughkeepsie',2435),
('USA','45lake','NY','Poughkeepsie',2435),
('USA','45lake','NY','Poughkeepsie',2435),
('USA','45lake','NY','Poughkeepsie',2435),
('USA','5lake','LA','newtown',1565);
select * from Address;
CREATE TABLE Customer (
  Customer_id INT AUTO_INCREMENT,
  First_name varchar(40) NOT NULL,
  Last_name varchar(40) NOT NULL ,
  c_password varchar(40) NOT NULL ,
  phone int NOT NULL ,
  email varchar(40) NOT NULL ,
  Address_id INT,
  PRIMARY KEY (Customer_id),
  FOREIGN KEY (Address_id) REFERENCES Address(Address_id)
);



set foreign_key_checks=0;
select * from Customer;

Select * from customer;
Alter table Customer add column parents varchar(30);
Alter table customer modify column parents int;
Alter table customer drop column parents;

insert into customer(First_name,Last_name,c_password, phone,email,Address_id)
 values
('Jacob','jane','password1',646785893,'bhac@gmail.com',1),
('Job','Mark','password1',646720893,'bcdc@gmail.com',2),
('Bill','Toamso','password1',657867786,'hbah@gmail.com',3),
('Nico','jane','password1',646785893,'bhac@gmail.com',6),
('Ricky','Isheja','password1',646785893,'bhac@gmail.com',8),
('Descartes','Abdilahi','password1',646785893,'bhac@gmail.com',9),
('Saeed','Musoni','password1', 646785893,'bhac@gmail.com',10);

set foreign_key_checks=1;
select * from customer;

CREATE TABLE Department (
  Dept_id INT AUTO_INCREMENT,
  Name varchar(20) NOT NULL,
  Description varchar(200) NOT NULL ,
  PRIMARY KEY (Dept_id)
);
insert into department(name,description)values('IT','In charge of IT'),
('HR','In charge of Human Resources'),('Operations','In charge of all business related Operations');
select * from department;

CREATE TABLE Employee (
  Employee_id INT AUTO_INCREMENT,
  First_name varchar(40) NOT NULL,
  Last_name varchar(40) NOT NULL,
  Dept_id INT,
  SSN int(10) NOT NULL ,
  Phone int(10) NOT NULL ,
  Address_id INT,
  PRIMARY KEY (Employee_id),
  FOREIGN KEY (Address_id) REFERENCES Address(Address_id),
  FOREIGN KEY (Dept_id) REFERENCES Department(Dept_id)
);
insert into employee(First_name,Last_name,Dept_id,SSN,phone,Address_id) values('John','doe',1,000000222,222111333,9),
('John','doe',1,000000333,111222333,3),
('John','doe',2,000000444,444222333,4),
('John','doe',3,000000555,000111222,5),
('John','doe',3,000000678,212323434,6),
('John','doe',3,000000777,121212121,7),
('John','doe',1,000000888,111000222,8),
('John','doe',2,000000999,909090909,9),
('John','doe',2,000000181,756876890,2);
select * from employee;
Update employee set First_name="Ricky" where Employee_id=1;
Update employee set First_name="Junior" where Employee_id=2;
Update employee set First_name="Isheja" where Employee_id=3;
Update employee set First_name="Big" where Employee_id=4;
Update employee set First_name="Boys" where Employee_id=5;
update employee set SSN=394039245 where employee_id=2;
SELECT SSN FROM employee WHERE First_name REGEXP 'or$';

CREATE TABLE Product (
  Product_id INT AUTO_INCREMENT,
  Product_name varchar(40) NOT NULL,
  Description varchar(40) NOT NULL ,
  Manifacturer varchar(40) NOT NULL ,
  Expiration_date varchar(40) NOT NULL ,
  PRIMARY KEY (Product_id, Product_name )
);
 select * from Product;
 insert into Product(Product_name,description,manifacturer,Expiration_date)values('riham','biscuit','axzam',12/3/2021),
 ('MT dew','Drink','dew',1/3/2021),
 ('T-shirt','Clothes','Gucci',12/4/2021),
 ('Hoddie','Clothes','LV',12/3/2021),
 ('laptop','Tech','HP',13/4/2022),
 ('Macbook pro','tech','Apple',4/3/2022),
 ('Books','paperterie ','axzam',12/3/2023);

CREATE TABLE Supplier (
  Supplier_id INT AUTO_INCREMENT,
  First_name varchar(40) NOT NULL,
  Last_name varchar(40) NOT NULL ,
  phone int(10) NOT NULL ,
  SSN int(10) NOT NULL ,
  email varchar(40) NOT NULL ,
  Product_id INT,
  Payment varchar(40) NOT NULL,
  Quantity INT, 
  Price DOUBLE,
  Address_id INT,
  PRIMARY KEY (Supplier_id),
  FOREIGN KEY (Address_id) REFERENCES Address(Address_id),
  FOREIGN KEY (Product_id) REFERENCES Product(Product_id)
); 
insert into Supplier(First_name,Last_name,phone,SSN,email,payment,Quantity,Price,Address_id,Product_id)
values('John','Doe',832456789,000000111,'jaha@gxc.com','Credit card',5,5000,1,1),
('John','Doe',832456908,000000111,'jaha@gxc.com','Debit Card',5,2000,9,5),
('John','Doe',832263876,000000111,'jaha@gxc.com','Credit card',5,3000,3,1),
('John','Doe',832798725,000000111,'jaha@gxc.com','credit card',5,4000,2,2),
('John','Doe',832798723,000000111,'jaha@gxc.com','credit card',5,5000,1,3),
('John','Doe',832798725,000000111,'jaha@gxc.com','credit card',5,7000,4,5),
('John','Doe',832798722,000000111,'jaha@gxc.com','credit card',5,1000,5,7);
select * from Supplier;

CREATE TABLE Orders (
  Order_id INT AUTO_INCREMENT,
  Customer_id INT NOT NULL,
  Employee_id INT NOT NULL ,
  Date date DEFAULT NULL,
  PRIMARY KEY (Order_id),
  FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id),
  FOREIGN KEY (Employee_id) REFERENCES Employee(Employee_id)
);

insert into Orders(Customer_id,Employee_id)values(1,2),(3,4),(1,6);
select * from Orders;

CREATE TABLE Payment (
  Payment_id INT AUTO_INCREMENT,
  Payment_type varchar(40) NOT NULL,
  Date date DEFAULT NULL,
  Amount double NOT NULL,
  PayDueDate date DEFAULT NULL,
  PRIMARY KEY (Payment_id)
);
insert into Payment(Payment_type,Date,Amount,PayDueDate)value('Check',12/3/2021,2000,24/3/2021),
('Debit Card',12/6/2021,2000,24/12/2021),
('Check',12/5/2021,6000,24/11/2021),
('Credit Card',12/7/2021,5000,24/10/2021),
('Check',12/8/2021,200,24/9/2021);

select * from payment;

CREATE TABLE Order_detail (
  Receipt_id INT AUTO_INCREMENT,
  Customer_id INT NOT NULL,
  Order_id INT NOT NULL,
  Product_id INT NOT NULL,
  Product_name varchar(40) NOT NULL,
  Date date DEFAULT NULL,
  Quantity double NOT NULL,
  Amount double NOT NULL,
  Payment_id INT NOT NULL,
  FOREIGN KEY (Product_id, Product_name) REFERENCES Product(Product_id, Product_name),
  FOREIGN KEY (Customer_id) REFERENCES Customer(Address_id),
  FOREIGN KEY (Order_id) REFERENCES Orders(Order_id),
  FOREIGN KEY (Payment_id) REFERENCES Payment(Payment_id),
  PRIMARY KEY (Receipt_id, Payment_id)
);


CREATE TABLE Inventory (
  Inventory_id INT AUTO_INCREMENT,
  Name varchar(40) NOT NULL,
  Location varchar(40) NOT NULL ,
  Supplier_id INT ,
  Product_id INT ,
  Product_name varchar(40),
  Quantity double NOT NULL,
  Contact varchar(40) NOT NULL ,
  PRIMARY KEY (Inventory_id),
  FOREIGN KEY (Supplier_id) REFERENCES Supplier(Supplier_id),
  FOREIGN KEY (Product_id, Product_name) REFERENCES Product(Product_id, Product_name)
);
insert into Inventory(Name,Location,Quantity,Contact)value('biscuits','3rd street',2000,387873),
('Drinks','4th street',2000,384573),
('Clothes','1st street',2000,383873),
('Tech','5th street',2000,387323),
('biscuits','3rd street',2000,387873),
('biscuits','3rd street',2000,387873),
('biscuits','3rd street',2000,387873),
('biscuits','3rd street',2000,387873);



CREATE TABLE Supplies (
  Supplier_id INT ,
  Product_id INT ,
  PRIMARY KEY (Supplier_id,Product_id),
  FOREIGN KEY (Supplier_id) REFERENCES Supplier(Supplier_id),
  FOREIGN KEY (Product_id) REFERENCES Product(Product_id)
);


CREATE TABLE Work_for (
  Dept_id INT ,
  Employee_id INT ,
  PRIMARY KEY (Dept_id, Employee_id),
  FOREIGN KEY (Dept_id) REFERENCES Department(Dept_id),
  FOREIGN KEY (Employee_id) REFERENCES Employee(Employee_id)
);


create table roles( Role_name varchar(80), Role_specification varchar(80));

select * from Product; 