import speech_recognition as sr
from banglaspeech2text import Speech2Text
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("groq_api_key"))

# stt = Speech2Text("base")

def predict_text(text):
  vec = vectorizer.transform([text])
  return model.predict(vec)[0]

def transcribe_audio(audio_file):
    with open(audio_file, "rb") as f:
        result = client.audio.transcriptions.create(
            file=f,
            model="whisper-large-v3",
            language="bn"
        )
    return result.text

df = pd.read_csv("datasets/bangla_intent_v3.csv")

X = df["utterance"]
y = df["intent"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)

vectorizer = TfidfVectorizer(
    analyzer='char',
    ngram_range=(3,5)
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    # output = stt.recognize(audio)

with open("recorded.wav", "wb") as f:
    f.write(audio.get_wav_data())

text = transcribe_audio("recorded.wav")
print(text)
print(predict_text(text))

# print(output)
# print(predict_text(output))

