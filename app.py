from flask import render_template, Flask, session, redirect, url_for, escape, request, flash

from config import app


app = app


# MAIN PAGE
@app.route('/', methods=['GET', 'POST'])
def main_page():
    session['user'] = ''
    session['status'] = ''
    loginout = "login"
    error = None
    flashMsg = ''

    if request.method == 'POST':
        whichPost = request.form.get('post')
        app.logger.debug(whichPost)

        # login
        if whichPost == 'logInOut':
            app.logger.debug('waiting for data')

            userEmail = request.form['userEmail']
            userPwd = request.form['userPwd']

            print(userEmail, userPwd)
            if userEmail == 'yiweiyh@163.com' and userPwd == '123':
                session['user'] = userEmail
                session['status'] = 'login succeed'
                session['name'] = "Hannah"
                app.logger.info('got it')
                return redirect(url_for('isLogin', name=session['name']), 302)

        else:
            flash('please login')
            # return redirect(url_for('index'), 302)
            return render_template('index.html')

    return render_template('shop-homepage.html', loginout=loginout)


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


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

        # search, select sql
        if whichPost == 'logInOut':
            '''doing log out.'''
            flash('you have logged out.')

        elif whichPost == 'search':
            if session['user']:
                app.logger.debug(request.form.get('selectRecord'))
                app.logger.debug(request.form.get('buttonSearch'))
                app.logger.debug(request.form.get('checkBoxRegion'))
                app.logger.debug(request.form.get('checkBoxProductName'))
                app.logger.debug(request.form.get('checkBoxStoreName'))

                return request.form.get('selectRecord')

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
        pass

    return render_template('shop-homepage.html', hello=hello, name=name, loginout='log out')


if __name__ == '__main__':
    app.debug = True
    app.run()
