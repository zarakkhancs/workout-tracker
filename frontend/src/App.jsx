import { useEffect, useState } from 'react'

function App() {
  const [exercises, setExercises] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/exercises')
      .then(response => response.json())
      .then(data => setExercises(data))
  }, [])

  return (
    <div>
      <h1>Workout Progression Tracker</h1>

      <h2>Exercises</h2>

      {exercises.map(exercise => (
        <div key={exercise.id}>
          <h3>{exercise.name}</h3>
          <p>{exercise.muscle_group}</p>
        </div>
      ))}
    </div>
  )
}

export default App