from flask import render_template, Flask, session, redirect, url_for, escape, request, flash, jsonify, json, Response
from flask_cors import CORS, cross_origin
from config import app
from sqlalchemy.sql import exists
from db import sessionDB
from models import *
import modelController as mc

app = app
CORS(app, support_credentials=True)


# MAIN PAGE
@cross_origin(origin='*')
@app.route('/', methods=['GET', 'POST'])
def main_page():
    session['user'] = ''
    session['status'] = ''
    loginout = "login"
    error = None
    flashMsg = ''

    if request.method == 'POST':
        req = request.get_data()
        # mistakenly hit 'Place order'
        if len(req) <= 13:
            return render_template('shop-homepage.html', loginout=loginout)
        else:
            whichPost = json.loads(req)
        # login
        if whichPost['post'] == 'logInOut':
            # get email and password from html
            userEmail = whichPost['userEmail']
            userPwd = whichPost['userPwd']
            result = mc.login(userEmail, userPwd)
            response = Response(
                response=json.dumps(result),
                status=200,
                mimetype='json'
            )
            if result['status'] == 'succeed':
                session['fisrtName'] = result['fname']
                session['lastName'] = result['lname']
                session['email'] = result['email']
                session['cID'] = result['cID']
                url = url_for('isLogin', name=session['fisrtName'], cID=session['cID'])
                return Response(response=json.dumps({'redirect': url}), status=200, mimetype='json')
            else:
                return response
        else:
            return render_template('shop-homepage.html', loginout=loginout)

     # display by kind
    if request.method == 'GET':
        whichCategory = request.args.get('kind', '')
        app.logger.debug(whichCategory)
        if whichCategory:
            # get the result
            data = mc.searchKind(whichCategory)
            if data:
                return data

        # search, select sql
        search = request.args.get('search', '')
        app.logger.debug(search)
        if search:
            data = mc.search(search)
            app.logger.debug(data)
            if data:
                return data

        [src1, src2, src3], [n1, n2, n3] = mc.mostPopular()
        return render_template('shop-homepage.html', loginout='log in',
                               mostPopular1=src1, mostPopular2=src2, mostPopular3=src3,
                               n1=n1, n2=n2, n3=n3, display='none')


# REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def register():
        if request.method == 'GET':
            return render_template('register.html', hint='')

        if request.method == 'POST':
            print('waiting for data')
            radio_value = request.form.get('AdPrintMode')

            # individual
            if radio_value == '1':
                # get individual information
                first_name = request.form.get('first_name', None)
                last_name = request.form.get('last_name', None)
                email = request.form.get('Iemail', None)
                password = request.form.get('Ipassword', None)
                zip_code = request.form.get('Izip_code', None)
                street = request.form.get('Istreet', None)
                city = request.form.get('Icity', None)
                age = request.form.get('age', None)
                remain = request.form.get('annu_income', None)
                status = request.form.get('subject', None)
                marriage = None
                if status == 'Single':
                    marriage = 0
                if status == 'Married':
                    marriage = 1

                result = mc.registerIndividual(street, city, zip_code, email, password,
                                               first_name, last_name, age, remain, marriage)
                print(result)
                if result == 'succeed':
                    return redirect(url_for('main_page'))
                else:
                    return render_template('register.html', hint=result)

            # business
            if radio_value == '2':
                # get individual information
                name = request.form.get('name', None)
                email = request.form.get('Bemail', None)
                password = request.form.get('Bpassword', None)
                zip_code = request.form.get('Bzip_code', None)
                street = request.form.get('Bstreet', None)
                city = request.form.get('Bcity', None)
                remain = request.form.get('bus_income', 1)
                category = request.form.get('subject', "default")

                result = mc.registerBusiness(street, city, zip_code, email,
                                             password, name, remain, category)
                print(result)
                if result == 'succeed':
                    return render_template(url_for('main_page'))
                else:
                    return render_template('register.html', hint=result)


# PAGE LOADED AFTER LOGIN
@app.route('/<name>_<cID>/', methods=['GET', 'POST'])
def isLogin(name, cID):
    hello = "Hello, "

    if request.method == 'POST':
        whichPost = request.form.get('post')
        # log out
        if whichPost == 'logInOut':
            '''doing log out.'''
            flash('you have logged out.')

        # place order
        elif whichPost == "checkout":
            pID = request.form.getlist('pID')
            amount = request.form.getlist('amount')
            price = request.form.getlist('price')
            quantity = request.form.getlist('quantity')
            pName = request.form.getlist('pName')
            print(pID, amount, price, quantity, pName)
            cID = session['cID']
            mc.placeOrder(pName, pID, amount, quantity, price, cID)
            return 'ok'

        # unknown request
        else:
            return 'Unknown Error'

    # display by kind
    if request.method == 'GET':
        whichCategory = request.args.get('kind', '')
        app.logger.debug(whichCategory)
        if whichCategory:
            # get the result
            data = mc.searchKind(whichCategory)
            if data:
                return data

        # search, select sql
        search = request.args.get('search', '')
        app.logger.debug(search)
        if search:
            data = mc.search(search)
            app.logger.debug(data)
            if data:
                return data

        [src1, src2, src3], [n1, n2, n3] = mc.mostPopular()
        return render_template('shop-homepage.html', hello=hello, name=name, loginout='log out', cID=cID,
                               mostPopular1=src1, mostPopular2=src2, mostPopular3=src3,
                               n1=n1, n2=n2, n3=n3, display='block')


@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'GET':
        cID = ''
        ord = sessionDB.query(OrderList.ID, OrderList.pID, Product.p_name,
                              OrderList.quantity, OrderList.price, OrderList.placetime)\
            .join(Product, Product.pID == OrderList.pID).filter(OrderList.cID == cID).all()
        return render_template('review.html', ord=ord)


if __name__ == '__main__':
    app.debug = True
    app.run()
