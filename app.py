from flask import render_template, Flask, session, redirect, url_for, escape, request, flash, jsonify, json
from flask_cors import CORS, cross_origin
from config import app
from sqlalchemy.sql import exists
from db import sessionDB
from models import *
import modelController as mc

app = app
CORS(app, support_credentials=True)


# MAIN PAGE
@app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def main_page():
    session['user'] = ''
    session['status'] = ''
    loginout = "login"
    error = None
    flashMsg = ''

    if request.method == 'POST':
        whichPost = request.form.get('post')

        # login
        if whichPost == 'logInOut':
            # get email and password from html
            userEmail = request.form.get('userEmail')
            userPwd = request.form.get('userPwd')

            emailExist=sessionDB.query(exists().where(Customer.email == userEmail)).scalar()
            if emailExist:
                records = sessionDB.query(Customer).filter(Customer.email == userEmail)
                session['pwd'] = ''
                r = None
                for record in records:
                    r = record
                if r.passwords == userPwd:
                    session['pwd'] = r.passwords
                    session['user'] = r.email
                    session['status'] = 'login succeed'
                    session['cID'] = r.cID

                    # get user's name
                    homeRecord = sessionDB.query(HomeCu).filter(HomeCu.cID == session['cID'])
                    first_name = ''
                    last_name = ''
                    for hr in homeRecord:
                        first_name = hr.fname
                        last_name = hr.lname
                    session['fullname'] = first_name + ' ' + last_name

                else:
                    pass
                    # wrong password
            else:
                pass
                # email not exists
            return redirect(url_for('isLogin', name=first_name), 302)

        else:
            app.logger.debug('please login')
            # return redirect(url_for('index'), 302)
            return render_template('shop-homepage.html', loginout='Login')


    # display by kind
    if request.method == 'GET':
        return render_template('shop-homepage.html', loginout=loginout)


# REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


# PAGE LOADED AFTER LOGIN
@app.route('/<name>', methods=['GET', 'POST'])
def isLogin(name):
    hello = "Hello, "

    if request.method == 'POST':
        whichPost = request.form['post']

        # log out
        if whichPost == 'logInOut':
            '''doing log out.'''
            flash('you have logged out.')

        # search, select sql
        elif whichPost == 'search':
            selectRecord = request.form.get('selectRecord', None)
            result = mc.search(selectRecord)
            print(result)

            if not result:
                # turn to json
                data = jsonify(productName='llogin')
                return data

        # add to shopping cart
        elif whichPost == "addToCart":
            pass

        # remove items to cart
        elif whichPost == 'removeFromCart':
            pass

        # unknown request
        else:
            return 'Unknown Error'

    # display by kind
    if request.method == 'GET':
        if request.args.get('kind'):
            app.logger.debug(request.args.get('kind'))
            whichCategory = request.args.get('category', '')

            # get the result
            result = mc.searchKind(whichCategory)
            if not result:
                print(result)

            # turn to json
            data = jsonify(productName='lalala', productPrice='$'+'4.5', productDescription=request.args.get('kind'))
            # json_data = json.loads(request.get_data())
            # kind = json_data["kind"]
            return data

    return render_template('shop-homepage.html', hello=hello, name=name, loginout='log out')


if __name__ == '__main__':
    app.debug = True
    app.run()
