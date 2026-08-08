from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Allows your React frontend to talk to this backend

@app.route('/api/test', methods=['GET'])
def test_connection():
    return jsonify({"message": "Backend is locked in and ready!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)