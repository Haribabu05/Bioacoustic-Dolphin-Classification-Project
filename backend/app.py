from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/api/cves', methods=['GET'])
def get_cves():
    # Sample static data for testing
    data = [
        {"cve_id": "CVE-2024-1234", "description": "Buffer overflow in X", "severity": 9.8, "predicted_severity": "High"},
        {"cve_id": "CVE-2024-2345", "description": "SQL Injection", "severity": 7.5, "predicted_severity": "High"},
        {"cve_id": "CVE-2024-3456", "description": "XSS vulnerability", "severity": 4.3, "predicted_severity": "Low"},
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
