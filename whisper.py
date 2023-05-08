import openai
openai.api_key = "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"
file = open("recording.mp3", "rb")
transcription = openai.Audio.transcribe("whisper-1", file)

print(transcription)


