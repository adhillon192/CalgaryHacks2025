from flask import Flask, request, jsonify
import openai
from openai import OpenAI
import requests
import os
import base64
from PIL import Image
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
client = OpenAI( api_key=os.getenv("OPENAI_API_KEY"))

CORS(app)

@app.route("/api/identify", methods=["POST"])
def identify_animal():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image = request.files['image']
    
    # Convert image to bytes
    image_base64 = base64.b64encode(image.read()).decode('utf-8')
    # image_bytes = image.read()

    try:
        # Use OpenAI's Vision API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "In just one word, tell me what species of animal is in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}",
                    },
                },
            ],
        }
    ],
            max_tokens=300
        )

        # Extract the response
        animal_name = response.choices[0].message.content
        
            
        return jsonify({"animal": animal_name, "stat": animal_stat(animal_name)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def animal_stat(animal_name):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"for the animal {animal_name}, just list the species statistics. the statistics I am looking for include scientific name, conservation status, population, and how climate change is affecting their species"}],
            max_tokens=300        
        )
        statistics = response.choices[0].message.content
        print(statistics)
        return statistics

    except Exception as e:
        return jsonify({"error": str(e)}), 500   

if __name__ == '__main__':
    app.run(debug=True)