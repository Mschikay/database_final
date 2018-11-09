from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired


class loginForm(FlaskForm):
    userEmail = StringField('Email:', [validators.Length(min=4, max=25)])
    userPwd = StringField('Password:', [validators.Length(min=4, max=16)])
    buttonLogin = SubmitField('Login:')


class selectForm(FlaskForm):
    selectRecord = StringField('SelectRecord:')
    buttonSearch = SubmitField('Search:')
    checkbox = BooleanField('Region:', validators=[DataRequired(), ])
    checkbox = BooleanField('ProductName:', validators=[DataRequired(), ])
    checkbox = BooleanField('StoreName:', validators=[DataRequired(), ])
