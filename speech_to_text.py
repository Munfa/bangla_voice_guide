# import torch
# from transformers import pipeline

# pipe = pipeline(
#     "automatic-speech-recognition",
#     model = "openai/whisper-small",
#     device = -1 #CPU
# )

# from faster_whisper import WhisperModel

# model = WhisperModel("small", device="cpu", compute_type="int8")
# segments, info = model.transcribe("চটগইয় পয় চটগইয় মইয় মহজবন ও ইরফন সজজদ Chittagong Languages Irfan Sajjad.wav",
#                     language="bn")

# for seg in segments:
#     print(seg.text)

import speech_recognition as sr
from banglaspeech2text import Speech2Text

stt = Speech2Text("base")

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    output = stt.recognize(audio)

print(output)