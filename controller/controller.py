#  -*-coding:utf8 -*-
from flask import render_template, Flask
from demo import big_decimal

app = Flask(__name__)


@app.route('/')
def hello_flask():
    return "<h1>hello, Flask!</h1>"


@app.route("/hi")
def hi():
    big_decimal.hello()
    big_decimal.process()

    return render_template("hello.html", name="Kitty", age="22")



if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
