from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_db_connection

app = Flask(__name__)
CORS(app) # Allows React frontend to talk to this backend

@app.route('/api/exercises', methods=['GET'])
def get_exercises():
    # getting connection from database (opens workout.db)
    connection = get_db_connection()
    # create cursor object to exceute SQL statements
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM exercise")
    exercises = cursor.fetchall()

    connection.close()

    return jsonify(exercises)

# now for post

if __name__ == '__main__':
    app.run(debug=True, port=5000)