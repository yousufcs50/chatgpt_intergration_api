import openai
openai.api_key = 
file = open("recording.mp3", "rb")
transcription = openai.Audio.transcribe("whisper-1", file)

print(transcription)


