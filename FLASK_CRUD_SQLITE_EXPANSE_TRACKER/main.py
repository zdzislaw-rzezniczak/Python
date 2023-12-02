import json
import sqlite3
from flask import g, Flask, render_template, request, flash, redirect, url_for, abort

DATABASE = 'database.db'

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fduysiilfjsigyeowe246ulfd'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def connect_execute_db(sql_command):
    db = get_db()
    db.row_factory = lambda C, R: {c[0]: R[i] for i, c in enumerate(C.description)}
    sql_command = sql_command
    cur = db.execute(sql_command)
    res = cur.fetchall()
    return res


def get_expense(exense_id):
    db = get_db()
    db.row_factory = lambda C, R: {c[0]: R[i] for i, c in enumerate(C.description)}
    expense = db.execute('SELECT * FROM expenses WHERE id = ?',
                         (exense_id,)).fetchone()
    if expense is None:
        abort(404)
    return expense


@app.route('/')
def index():
    sql_stmt = 'select * from expenses'
    expenses = connect_execute_db(sql_stmt)
    return render_template('index.html', expenses=expenses)


@app.route('/create/', methods=('GET', 'POST'))
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
            db = get_db()
            db.execute('INSERT INTO expenses (category, total, description) VALUES (?, ?, ?)',
                       (category, total, description))
            db.commit()
            return redirect(url_for('index'))

    return render_template('create.html')


# ...

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    expense = get_expense(id)

    if request.method == 'POST':
        category = request.form['category']
        total = request.form['total']
        description = request.form['description']

        if not category:
            flash('Title is required!')

        elif not total:
            flash('Total is required!')

        else:
            db = get_db()
            db.execute('UPDATE expenses SET category = ?, total = ?, description = ?'
                       ' WHERE id = ?',
                       (category, total, description, id))
            db.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', expense=expense)


@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    expense = get_expense(id)
    db = get_db()
    db.execute('DELETE FROM expenses WHERE id = ?', (id,))
    db.commit()
    flash('"{}" was successfully deleted!'.format(expense['description']))
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
