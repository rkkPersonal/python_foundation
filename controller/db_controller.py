#  -*-coding:utf8 -*-
from flask import render_template, Flask, jsonify, json, Response
import mysql.connector

import logging.config
import yaml

app = Flask(__name__)

with open('../config.yaml', 'r', encoding='gbk') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("main")


@app.errorhandler(404)
def page_not_not_found(error):
    return render_template('404.html'), 404


@app.route('/query/<path:id>', methods=["GET", "POST"])
def hello_flask(id):
    conn = mysql.connector.connect(host='192.168.43.200', port='3306', user='root', password='12345678',
                                   database='study')
    try:
        cursor = conn.cursor()
        cursor.execute('select * from game where id = %s', ('1',))
        values = cursor.fetchall()
        # print(values)
        logger.info(values)
        conn.commit()

    except:

        conn.rollback()

    finally:
        cursor.close()
        conn.close()
        pass

    return jsonify(values)


@app.route('/test/json', methods=["GET"])
def testJson():
    conn = mysql.connector.connect(host='192.168.43.200', port='3306', user='root', password='12345678',
                                   database='study')
    cursor = conn.cursor()
    try:
        cursor.execute('select * from game where id = %s', ('1',))
        values = cursor.fetchall()

    finally:
        cursor.close()
        conn.close()
        pass

    return Response(json.dumps(values), mimetype='application/json')


@app.route('/obj')
def customizeValue():
    data = {
        'id': 1,
        'username': 2,
        'IDCard': [3, 4, 5]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.config['JSON_AS_ASCII'] = False
    app.run(host='127.0.0.1', port=5000)
