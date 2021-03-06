from myproject import app,db
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user
from myproject.models import User, Stock
from myproject.forms import LoginForm, RegistrationForm, StockForm, EditStockForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import ValidationError
from flask_table import Table, Col, LinkCol
from myproject.tables import Results, ResultsEdit, ResultsDelete

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    error = None
    if form.validate_on_submit():
        print('validate_on_submit ')
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()
        print('User ' )
        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not
        if user is None:
            #raise ValidationError('Your email is not registered')
            flash('Your email is not registered')

        if  user is not None and  user.check_password(form.password.data) :
            #Log in the user

            login_user(user)

            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')

            return redirect(next)
        else :
            # password mismatch
            flash('Your email id and or password is not matching.')
            error = 'Invalid credentials'

    return render_template('login.html', form=form, error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error_state = False
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)


        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/stocks')
@login_required
def stocks():
    #form = StockForm()

    '''form.validate_on_submit():
        return redirect(url_for('stocks'))
        '''
    stocks = Stock.query.all()
    table = Results(stocks)
    table.border = True


    #return render_template('stocks.html', form=form)
    return render_template('stocks.html', table=table)


@app.route('/add',methods=['GET', 'POST'])
@login_required
def add():
    form = StockForm()
    if form.validate_on_submit():
        stock = Stock(name=form.name.data,
                    code=form.code.data,
                    fair_price=form.fair_price.data)


        db.session.add(stock)
        db.session.commit()
        flash('Stock "' + stock.name + '" is added!')
        return redirect(url_for('stocks'))
    return render_template('add.html', form=form)

@app.route('/edit',methods=['GET', 'POST'])
@login_required
def edit_stock():

    stocks = Stock.query.all()
    table = ResultsEdit(stocks)
    table.border = True


    return render_template('edit.html', table=table)


@app.route('/item/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):

    stock = Stock.query.filter_by(id=id).first()
    if stock:
        #form = EditStockForm(formdata=request.form, obj=stock)
        form = EditStockForm(formdata=request.form)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(stock, form,new=False)
            flash('Stock updated successfully!')
            return redirect(url_for('stocks'))
        return render_template('edit_stock.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


def save_changes(stock_prev, form, new=False):
    """
    Save the changes to the database
    """


    onldname = stock_prev.name
    oldstock = Stock.query.filter_by(name=onldname).first()
    oldstock.name = form.name.data
    oldstock.code = form.code.data
    oldstock.fair_price = form.fair_price.data
    db.session.commit()


@app.route('/delete',methods=['GET', 'POST'])
@login_required
def delete_stock():

    stocks = Stock.query.all()
    table = ResultsDelete(stocks)
    table.border = True

    return render_template('delete.html', table=table)


@app.route('/item/<string:name>', methods=['GET', 'POST'])
@login_required
def delete(name):

    stock = Stock.query.filter_by(name=name).first()

    if stock:
        db.session.delete(stock)
        db.session.commit()
        flash('Stock "'  + name + '" is deleted!')
        return redirect(url_for('stocks'))

    else:
        return 'Error loading #{id}'.format(id=id)




if __name__ == '__main__':
    app.run(debug=True)
