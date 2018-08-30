from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from wtforms import ValidationError
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        print('\n check_password : ' + password)
        chk_val = check_password_hash(self.password_hash,password)
        return chk_val

class Stock(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True, index=True)
    code = db.Column(db.String(16))
    fair_price = db.Column(db.Float)
    target_price = db.Column(db.Float)
    market_price = db.Column(db.Float)
    gain = db.Column(db.Float)
    txn_price = db.Column(db.Float)
    quantity = db.Column(db.Integer)



    def __init__(self, name, code, fair_price, target_price,market_price,gain=0.0,txn_price=0.0,quantity=0):
        self.name = name
        self.code = code
        self.fair_price = fair_price
        self.target_price = target_price
        self.market_price = market_price
        self.gain = gain
        self.txn_price = txn_price
        self.quantity = quantity
