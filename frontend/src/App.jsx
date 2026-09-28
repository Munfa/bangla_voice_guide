import { useState } from 'react'
import { processAudio } from './api'

function App() {
  const [audioFile, setAudioFile] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    setAudioFile(event.target.files[0]);
    setResult(null);
    setError("");
  };

  const handleSubmit = async () => {
    if(!audioFile){
      setError("Please select an audio file");
      return ;
    }

    try {
      setError("");
      setResult(null);

      const data = await processAudio(audioFile);
      setResult(data);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
      <div>
        <h1>Bangla Banking Assistant</h1>
        <input
          type = "file"
          accept='audio/*'
          onChange={handleFileChange}
        />

        <button onClick={handleSubmit}>
          Process Audio
        </button>
        
        {error && <p>{error}</p>}

        {result && (
          <div>
            <h2>Result</h2>

            <p>
              <strong>Text:</strong> {result.text}
            </p>

            <p>
              <strong>App:</strong> {result.app}
            </p>

            <p>
              <strong>Intent:</strong> {result.intent}
            </p>

            <h3>Steps</h3>
            <pre>
              {JSON.stringify(result.steps, null, 2)}
            </pre>
          </div>
        )}
      </div>
  );
}

export default App
