select * from customer;

select * from home_cus;

create table shopList(
    ID int NOT NULL AUTO_INCREMENT,
    pID int NOT NULL,
    quantity int NOT NULL,
    price decimal(18, 2),
	FOREIGN KEY (pID) REFERENCES product(pID)
);

select * from shopList