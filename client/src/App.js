import React, {useState, useEffect} from 'react'

import './App.css';

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('/api/data');
      const result = await response.json();
      setData(result);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="App">
      <h1>React App with Flask Backend</h1>
      <p>Data from Flask: {data.message}</p>
    </div>
  );
}


export default App
