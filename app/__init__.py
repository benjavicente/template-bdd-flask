from flask import Flask, render_template

from .utils import get_cursor

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/hi/<name>')
def hello_name(name):
    return render_template('hello.html', name=name)

@app.route("/database")
def database():
    cursor = get_cursor()
    cursor.execute("SELECT * FROM sample_table")
    rows = cursor.fetchall()
    return render_template('database.html', rows=rows)
