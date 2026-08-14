import { useEffect, useState } from 'react'

function App() {
  // follows format of currentValue, wayToChangeIt, useState(initialValue)
  const [exercises, setExercises] = useState([])
  const [name, setName] = useState('')
  const [muscleGroup, setMuscleGroup] = useState('')

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/exercises')
      .then(response => response.json())
      .then(data => setExercises(data))
  }, [])

  // function to add exercise and muscle group, uses our post function we defined in backend app.py
  // we use this because we want to send flask some new data, i.e. REACT -> FLASK
  const addExercise = () => {
  fetch('http://127.0.0.1:5000/api/exercises', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: name,
      muscle_group: muscleGroup,
    }),
  })
}

  return (
    <div>
      <h1>Workout Progression Tracker</h1>

      <h2>Exercises</h2>

       {/* inputs are controlled components, so their values come from state, 
       and the onChange handler updates that state whenever the user types. */}
      <div>
        <input
          type="text"
          placeholder="Exercise name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          type="text"
          placeholder="Muscle group"
          value={muscleGroup}
          onChange={(e) => setMuscleGroup(e.target.value)}
        />

        {/* button click for adding exercise */}
        <button onClick={addExercise}>Add Exercise</button>

      </div>

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