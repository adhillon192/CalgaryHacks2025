import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ImageUpload from "./components/ImageUpload.jsx";
import PredictionResult from "./components/PredictionResult.jsx";

function App() {

  const [prediction, setPrediction] = useState(null);
      return (
          <div className="max-w-xl mx-auto mt-10">
              <h1 className="text-2xl font-bold text-center">Wild Vision</h1>
              <ImageUpload onPrediction={setPrediction} />
              <PredictionResult result={prediction} />
          </div>
      );
  }
  
  export default App;
  
