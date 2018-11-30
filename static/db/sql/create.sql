

CREATE TABLE address(
aID varchar(20) NOT NULL,
street varchar(20) NOT NULL,
city varchar(20) NOT NULL,
zip_code varchar(10) NOT NULL,
    PRIMARY KEY (aID) 
);

CREATE TABLE customer(
cID varchar(20) NOT NULL,
fname varchar(20) NOT NULL,
lname varchar(20) NOT NULL,
email varchar(30) NOT NULL,
passwords varchar(20) NOT NULL,
kind char(20) NOT NULL,
aID varchar(20) NOT NULL,
    PRIMARY KEY (cID),
    FOREIGN KEY (aID) REFERENCES address (aID),
    UNIQUE (email)
);

CREATE TABLE business_cus(
cID varchar(20) NOT NULL,
annu_income decimal(18,2), 
category varchar(20),
    PRIMARY KEY (cID),
    FOREIGN KEY (cID) REFERENCES customer(cID)
);


CREATE TABLE home_cus(
cID varchar(20) NOT NULL,
age varchar(10),
income decimal(18,2), --XXXX.XX
marriage integer not null CHECK (marriage in (0,1)), --Y(1)/N(0)
    PRIMARY KEY (cID),
    FOREIGN KEY (cID) REFERENCES customer(cID)
    
);

CREATE TABLE product(
pID varchar(20) NOT NULL,
name varchar(50) NOT NULL,
amount integer NOT NULL,
price decimal(18,2) NOT NULL,
kind varchar(20) NOT NULL,
picture varchar(30),
    PRIMARY KEY (pID)
);

create table region(
	rID varchar(20),
	r_manager varchar(20) not null,
	r_name varchar(20) not null,
	primary key (rID)
);

create table store(
	stID varchar(20),
	st_manager varchar(20),
	stuff_number varchar(10),
	aID varchar(20),
	rID varchar(20),
	primary key (stID),
	foreign key (aID) references address(aID)
		on delete cascade,
	foreign key (rID) references region(rID)
		on delete cascade
);

create table salesperson(
	saID varchar(20),
	name varchar(20),
	email varchar(30),
	job varchar(30),
	salary decimal(18,2),
	aID varchar(20),
	stID varchar(20),
	primary key (saID),
	foreign key (aID) references address(aID)
		on delete cascade,
	foreign key (stID) references store(stID)
		on delete cascade
);

CREATE TABLE transact(
order_num varchar(20) NOT NULL,
pID varchar(20) NOT NULL,
saID varchar(20) NOT NULL,
cID varchar(20) NOT NULL,
t_date date NOT NULL,
quantitiy integer NOT NULL,
    PRIMARY KEY (order_num),
    FOREIGN KEY (pID) REFERENCES product(pID),
    FOREIGN KEY (saID) REFERENCES salesperson(saID),
    FOREIGN KEY (cID) REFERENCES customer(cID)
);

