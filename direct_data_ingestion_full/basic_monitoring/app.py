from flask import Flask, render_template, request, jsonify
import json
import threading

app = Flask(__name__)

# Shared data structure for thread-safe updates
data_ingestion_info = {
    "total_insertions": 0,
    "last_update": "Not yet started"
}
data_lock = threading.Lock()

@app.route('/')
def home():
    with data_lock:
        return render_template('index.html', data_ingestion_info=data_ingestion_info)

@app.route('/update_metrics', methods=['POST'])
def update_metrics():
    global data_ingestion_info
    with data_lock:
        update_data = request.json
        data_ingestion_info['total_insertions'] += update_data['insertions']
        data_ingestion_info['last_update'] = update_data['last_update']
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
