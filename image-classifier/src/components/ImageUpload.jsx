import { useState } from "react";

const ImageUpload = ({ onPrediction }) => {
    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(null);

    const handleImageChange = (event) => {
      /*  const file = event.target.files[0];
        if (file) {
            setImage(file);
            setPreview(URL.createObjectURL(file));
        }
        */
        const file = event.target.files[0];
        if (!file) return;
    
        const img = new Image();
        img.src = URL.createObjectURL(file);
        
        img.onload = () => {
            const maxWidth = 1024;  // Set your max width (e.g., 1024px)
            const maxHeight = 1024; // Set your max height (e.g., 1024px)
    
            if (img.width > maxWidth || img.height > maxHeight) {
                alert(`Image resolution too high! Max allowed: ${maxWidth}x${maxHeight}px`);
                return;
            }
    
            setImage(file);
            setPreview(img.src);
        };
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
            
            <button onClick={handleUpload} className="mt-2 px-4 py-2 bg-blue-500 text-white rounded">
                Classify Image
            </button>
        <br />  
        <br />  
        <br />  
            {preview && (
            <div className="mt-4">
                <img src={preview} alt="Preview" className="w-40 h-40 object-cover mx-auto" />
            </div>
        )}
         <br />  
         <br />  
         <br />  
        </div>
    );
}

export default ImageUpload;
