import openai
import os
from dotenv import load_dotenv

# Load the API key from the environment or .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
file = open("recording.mp3", "rb")
transcription = openai.Audio.transcribe("whisper-1", file)

print(transcription)


