from flask import render_template, Flask, session, redirect, url_for, escape, request, flash
from flask_wtf.csrf import CSRFProtect

from config import app
from view import loginForm, selectForm

#
# def is_submitted(self):
#     """
#     Checks if form has been submitted. The default case is if the HTTP
#     method is **PUT** or **POST**.
#     """
#
#     return self.request and self.request.method in ("PUT", "POST")
#
#
# def validate_on_submit(self):
#     """
#     Checks if form has been submitted and if so runs validate. This is
#     a shortcut, equivalent to ``form.is_submitted() and form.validate()``
#     """
#     return self.is_submitted() and self.validate()


@property
def data(self):
    return dict((name, f.data) for name, f in self._fields)


app = app
# csrf = CSRFProtect()
# csrf.init_app(app)


# @csrf.exempt

@app.route('/', methods=['GET', 'POST'])
def main_page():
    session['user'] = ''
    session['status'] = ''
    loginform = loginForm()
    selectform = selectForm()
    error = None
    flashMsg = ''

    if request.method == 'POST':
        app.logger.debug(loginform.validate_on_submit())
        app.logger.debug(loginform.buttonLogin.data)

        app.logger.debug(selectform.validate_on_submit())
        app.logger.debug(selectform.selectRecord.data)
        flash(loginform.errors)
        flash(selectform.errors)

        # if loginform.buttonLogin.data and loginform.validate_on_submit():
        #     app.logger.debug('waiting for data')
        #
        #     userEmail = request.form['userEmail']
        #     userPwd = request.form['userPwd']
        #     print(userEmail, userPwd)
        #     if userEmail == 'yiweiyh@163.com' and userPwd == '123':
        #         session['user'] = userEmail
        #         session['status'] = 'login succeed'
        #         session['name'] = "Hannah"
        #         app.logger.info('got it')
        #         return redirect(url_for('login', name=session['name']), 302)
        #
        # elif selectform.buttonSearch.data and selectform.validate_on_submit():
        #     return "search page"
        return "hi"
    return render_template('shop-homepage.html')


@app.route('/<name>')
def login(name):
    hello = "hello, "
    return render_template('shop-homepage.html', hello=hello, name=name)


if __name__ == '__main__':
    app.debug = True
    app.run()
