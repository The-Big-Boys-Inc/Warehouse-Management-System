
drop database Warehouze;
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

CREATE TABLE Customer (
  Customer_id INT AUTO_INCREMENT,
  First_name varchar(40) NOT NULL,
  Last_name varchar(40) NOT NULL ,
  phone int(10) NOT NULL ,
  email varchar(40) NOT NULL ,
  Address_id INT,
  PRIMARY KEY (Customer_id),
  FOREIGN KEY (Address_id) REFERENCES Address(Address_id)
);

CREATE TABLE Department (
  Dept_id INT AUTO_INCREMENT,
  Name varchar(40) NOT NULL,
  Description varchar(40) NOT NULL ,
  PRIMARY KEY (Dept_id)
);

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

CREATE TABLE Product (
  Product_id INT AUTO_INCREMENT,
  Product_name varchar(40) NOT NULL,
  Description varchar(40) NOT NULL ,
  Manifacturer varchar(40) NOT NULL ,
  Expiration_date varchar(40) NOT NULL ,
  PRIMARY KEY (Product_id, Product_name )
);
 select * from Product;

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

CREATE TABLE _Order (
  Order_id INT AUTO_INCREMENT,
  Customer_id INT NOT NULL,
  Employee_id INT NOT NULL ,
  Date date DEFAULT NULL,
  PRIMARY KEY (Order_id),
  FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id),
  FOREIGN KEY (Employee_id) REFERENCES Employee(Employee_id)
);

CREATE TABLE Payment (
  Payment_id INT AUTO_INCREMENT,
  Payment_type varchar(40) NOT NULL,
  Date date DEFAULT NULL,
  Amount double NOT NULL,
  PayDueDate date DEFAULT NULL,
  PRIMARY KEY (Payment_id)
);

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
  FOREIGN KEY (Order_id) REFERENCES _Order(Order_id),
  FOREIGN KEY (Payment_id) REFERENCES Payment(Payment_id),
  PRIMARY KEY (Receipt_id, Payment_id)
);

CREATE TABLE Inventory (
  Inventory_id INT AUTO_INCREMENT,
  Name varchar(40) NOT NULL,
  Location varchar(40) NOT NULL ,
  Supplier_id INT NOT NULL ,
  Product_id INT NOT NULL ,
  Product_name varchar(40) NOT NULL ,
  Quantity double NOT NULL,
  Contact varchar(40) NOT NULL ,
  PRIMARY KEY (Inventory_id),
  FOREIGN KEY (Supplier_id) REFERENCES Supplier(Supplier_id),
  FOREIGN KEY (Product_id, Product_name) REFERENCES Product(Product_id, Product_name)
);


CREATE TABLE Warehouse (
  Warehouse_id INT AUTO_INCREMENT,
  Name varchar(40) NOT NULL,
  Location varchar(40) NOT NULL ,
  Inventory_id INT NOT NULL ,
  Employee_id INT NOT NULL ,
  Contact varchar(40) NOT NULL ,
  PRIMARY KEY (Warehouse_id),
  FOREIGN KEY (Employee_id) REFERENCES Employee(Employee_id),
  FOREIGN KEY (Inventory_id) REFERENCES Inventory(Inventory_id)
);

































