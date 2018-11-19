# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Addres(Base):
    __tablename__ = 'address'

    aID = Column(INTEGER(11), primary_key=True)
    street = Column(String(80), nullable=False)
    city = Column(String(20), nullable=False)
    zip_code = Column(String(10), nullable=False)


class Region(Base):
    __tablename__ = 'region'

    rID = Column(INTEGER(11), primary_key=True)
    r_manager = Column(String(20), nullable=False)
    r_name = Column(String(20), nullable=False)


class Customer(Base):
    __tablename__ = 'customer'

    cID = Column(INTEGER(11), primary_key=True)
    email = Column(String(30), nullable=False, unique=True)
    passwords = Column(String(20), nullable=False)
    kind = Column(String(20), nullable=False)
    aID = Column(ForeignKey('address.aID'), nullable=False, index=True)

    addres = relationship('Addres')


class BusinessCu(Customer):
    __tablename__ = 'business_cus'

    cID = Column(ForeignKey('customer.cID'), primary_key=True)
    b_name = Column(String(20), nullable=False)
    annu_income = Column(DECIMAL(18, 2))
    category = Column(String(20))


class HomeCu(Customer):
    __tablename__ = 'home_cus'

    cID = Column(ForeignKey('customer.cID'), primary_key=True)
    fname = Column(String(20), nullable=False)
    lname = Column(String(20), nullable=False)
    age = Column(String(10))
    income = Column(DECIMAL(18, 2))
    marriage = Column(INTEGER(11))


class Store(Base):
    __tablename__ = 'store'

    stID = Column(INTEGER(11), primary_key=True)
    st_manager = Column(String(20))
    stuff_number = Column(String(10))
    aID = Column(ForeignKey('address.aID', ondelete='CASCADE'), nullable=False, index=True)
    rID = Column(ForeignKey('region.rID', ondelete='CASCADE'), nullable=False, index=True)

    addres = relationship('Addres')
    region = relationship('Region')


class Product(Base):
    __tablename__ = 'product'

    pID = Column(INTEGER(11), primary_key=True)
    p_name = Column(String(50), nullable=False)
    amount = Column(INTEGER(11), nullable=False)
    price = Column(DECIMAL(18, 2), nullable=False)
    kind = Column(String(20), nullable=False)
    picture = Column(String(30))
    stID = Column(ForeignKey('store.stID', ondelete='SET NULL', onupdate='SET NULL'), index=True)

    store = relationship('Store')


class Salesperson(Base):
    __tablename__ = 'salesperson'

    saID = Column(INTEGER(11), primary_key=True)
    s_name = Column(String(20))
    email = Column(String(30))
    job = Column(String(30))
    salary = Column(DECIMAL(18, 2))
    aID = Column(ForeignKey('address.aID', ondelete='CASCADE'), index=True)
    stID = Column(ForeignKey('store.stID', ondelete='CASCADE'), index=True)

    addres = relationship('Addres')
    store = relationship('Store')


class Transact(Base):
    __tablename__ = 'transact'

    order_num = Column(INTEGER(11), primary_key=True)
    pID = Column(ForeignKey('product.pID'), nullable=False, index=True)
    saID = Column(ForeignKey('salesperson.saID'), nullable=False, index=True)
    cID = Column(ForeignKey('customer.cID'), nullable=False, index=True)
    t_date = Column(Date, nullable=False)
    quantitiy = Column(INTEGER(11), nullable=False)

    customer = relationship('Customer')
    product = relationship('Product')
    salesperson = relationship('Salesperson')
