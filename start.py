#!/usr/bin/env python3
""" Testing flask and js-grid """

from flask import *
import json

app = Flask('jsgrid-playground', template_folder='.')

# The simplest of databases :)
def load_data():
    return json.load(open('clients.json'))

def write_data(data):
    json.dump(data, open('clients.json', 'w'), indent=4, sort_keys=True)
    return


@app.route('/api/database', methods=['GET',])
def getdata():
    return jsonify(load_data())


@app.route('/api/database', methods=['PUT',])
def updatedata():
    data = load_data()
    for i in range(len(data)):
        if data[i].get('id') == request.json['id']:
            data[i].update(request.json)
    write_data(data)
    return jsonify(request.json)


@app.route('/api/database', methods=['POST',])
def insertdata():
    data = load_data()
    newdata = request.json
    newdata['id'] = len(data) + 1
    data.append(newdata)
    write_data(data)
    return jsonify(newdata)

@app.route('/api/database', methods=['DELETE',])
def deletedata():
    data = load_data()
    out = []
    for i in range(len(data)):
        if data[i].get('id') != int(request.form.get('id')):
            out.append(data[i])
    write_data(out)
    return jsonify(success=True)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
