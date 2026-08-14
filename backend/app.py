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

    # close
    connection.close()

    return jsonify(exercises)

# now for post
@app.route('/api/exercises', methods=['POST'])
def send_exercises():

    # create data variable for reading json using our imported request
    data = request.get_json()

    # read name and muscle_group from data
    name = data["name"]
    muscle_group = data["muscle_group"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO exercise (name, muscle_group)
        VALUES (?, ?)
    """, (name, muscle_group))

    # commit and close
    connection.commit()
    connection.close()

    # we add 201 because new resource created using status code 201
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True, port=5000)