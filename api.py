from flask import Flask, flash, json, request, redirect, Response, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import datetime
import zipstream
import os
from wtforms import Form, StringField, validators


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config.from_envvar('APP_SETTINGS')
CORS(app)


@app.route('/ping', methods=['GET'])
def ping():
    response = app.response_class(
        response='pong',
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)