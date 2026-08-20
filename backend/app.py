from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_db_connection

app = Flask(__name__)
CORS(app) # Allows React frontend to talk to this backend


# get
@app.route('/api/exercises', methods=['GET'])
def get_exercises():
    # getting connection from database (opens workout.db)
    connection = get_db_connection()
    # create cursor object to exceute SQL statements
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM exercise")
    exercises = [dict(row) for row in cursor.fetchall()]

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


# now for put
@app.route('/api/exercises/<id>', methods=['PUT'])
def update_exercise(id):

    # create data variable for reading json using our imported request
    data = request.get_json()

    # read name and muscle_group from data
    name = data["name"]
    muscle_group = data["muscle_group"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE exercise
    SET name = ?, muscle_group = ?
    WHERE id = ?
    """, (name, muscle_group, id))

    # commit and close
    connection.commit()
    connection.close()
    
    # 200 = successful update
    return jsonify(data), 200

# now for delete
@app.route('/api/exercises/<id>', methods=['DELETE'])
def delete_exercise(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM exercise WHERE id = ?;
    """, (id,))

    # commit and close
    connection.commit()
    connection.close()
    
    # 200 = successful delete
    return jsonify({"message": "Exercise deleted successfully"}), 200


# get but for workout_session
@app.route('/api/workout_sessions', methods=['GET'])
def get_workout_sessions():
    # getting connection from database (opens workout.db)
    connection = get_db_connection()
    # create cursor object to exceute SQL statements
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM workout_session")
    workout_sessions = [dict(row) for row in cursor.fetchall()]

    # close
    connection.close()

    return jsonify(workout_sessions)

# post but for workout_session
@app.route('/api/workout_sessions', methods=['POST'])
def send_workout_esssion():

    # create data variable for reading json using our imported request
    data = request.get_json()

    # read date from data
    date = data["date"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO workout_session (date)
        VALUES (?)
    """, (date,))

    # commit and close
    connection.commit()
    connection.close()

    # we add 201 because new resource created using status code 201
    return jsonify(data), 201

# WORK NOTES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# put but for workout_session
@app.route('/api/workout_sessions/<id>', methods=['PUT'])
def update_workout_session(id):

    # create data variable for reading json using our imported request
    data = request.get_json()

    # read date from data
    date = data["date"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE workout_session
    SET date = ?
    WHERE id = ?
    """, (date, id))

    # commit and close
    connection.commit()
    connection.close()
    
    # 200 = successful update
    return jsonify(data), 200

# WORK CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# delete but for workout_session
@app.route('/api/workout_sessions/<id>', methods=['DELETE'])
def delete_workout_session(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM workout_session WHERE id = ?;
    """, (id,))

    # commit and close
    connection.commit()
    connection.close()
    
    # 200 = successful delete
    return jsonify({"message": "Workout session deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
