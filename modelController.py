from sqlalchemy.sql import exists
from db import sessionDB
from models import *
import simplejson as json
import collections
from flask import jsonify



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


if __name__ == '__main__':
    print(searchKind('clothes'))

# print(type(product[0])) # <class 'models.Product'>
