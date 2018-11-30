
-- create table orderList(
--     ID int NOT NULL AUTO_INCREMENT,
--     cID int NOT NULL,
--     pID int NOT NULL,
--     quantity int NOT NULL,
--     price decimal(18, 2),
--     primary key(ID),
-- 	FOREIGN KEY (pID) REFERENCES product(pID),
--     FOREIGN KEY (cID) REFERENCES customer(cID)
-- );

-- alter table business_cus rename column annu_income to remain
-- alter table home_cus rename column income to remain
-- alter table orderList add column placetime datetime DEFAULT CURRENT_TIMESTAMP


select * from home_cus;
select * from orderList；
select * from customer;
select * from address;
select * from business_cus;




