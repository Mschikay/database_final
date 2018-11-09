from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import create_session

dbUrl = "mysql+pymysql://root:Tangziqi1996@localhost/greeneat?host=localhost?port=3306"
engine = create_engine(dbUrl)
meta = MetaData(bind=engine)


customer = Table("customer", meta, autoload=True, autoload_with=engine)
address = Table("address", meta, autoload=True, autoload_with=engine)
bCustomer = Table("business_cus", meta, autoload=True, autoload_with=engine)
hCustomer = Table("home_cus", meta, autoload=True, autoload_with=engine)
product = Table("product", meta, autoload=True, autoload_with=engine)
region = Table("region", meta, autoload=True, autoload_with=engine)
salesperson = Table("salesperson", meta, autoload=True, autoload_with=engine)
store = Table("store", meta, autoload=True, autoload_with=engine)
transact = Table("transact", meta, autoload=True, autoload_with=engine)

ins = address.insert()
ins = ins.values(aid='02', street='abc St', city='New York', zip_code='12345')
# print (address.columns)
# query = address.select()
# query = query.where(users.c.name=='jack')


session = create_session(bind=engine)
rest = session.query(customer).all()

print(rest)

