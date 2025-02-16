from flask import Flask, request, jsonify
import openai
import requests
import os
from PIL import Image

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("api/identify", methods=["POST"])
def identify_animal():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image = request.files['image']
    
    # Convert image to bytes
    image_bytes = image.read()

    try:
        # Use OpenAI's Vision API
        response = openai.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "system", "content": "You are an expert in identifying animals."},
                {"role": "user", "content": [
                    {"type": "text", "text": "Identify the animal in this image."},
                    {"type": "image", "image": image_bytes}
                ]}
            ],
            max_tokens=50
        )

        # Extract the response
        animal_name = response["choices"][0]["message"]["content"]

        return jsonify({"animal": animal_name})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)