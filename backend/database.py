import sqlite3
import os

def get_db_connection():
    # connect to the database file inside the backend folder
    database_path = os.path.join(os.path.dirname(__file__), 'workout.db')

    # connect to database file (create it if it's missing)
    connection = sqlite3.connect('workout.db')
    return connection


def create_tables():
    database_connection = get_db_connection()
    cursor = database_connection.cursor()

    # table for what exercise done (non-detailed)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exercise (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            muscle_group TEXT NOT NULL
        );
    """)


    # table for what workout_session we are on
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS workout_session (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL
            );
        """)


    # table to connect workout session and exercise
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS workout_exercise (
                    id INTEGER PRIMARY KEY,
                    exercise_id INTEGER NOT NULL,
                    workout_session_id INTEGER NOT NULL,
                    FOREIGN KEY (exercise_id) REFERENCES exercise(id),
                    FOREIGN KEY (workout_session_id) REFERENCES workout_session(id)
                );
            """)    


    # table for exercise set
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS exercise_set (
                        id INTEGER PRIMARY KEY,
                        workout_exercise_id INTEGER NOT NULL,
                        set_number INTEGER NOT NULL,
                        weight INTEGER NOT NULL,
                        reps INTEGER NOT NULL,
                        FOREIGN KEY (workout_exercise_id) REFERENCES workout_exercise(id)
                    );
                """)
    
    
    database_connection.commit()

    database_connection.close()

    print("Exercise, workout session, and workout exercise link tables created!")

if __name__ == "__main__":
    create_tables()