from sqlalchemy.sql import exists
from db import sessionDB
from models import *
from flask import jsonify
from decimal import Decimal


class Error(Exception):
    pass

def search(selectRecord):
    result = []
    # need to query by address
    idx = selectRecord.rfind(' in ')  # search the last ' in '
    if idx != -1:
        productName = selectRecord[0:idx].strip()
        address = selectRecord[idx + 4:-1].strip()
        aID = []
        stID = []

        address = sessionDB.query(Addres).filter(Addres.street.like('%'+address+'%'))
        if len(address.all()) < 1:
            return None
        for a in address:
            aID.append(a.aID)

        store = sessionDB.query(Store).filter(Store.aID.in_(aID))
        if len(store.all()) < 1:
            return None
        for s in store:
            stID.append(s.stID)

        product = sessionDB.query(Product).filter(Product.stID.in_(stID)).\
            filter(Product.p_name.like('%'+productName+'%')).limit(50)
        if len(product.all()) < 1:
            return None
        for p in product:
            result.append(p.to_json())
        return jsonify(result)

    else:
        productName = selectRecord.strip()
        product = sessionDB.query(Product).filter(Product.p_name.like('%'+productName+'%')).limit(50)
        if (len(product.all())) < 1:
            return None     # no such product

        for p in product:
            result.append(p.to_json())
        return jsonify(result)


def searchKind(kind):
    result = []
    product = sessionDB.query(Product).filter(Product.kind.like('%' + kind + '%')).limit(50)

    if (len(product.all())) < 1:
        return None  # no such product

    for p in product:
        result.append(p.to_json())

    return jsonify(result)


def placeOrder(pName, pid, amount, quantity, price, cID):
    try:
        assert len(pid) == len(amount) and len(pid) == len(price) and len(pid) == len(quantity) and len(pid) != 0

        #get user's remain money
        customer = sessionDB.query(Customer).filter_by(cID=cID).first()
        kind = customer.kind
        if kind == 'individual':
            remain = sessionDB.query(HomeCu).filter_by(cID=cID).first().remain
            model = HomeCu
        else:
            remain = sessionDB.query(BusinessCu).filter_by(cID=cID).first().remain
            model = BusinessCu
        if remain <= 0:
            raise Exception('Cannot find enough remain')

        for i in range(len(pid)):
            _pid = pid[i]
            _amount = int(amount[i])
            _quantity = int(quantity[i])
            _price = Decimal(price[i])
            _pName = pName[i]
            if _quantity > _amount or _quantity*_price > remain:
                raise Exception('No enough storage for '+_pName)
            else:
                remain = remain - _quantity*_price
                _amount = _amount - _quantity
                sessionDB.query(Product).filter(Product.pID == _pid).update({'amount': _amount})
                sessionDB.query(model).filter(model.cID == cID).update({'remain': remain})
                # save this new order
                record = OrderList(cID=cID, pID=_pid, quantity=_quantity, price=_price)
                sessionDB.add(record)
        sessionDB.commit()

    except Exception as e:
        # on rollback, the same closure of state
        # as that of commit proceeds.
        sessionDB.rollback()
        print(e.args)
        raise
    finally:
        sessionDB.close()


def registerIndividual(street, city, zip_code, email, password, first_name, last_name, age, remain, marriage):
    try:
        sessionDB.autocommit = False
        # insert Address
        addrRecord = Addres(street=street, city=city, zip_code=zip_code)

        # insert customer
        cRecord = Customer(email=email, passwords=password, kind='individual')
        cRecord.addres = addrRecord
        homeCRecord = HomeCu(fname=first_name, lname=last_name, age=age, marriage=marriage, remain=remain)
        homeCRecord.customer = cRecord

        sessionDB.add_all([addrRecord, cRecord, homeCRecord])
        sessionDB.commit()

    except Error as e:
        print(e)
        sessionDB.rollback()
        raise
    finally:
        sessionDB.close()


def registerBusiness(street, city, zip_code, email, password, name, remain, category):
    try:
        sessionDB.autocommit = False
        # insert Address
        addrRecord = Addres(street=street, city=city, zip_code=zip_code)

        # insert customer
        cRecord = Customer(email=email, passwords=password, kind='business', aID=addrRecord.aID)
        cRecord.addres = addrRecord

        # insert customer
        bCRecord = BusinessCu(cID=cRecord.cID, b_name=name, remain=remain, category=category)
        bCRecord.customer = cRecord

        sessionDB.add_all([addrRecord, cRecord, bCRecord])
        sessionDB.commit()

    except Error as e:
        print(e)
        sessionDB.rollback()
        raise
    finally:
        sessionDB.close()


if __name__ == '__main__':
    # registerIndividual('534 Henry St', 'New York', '38110', 'user1@qq.com', '123', 'Fanny', 'Cumber', 333, 82394.23, 1)
    registerBusiness('9898 Rail St', 'Chicago', '84578', 'user1@org.com', '123', 'user1', 9120, 'beverage')
# print(type(product[0])) # <class 'models.Product'>
