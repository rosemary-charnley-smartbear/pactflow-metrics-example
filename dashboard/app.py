from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

DATA_DIR = os.environ.get('DATA_DIR', '/data')


def load_json(filename):
    with open(os.path.join(DATA_DIR, filename)) as f:
        return json.load(f)


@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')


@app.route('/api/latest')
def latest():
    return jsonify(load_json('pactflow_metrics_latest.json'))


@app.route('/api/history')
def history():
    return jsonify(load_json('pactflow_metrics_history.json'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
