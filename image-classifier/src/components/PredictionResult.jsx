const PredictionResult = ({ result }) => {
    if (!result) return null;

    return (
        <div className="mt-4 p-4 border rounded-lg shadow-md">
            <h2 className="text-lg font-bold">Prediction Result</h2>
            <p>Class: {result.class}</p>
            <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
        </div>
    );
};

export default PredictionResult;
