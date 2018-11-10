from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired


class loginForm(FlaskForm):
    userEmail = StringField('inputEmail', [validators.Length(min=4, max=25)])
    userPwd = StringField('inputPassword', [validators.Length(min=4, max=16)])
    buttonLogin = SubmitField('buttonLogin')


class selectForm(FlaskForm):
    selectRecord = StringField('selectRecord')
    buttonSearch = SubmitField('buttonSearch')
    checkboxRegion = BooleanField('checkBoxRegion', validators=[DataRequired(), ])
    checkboxProductName = BooleanField('checkBoxProductName', validators=[DataRequired(), ])
    checkboxStoreName = BooleanField('checkBoxStoreName', validators=[DataRequired(), ])
