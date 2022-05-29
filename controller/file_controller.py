#  -*-coding:utf8 -*-

import logging.config
import os

import yaml
from flask import Flask, json, Response, request, render_template
from werkzeug.utils import secure_filename

from service import file_service
from studyutil import base_result

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '../'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

with open('../config.yaml', 'r', encoding='gbk') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("main")


@app.route('/upload')
def upload_index_page():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print(request.files)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))

        return 'file uploaded successfully'

    else:

        return render_template('upload.html')


@app.route('/read_file', methods=["GET"])
def readFile():
    file = file_service.read_file()
    data = base_result.result(file)
    return Response(json.dumps(data))


@app.route('/write_file', methods=["GET"])
def writeFile():
    file_service.write_file()
    data = base_result.data_response()
    return Response(json.dumps(data))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.debug = True
    app.config['JSON_AS_ASCII'] = False
    app.run(host='127.0.0.1', port=5000)
