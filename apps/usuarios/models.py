from django.db import models

# Create your models here.
"""
-- DOMAINS
Create domain AreaCode as Varchar(5);
Create domain EmployeeKey as Varchar(5);
Create domain ClientKey as Varchar(5);
Create domain ProductKey as Varchar(10);
Create domain CategoryKey as Varchar(10);
Create domain ProviderKey as Varchar(10);
Create domain NotificationKey as Varchar(10);

-- CREATE TABLE
Create table Area (
	area_code AreaCode NOT NULL,
	area varchar(30) NOT NULL,
    primary key (area_code)
) Without Oids;

* empleado
    - id
    - email
    - password
    - nombre
    - apellido
    - fecha_inicio
    - area
    - sueldo
    - is_super_user
    - is_area_admin

-- CREATE TABLE
CREATE TABLE Employee (
    emp_key EmployeeKey NOT NULL, 
    email varchar(75) NOT NULL UNIQUE, 
    password varchar(128) NOT NULL, 
    first_name varchar(50) NOT NULL, 
    last_name varchar(50) NOT NULL, 
    date_joined timestamp with time zone NOT NULL,
    area AreaCode,
    is_superuser boolean NOT NULL, 
    is_areaadmin boolean NOT NULL, 
    is_simplemortal boolean NOT NULL, 
    primary key (emp_key)
) Without Oids;

-- FOREIGN KEYS Employee
Alter table Employee add foreign key (area) references Area (area_code) on update cascade on delete set null;

* cliente
    - claveCliente
    - nombre
    - RFC
    - direccion
    - correo
    - telefono

-- CREATE TABLE
CREATE TABLE Client (
    client_key ClientKey NOT NULL, 
    name varchar(50) NOT NULL,
    rfc varchar(128) NOT NULL UNIQUE, 
    address varchar(60) NOT NULL, 
    email varchar(75), 
    phone varchar(30), 
    primary key (client_key)
) Without Oids;

-- CREATE TABLE
CREATE TABLE Category (
    category_key CategoryKey NOT NULL, 
    name varchar(75) NOT NULL, 
    description varchar(128), 
    primary key (category_key)
) Without Oids;

-- CREATE TABLE
CREATE TABLE Provider (
    provider_key ProviderKey NOT NULL, 
    name varchar(50) NOT NULL,
    rfc varchar(128) NOT NULL UNIQUE, 
    address varchar(60) NOT NULL, 
    email varchar(75), 
    phone varchar(30), 
    primary key (provider_key)
) Without Oids;

-- CREATE TABLE
CREATE TABLE Product (
    product_key ProductKey NOT NULL, 
    name varchar(75) NOT NULL, 
    description varchar(128), 
    price numeric(10,2) NOT NULL, 
    category CategoryKey,
    provider ProviderKey,
    primary key (product_key)
) Without Oids;

-- FOREIGN KEYS Product
Alter table Product add foreign key (category) references Category (category_key) on update cascade on delete set null;
Alter table Product add foreign key (provider) references Provider (provider_key) on update cascade on delete set null;

CREATE TABLE Stock (
    id serial NOT NULL,
    product ProductKey,
    amount numeric(10),
    primary key(id)
) Without Oids;

-- FOREIGN KEYS Stock
Alter table Stock add foreign key (product) references Product (product_key) on update cascade on delete cascade;

CREATE TABLE Purchase (
    id serial NOT NULL,
    product ProductKey NOT NULL,
    amount numeric(10) NOT NULL,
    provider ProviderKey,
    total numeric(12,2),
    buyer EmployeeKey NOT NULL,
    purchase_date timestamp with time zone NOT NULL,
    primary key(id)
) Without Oids;

CREATE TABLE Purchase (
    id serial NOT NULL,
    product ProductKey NOT NULL,
    amount numeric(10) NOT NULL,
    provider ProviderKey,
    total numeric(12,2),
    buyer EmployeeKey NOT NULL,
    purchase_date timestamp with time zone NOT NULL,
    primary key(id)
) Without Oids;

-- FOREIGN KEYS Purchase
Alter table Purchase add foreign key (provider) references Provider (provider_key) on update cascade on delete set null;
Alter table Purchase add foreign key (buyer) references Employee (emp_key) on update cascade on delete set null;

CREATE TABLE Sale (
    id serial NOT NULL,
    product ProductKey NOT NULL,
    amount numeric(10) NOT NULL,
    client ClientKey,
    total numeric(12,2),
    seller EmployeeKey NOT NULL,
    sale_date timestamp with time zone NOT NULL,
    primary key(id)
) Without Oids;

-- FOREIGN KEYS Sale
Alter table Sale add foreign key (client) references Client (client_key) on update cascade on delete set null;
Alter table Sale add foreign key (seller) references Employee (emp_key) on update cascade on delete set null;

CREATE TABLE Notification (
    notification_key NotificationKey NOT NULL,
    transmitter EmployeeKey,
    description varchar(128),
    transmitter_area AreaCode,
    primary key(notification_key)
) Without Oids;

-- FOREIGN KEYS Notification
Alter table Notification add foreign key (transmitter) references Employee (emp_key) on update cascade on delete set null;
Alter table Notification add foreign key (transmitter_area) references Area (area_code) on update cascade on delete set null;

CREATE TABLE NotiAdmin (
    id serial NOT NULL,
    last_notification NotificationKey,
    area_admin EmployeeKey,
    primary key(id)
) Without Oids;

-- FOREIGN KEYS Notification
Alter table NotiAdmin add foreign key (last_notification) references Notification (notification_key) on update cascade on delete cascade;
Alter table NotiAdmin add foreign key (area_admin) references Employee (emp_key) on update cascade on delete cascade;

-- INSERTS Area
INSERT INTO Area VALUES('AAVEN','Administrador Ventas');
INSERT INTO Area VALUES('AACOM','Administrador Compras');
INSERT INTO Area VALUES('AAALM','Administrador Almacén');
INSERT INTO Area VALUES('SADMI','Super Administrador');
INSERT INTO Area VALUES('AA','Área Almacén');
INSERT INTO Area VALUES('AC','Área Compras');
INSERT INTO Area VALUES('AV','Área Ventas');

-- INSERTS Employee
INSERT INTO Employee VALUES('SA001','edgar@mail.com','pbkdf2_sha256$150000$wE9JmStZJWPh$TRMl/z4tXQYs2VqerMc3di0d0trHq2tPANELEoxmjm4=','Edgar', 'Gómez', '2019-09-23 09:46:31.22461-05', 'SADMI', TRUE, FALSE, FALSE);
INSERT INTO Employee VALUES('SA002','paola@mail.com','pbkdf2_sha256$150000$k0PywcaQyaaV$v/aW088rgR4LrYXJKCgviu956N7j09bmDQz4fIBl2h0=','Paola', 'QuezadaAuu', '2019-09-23 09:46:31.22461-05', 'SADMI', TRUE, FALSE, FALSE);
-- Password: employee123
INSERT INTO Employee VALUES('AA001','juan@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Juan', 'López', '2019-09-23 09:46:31.22461-05', 'AA', FALSE, FALSE, TRUE);
INSERT INTO Employee VALUES('AC001','maria@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Maria', 'Echeverria', '2019-09-23 09:46:31.22461-05', 'AC', FALSE, FALSE, TRUE);
INSERT INTO Employee VALUES('AV001','rodrigo@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Rodrigo', 'Huerta', '2019-09-23 09:46:31.22461-05', 'AV', FALSE, FALSE, TRUE);
-- Password: admin123
INSERT INTO Employee VALUES('AAC01','margarita@mail.com','pbkdf2_sha256$150000$xwzLHlVLuCzf$fdbqPpA02u1sVusR90/nAhu/b7DQUWcLqDzBAMkwaKM=','Margarita', 'Prado', '2019-09-23 09:46:31.22461-05', 'AACOM', FALSE, TRUE, FALSE);
"""
