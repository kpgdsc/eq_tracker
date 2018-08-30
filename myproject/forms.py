from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from myproject.models import User, Stock


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is already taken!')

class StockForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    code = StringField('Code', validators=[DataRequired()])
    fair_price = FloatField('Fair Price',  validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_name(self, field):
        # Check if not None for that user email!
        if Stock.query.filter_by(name=field.data).first():
            raise ValidationError('Stock is already present!')

    def validate_code(self, field):
        # Check if not None for that user email!
        if Stock.query.filter_by(code=field.data).first():
            raise ValidationError('Stock is already present!')

class EditStockForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    code = StringField('Code', validators=[DataRequired()])
    fair_price = FloatField('Fair Price',  validators=[DataRequired()])
    submit = SubmitField('Update')


    def validate_name(self, field):
        # Check if not None for that user email!
        if Stock.query.filter_by(name=field.data).first():
            raise ValidationError('Stock is already present!')

    def validate_code(self, field):
        # Check if not None for that user email!
        if Stock.query.filter_by(code=field.data).first():
            raise ValidationError('Stock is already present!')
