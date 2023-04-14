import whisper

model = whisper.load_model("small")
result = model.transcribe("WhatsApp Audio 2023-01-16 at 07.55.21.ogg")
print(result["text"])