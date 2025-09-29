# Flask Server (Web API Serving)

# Flask - Flask is a micro web framework written in Python. It is classified as a micro framework

from flask import Flask, jsonify, send_from_directory
import pandas as pd
from analysis import compute_summary, load_students

app = Flask(__name__, static_folder='static')
DATA_PATH = 'data/students.csv'

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/students')
def api_students():
    df = load_students(DATA_PATH)
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/summary')
def api_summary():
    df = load_students(DATA_PATH)
    summary = compute_summary(df)
    return jsonify(summary)

@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)