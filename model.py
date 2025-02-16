from flask import Flask, request, jsonify
import openai
from openai import OpenAI
import requests
import os
import base64
from PIL import Image

from flask_cors import CORS


app = Flask(__name__)
client = OpenAI( api_key="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")
openai.api_key = "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"

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
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert in identifying animals."},
                {"role": "user", "content": "In exactly one word, identify the animal in this image. Image URL: data:image/jpeg;base64," + image_base64}
            ],
            max_tokens=300
        )

        # Extract the response
        animal_name = response.choices[0].message.content

        return jsonify({"animal": animal_name})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)