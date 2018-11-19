from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import exists
from models import *

dbUrl = "mysql+pymysql://root:Tangziqi1996@localhost/greeneat?host=localhost?port=3306"
engine = create_engine(dbUrl)
meta = MetaData(bind=engine)
Base = declarative_base()
Session = sessionmaker(bind=engine)
sessionDB = Session()

# customer = Table("customer", meta, autoload=True, autoload_with=engine)
# address = Table("address", meta, autoload=True, autoload_with=engine)
# bCustomer = Table("business_cus", meta, autoload=True, autoload_with=engine)
# hCustomer = Table("home_cus", meta, autoload=True, autoload_with=engine)
# product = Table("product", meta, autoload=True, autoload_with=engine)
# region = Table("region", meta, autoload=True, autoload_with=engine)
# salesperson = Table("salesperson", meta, autoload=True, autoload_with=engine)
# store = Table("store", meta, autoload=True, autoload_with=engine)
# transact = Table("transact", meta, autoload=True, autoload_with=engine)

# emailExist = sessionDB.query(exists().where(Customer.email == 'yiweiyh@gmail.com')).scalar()

# record = sessionDB.query(Product).filter(Product.p_name.like('%Women%'))
# print(type(record))     # <class 'sqlalchemy.orm.query.Query'>
#
# for r in record:
#     print(r.p_name)

# aID = []
# stID = []
# address = sessionDB.query(Addres).filter(Addres.street.like('%happy%'))
# for a in address:
#     aID.append(a.aID)
# store = sessionDB.query(Store).filter(Store.aID.in_(aID))
# for s in store:
#     stID.append(s.stID)
# product = sessionDB.query(Product).filter(Product.stID.in_(stID))
# for p in product:
#     print(p.p_name)

