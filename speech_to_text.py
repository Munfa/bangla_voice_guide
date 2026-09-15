from banglaspeech2text import Speech2Text
import os
# from dotenv import load_dotenv
import joblib
from text_to_speech import speak_steps

artifacts = joblib.load("joblibs/intent_model_and_vectorizer.joblib")
vectorizer = artifacts["vectorizer"]
intent_model = artifacts["model"]
app_model = joblib.load("joblibs/app_model.joblib")

# stt = Speech2Text("small")

# transcription = stt.recognize("audio2.mp3")
# print(transcription)

def predict_text(text):
  vec = vectorizer.transform([text])
  intent = intent_model.predict(vec)[0]
  app = app_model.predict(vec)[0]
  return intent, app

# sentence = stt.recognize("audio_samples/audio2.mp3")
sentence = "বিদ্যুৎ বিলটা নগদ দিয়া দিতে চাই"
print(sentence)
intent, app = predict_text(sentence) #predict_text("বিক্ষাসক ই লাটে খাফাটা ইত্যাম।")
print(f"intent: {intent}, app: {app}")

speak_steps(app, intent)