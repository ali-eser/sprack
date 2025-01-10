import { FormEvent, useState } from 'react'
import './App.css'
import get_sentiment from './services/textService';

function App() {
  const [textInput, setTextInput] = useState("");
  const [prevInput, setPrevInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const [label, setLabel] = useState(null);
  const [score, setScore] = useState(null);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    if (prevInput === textInput || textInput === "") {
      return
    }

    setIsLoading(true);

    const result = await get_sentiment(textInput);

    setTimeout(() => {
      setLabel(result.label);
      setScore(result.score);
      setIsLoading(false);
    }, 500);

    setPrevInput(textInput);
  }

  return (
    <>
      <h1>Språk</h1>
      <form onSubmit={handleSubmit}>
        <textarea className={`input-box ${isLoading ? "gradient-border" : "normal-border"}`}
          cols={120}
          rows={5}
          name="text"
          id="text"
          value={textInput}
          placeholder='Type or paste text here'
          onChange={(e) => setTextInput(e.target.value)}/>

          {isLoading && (
            <button type='submit'>Analyzing</button>
          )}
          {!isLoading && (
            <button type='submit'>Analyze</button>
          )}
      </form>
      {score && (
        <div>
          <h3>{label} with a score of {score}</h3>
        </div>
      )}

    </>
  )
}

export default App
