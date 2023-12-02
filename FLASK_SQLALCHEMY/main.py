from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, session, flash
import re
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, insert


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'fduysiilfjsigyeowe246ulfd'


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect('/login',code=302)
        return f(*args, **kwargs)
    return decorated_function
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime, default=func.now())
    category = db.Column(db.String(50))
    total = db.Column(db.Float)
    description = db.Column(db.String(50))

    def __repr__(self):
        return f"Expense created: {self.created}, category: {self.category}, total: {self.total}, description: {self.description}."


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))


# @app.route("/")
# def index():
#     db.create_all()
#
#     # e1 = Expense(category="zywnosc", total=124.55, description="Dino")
#     # e2 = Expense(category="paliwo", total=230, description="Petropol")
#     # e3 = Expense(category="ubrania", total=300.25, description="C&A")
#     # e4 = Expense(category="ubrania", total=100.25, description="CCC")
#     # db.session.add(e1)
#     # db.session.add(e2)
#     # db.session.add(e3)
#     # db.session.add(e4)
#     # db.session.commit()
#
#     expenses = Expense.query.all()
#     print(expenses)
#     ret = ''
#     for e in expenses:
#         ret += str(e) + '<br>'
#
#     return ret

@app.route('/', methods=('GET', 'POST'))

@login_required
def index():
    # db.create_all()
    #


    if request.method == 'POST':
        date = request.form['created_search']
        category = request.form['category_search']
        total = request.form['total_search']
        description = request.form['description_search']

        expenses = Expense.query.filter(Expense.category.like(f'%{category}%')).filter(Expense.created.like(f'%{date}%')).filter(Expense.total.like(f'%{total}%')).filter(Expense.description.like(f'%{description}%')).all()
        sum_expenses = 0
        for expense in expenses:
            sum_expenses += expense.total
        return render_template('index.html', expenses=expenses, suma=sum_expenses, category=category, date=date, total=total, description=description)

    else:
        expenses = Expense.query.all()
        sum_expenses = 0
        for expense in expenses:
            sum_expenses  += expense.total
        return render_template('index.html', expenses=expenses, suma=sum_expenses)

@app.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        category = request.form['category']
        total = request.form['total']
        description = request.form['description']

        if not category:
            flash('Category is required!')
        elif not total:
            flash('Total is required!')
        else:

            e1 = Expense(category=category, total=total, description=description)
            db.session.add(e1)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    expense = db.session.query(Expense).filter(Expense.id == id).first()
    if request.method == 'POST':
        category = request.form['category']
        total = request.form['total']
        description = request.form['description']

        if not category:
            flash('Title is required!')

        elif not total:
            flash('Total is required!')

        else:

            expense.category = category
            expense.total = total
            expense.description = description
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', expense=expense)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    expense = db.session.query(Expense).filter(Expense.id == id).first()

    db.session.delete(expense)
    db.session.commit()
    flash('"{}" was successfully deleted!'.format(expense.description))
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        account = db.session.query(Account).filter(Account.username == username).filter(Account.password == password).first()
        if account:
            session['loggedin'] = True
            session['id'] = account.id
            session['username'] = account.username
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        account = db.session.query(Account).filter(Account.username == username).first()
        # db.session.execute(account)
        # db.session.commit()

        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            stmt = (
                insert(Account).
                values(username=username, password=password, email=email)
            )
            db.session.execute(stmt)
            db.session.commit()

            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
