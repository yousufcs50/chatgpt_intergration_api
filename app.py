# from flask import Flask, abort, request
# import whisper
# from tempfile import NamedTemporaryFile

# # Load the Whisper model:
# model = whisper.load_model('base')

# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def handler():
#     if not request.files:
#         # If the user didn't submit any files, return a 400 (Bad Request) error.
#         abort(400)

#     # For each file, let's store the results in a list of dictionaries.
#     results = []

#     # Loop over every file that the user submitted.
#     for filename, handle in request.files.items():
#         # Create a temporary file.
#         # The location of the temporary file is available in `temp.name`.
#         temp = NamedTemporaryFile()
#         # Write the user's uploaded file to the temporary file.
#         # The file will get deleted when it drops out of scope.
#         handle.save(temp)
#         # Let's get the transcript of the temporary file.
#         result = model.transcribe(temp.name)
#         # Now we can store the result object for this file.
#         results.append({
#             'filename': filename,
#             'transcript': result['text'],
#         })

#     # This will be automatically converted to JSON.
#     return {'results': results}
from flask import Flask, request,jsonify 
import openai
import json
import os
from dotenv import load_dotenv

# Load the API key from the environment or .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up the OpenAI API key
openai.api_key = api_key

# Initialize the Flask app
app = Flask(__name__)

# Define the API endpoint for ChatGPT
def generate_answer(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.7,
              messages=[
        {"role": "system", "content": "You are a pet care assistant."},
        {"role": "user", "content": prompt}
    ]
        )
        answer = response.choices[0].message.content
#         sample answer:
#         {
#     "answer": "As an AI language model, I don't have emotions like humans, but I'm functioning properly. Thank you for asking. How can I assist you today?"
# }
#         return answer
    except Exception as e:
        print(f"Error generating answer: {e}")
        return None

@app.route('/v1/chat', methods=['POST'])
def api_generate_answer():
    if request.is_json:
        data = request.get_json()
        prompt = data.get('prompt', None)

        if prompt is not None:
            answer = generate_answer(prompt)
            return jsonify({"answer": answer})
        else:
            return jsonify({"error": "Missing prompt in JSON request"}), 400
    else:
        return jsonify({"error": "Request must be in JSON format"}), 400

if __name__ == "__main__":
    app.run()
