from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('intro.html')


@app.route('/simple-table')
def simple_table():
    return render_template('simple-table.html')