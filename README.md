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
