import { useState } from "react";

const ImageUpload = ({ onPrediction }) => {
    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(null);

    const handleImageChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setImage(file);
            setPreview(URL.createObjectURL(file));
        }
    };

    const handleUpload = async () => {
        if (!image) return;

       /* const formData = new FormData();
        formData.append("file", image);

        try {
            const response = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                body: formData,
            });
            const data = await response.json();
            onPrediction(data);
        } catch (error) {
            console.error("Error:", error);
        }
            */
        
            // Simulate API response
            setTimeout(() => {
                const mockResponse = {
                    class: "cat",
                    confidence: 0.92,
                };
                onPrediction(mockResponse);
            }, 1000); // Simulates a 1-second delay
    };

    return (
        <div className="p-4 border rounded-lg shadow-md text-center">
            <input type="file" onChange={handleImageChange} />
            {preview && <img src={preview} alt="Preview" className="mt-2 w-40 h-40 object-cover" />}
            <button onClick={handleUpload} className="mt-2 px-4 py-2 bg-blue-500 text-white rounded">
                Classify Image
            </button>
        </div>
    );
}

export default ImageUpload;
