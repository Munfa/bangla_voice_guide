from banglaspeech2text import Speech2Text

stt = Speech2Text("small")

transcription = stt.recognize("audio_samples/audio2.mp3")
print(transcription)