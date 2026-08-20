# 🏋️ Workout Overload Tracker

A full-stack workout tracking application designed to help users monitor exercise performance, track workout history, and apply progressive overload principles to improve strength and fitness over time.

## Overview

Workout Overload Tracker was built to solve a common challenge in strength training: consistently tracking performance and knowing when to increase training load.

The application allows users to:

- Create and manage exercises
- Log workout sessions
- Record sets, repetitions, and weights
- View workout history
- Track progression over time
- Receive progressive overload recommendations based on previous performance

---

## Tech Stack

### Frontend
- React
- Tailwind CSS

### Backend
- Python
- Flask

### Database
- SQLite

### API
- RESTful APIs

### Development Tools
- Git
- GitHub

---

## Features

### Exercise Management
Create, edit, and organize custom exercises.

### Workout Logging
Record and store workout sessions, including:

- Exercise name
- Number of sets
- Repetitions
- Weight lifted

### Workout History
Review previous workout performance and monitor long-term progression.

### Progressive Overload Recommendations
Analyze previous workout data and provide recommendations for increasing training stimulus through:

- Additional weight
- Additional repetitions
- Increased training volume

---

## System Architecture

```text
React Frontend
      │
      ▼
Flask REST API
      │
      ▼
SQLite Database
```

### Frontend

The React frontend provides a responsive user experience for workout tracking, exercise management, and progression monitoring.

### Backend

The Flask backend handles:

- API routing
- Data processing
- Business logic
- Progressive overload calculations
- Database interactions

### Database

SQLite stores:

- Exercises
- Workout sessions
- Sets and repetitions
- Historical performance records

---

## Project Structure

```text
workout-tracker/
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── pages/
│
├── backend/
│   ├── routes/
│   ├── models/
│   └── database/
│
└── README.md
```

---

## Database Relationships

The application uses a relational database to model workouts, exercises, and performance history.

### Example: Chest Day Workout

Suppose a user completes the following workout on August 20, 2026:

Chest Day
├── Bench Press
│   ├── Set 1: 135 × 8
│   ├── Set 2: 135 × 8
│   └── Set 3: 135 × 7
│
└── Incline Bench Press
    ├── Set 1: 95 × 10
    └── Set 2: 95 × 10

This data is represented using four tables:

### workout_session

Represents a single workout session.

| id | date |
|----|------|
| 1 | 2026-08-20 |

---

### exercise

Stores all available exercises that can be reused across workouts.

| id | name |
|----|------|
| 1 | Bench Press |
| 2 | Incline Bench Press |
| 3 | Squat |
| 4 | Deadlift |

---

### workout_exercise

Connects an exercise to a specific workout session.

| id | workout_session_id | exercise_id |
|----|-------------------|------------|
| 1 | 1 | 1 |
| 2 | 1 | 2 |

This means:

- Workout Session #1 contains Bench Press.
- Workout Session #1 contains Incline Bench Press.

---

### exercise_set

Stores the actual workout performance data.

| id | workout_exercise_id | set_number | weight | reps |
|----|--------------------|------------|--------|------|
| 1 | 1 | 1 | 135 | 8 |
| 2 | 1 | 2 | 135 | 8 |
| 3 | 1 | 3 | 135 | 7 |
| 4 | 2 | 1 | 95 | 10 |
| 5 | 2 | 2 | 95 | 10 |

---

### Relationship Diagram

```text
Workout Session
│
├── Workout Exercise (Bench Press)
│      ├── Set 1: 135 × 8
│      ├── Set 2: 135 × 8
│      └── Set 3: 135 × 7
│
└── Workout Exercise (Incline Bench Press)
       ├── Set 1: 95 × 10
       └── Set 2: 95 × 10

Exercise Library
├── Bench Press
├── Incline Bench Press
├── Squat
└── Deadlift
```

The `exercise` table acts as a reusable exercise library, while `workout_exercise` connects exercises to specific workout sessions. `exercise_set` stores the actual performance data used for workout history tracking and future progressive overload recommendations.

## Running Locally

### Prerequisites

- Node.js
- Python 3.x
- npm

### Backend Setup

```bash
cd backend

pip install -r requirements.txt

python app.py
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

The frontend should now be available locally and connected to your Flask backend.

---

## Future Improvements

### Authentication
- User registration
- Login system
- Personalized workout history

### Database Enhancements
- PostgreSQL migration
- Improved data indexing and performance

### Analytics Dashboard
- Training volume charts
- Strength progression analytics
- Personal record tracking

### Enhanced Recommendations
- Smarter overload recommendations
- Recovery considerations
- Fatigue tracking

### Cloud Deployment
- Public deployment
- Managed database
- CI/CD pipeline

---

## What I Learned

This project has helped me develop and strengthen my skills in:

- Full-stack web development
- REST API design
- Relational database design
- CRUD 
