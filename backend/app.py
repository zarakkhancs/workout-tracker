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

# WORK CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# get but for workout_exercise
@app.route('/api/workout_exercises', methods=['GET'])
def get_workout_exercise():
    # getting connection from database (opens workout.db)
    connection = get_db_connection()
    # create cursor object to exceute SQL statements
    cursor = connection.cursor()

    # workout_exercise only stores IDs.
    # JOINs allow us to bring in related data from other tables.
    # exercise_id -> exercise.name
    # workout_session_id -> workout_session.date
    # Result:
    # id | exercise_name | workout_date

    cursor.execute("SELECT
    	workout_exercise.id,
    	exercise.name,
    	workout_session.date
	FROM workout_exercise
	JOIN exercise
    	ON workout_exercise.exercise_id = exercise.id
	JOIN workout_session
    ON workout_exercise.workout_session_id = workout_session.id")
    workout_exercises = [dict(row) for row in cursor.fetchall()]

    # close
    connection.close()

    return jsonify(workout_exercises)

# WORK CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# post but for workout_exercise
    # workout_exercise is a junction table that links
    # an exercise to a specific workout session.
    # Example:
    # Workout Session #1 -> Bench Press	

@app.route('/api/workout_exercises', methods=['POST'])
def send_workout_exercise():

    # create data variable for reading json using our imported request
    data = request.get_json()

    # read exercise and workout session IDs from JSON payload
    exercise_id = data["exercise_id"]
    workout_session_id = data["workout_session_id"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO workout_exercise (exercise_id, workout_session_id)
        VALUES (?, ?)
    """, (exercise_id, workout_session_id))

    # commit and close
    connection.commit()
    connection.close()

    # we add 201 because new resource created using status code 201
    return jsonify(data), 201

# NOTE:
# No PUT endpoint is implemented for workout_exercise.
# If an incorrect exercise is attached to a workout session,
# the relationship can simply be deleted and recreated.
# Editing the relationship directly provides little benefit.

# WORK CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# delete but for workout_exercise
@app.route('/api/workout_exercises/<id>', methods=['DELETE'])
def delete_workout_exercise(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM workout_exercise WHERE id = ?;
    """, (id,))

    # commit and close
    connection.commit()
    connection.close()
    
    # 200 = successful delete
    return jsonify({"message": "Workout exercise deleted successfully"}), 200

# WORK CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# get but for exercise sets
@app.route('/api/exercise_sets', methods=['GET'])
def get_exercise_set():

    # open database connection
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            exercise_set.id,
            exercise.name AS exercise_name,
            workout_session.date AS workout_date,
            exercise_set.set_number,
            exercise_set.weight,
            exercise_set.reps

        FROM exercise_set

        -- exercise_set -> workout_exercise
        JOIN workout_exercise
            ON exercise_set.workout_exercise_id = workout_exercise.id

        -- workout_exercise -> exercise
        JOIN exercise
            ON workout_exercise.exercise_id = exercise.id

        -- workout_exercise -> workout_session
        JOIN workout_session
            ON workout_exercise.workout_session_id = workout_session.id
    """)

	# convert SQL rows into dictionaries
    # Example:
    # {
    # "id": 1,
    # "exercise_name": "Bench Press",
    # "workout_date": "2026-08-20",
    # "set_number": 1,
    # "weight": 135,
    # "reps": 8
    # }

    exercise_sets = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return jsonify(exercise_sets)

# WORK CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# post but for exercise_set
@app.route('/api/exercise_sets', methods=['POST'])
def send_exercise_set():

    # create data variable for reading json using our imported request
    data = request.get_json()

    # read workout_exercise_id, set_number, weight, and reps
	workout_exercise_id = data["workout_exercise_id"]
    set_number = data["set_number"]
    weight = data["weight"]
	reps = data["reps"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO exercise_set (workout_exercise_id, set_number, weight, reps)
        VALUES (?, ?, ?)
    """, (workout_exercise_id, set_number, weight, reps))

    # commit and close
    connection.commit()
    connection.close()

    # we add 201 because new resource created using status code 201
    return jsonify(data), 201


# WORK CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# put but for exercise_set
@app.route('/api/exercise_sets/<id>', methods=['PUT'])
def update_exercise_set(id):

    # create data variable for reading json using our imported request
    data = request.get_json()

    # read set_number, weight, and reps
    set_number = data["set_number"]
    weight = data["weight"]
	reps = data["reps"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE exercise_set
    SET set_number = ?, weight = ?, reps = ?
    WHERE id = ?
    """, (set_number, weight, reps, id))

    # commit and close
    connection.commit()
    connection.close()
    
    # 200 = successful update
    return jsonify(data), 200

# WORK CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# delete but for exercise_set
@app.route('/api/exercise_sets/<id>', methods=['DELETE'])
def delete_exercise_set(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM exercise_set WHERE id = ?;
    """, (id,))

    # commit and close
    connection.commit()
    connection.close()
    
    # 200 = successful delete
    return jsonify({"message": "Exercise set deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
