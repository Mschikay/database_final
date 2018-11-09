from flask import Flask
app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="shiliwanglitangziqigreeneatprojectfordatabasemanagement",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "greeneat"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Tangziqi1996@localhost/greeneat?host=localhost?port=3306'