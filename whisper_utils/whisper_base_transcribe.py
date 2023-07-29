import whisper
import pprint

model = whisper.load_model("base")
result = model.transcribe("../test_audios/input_audios/audio_1.mp3")
print(result["text"])
pprint.pprint(result)