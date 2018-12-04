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



