from banglaspeech2text import Speech2Text
import os
# from dotenv import load_dotenv
import json
import joblib
from text_to_speech import speak_steps

artifacts = joblib.load("joblibs/intent_model_and_vectorizer.joblib")
vectorizer = artifacts["vectorizer"]
intent_model = artifacts["model"]
app_model = joblib.load("joblibs/app_model.joblib")

stt = Speech2Text("small")

with open("steps_guide.json", encoding="utf-8") as f:
    guide = json.load(f)

def predict_app(text):
  vec = vectorizer.transform([text])
  app = app_model.predict(vec)[0]
  return app

def predict_intent(text):
  vec = vectorizer.transform([text])
  intent = intent_model.predict(vec)[0]
  return intent

def get_steps(app, intent):
    app_data = guide["apps"].get(app, {})
    intent_data = app_data.get(intent)
   
    if not intent_data:
        print("দুঃখিত, এই তথ্যের নির্দেশিকা খুঁজে পাওয়া যায়নি।")
        return
    
    steps = intent_data['steps']

    return steps 

def process_audio(audio_path):
    text = stt.recognize(audio_path)
    app = predict_app(text)
    intent = predict_intent(text)
    steps = get_steps(app, intent)

    return {
        "text": text,
        "app": app,
        "intent": intent,
        "steps": steps
    }

################# For Practice ################
def process_text(text):
    # text = stt.recognize(audio_path)
    app = predict_app(text)
    intent = predict_intent(text)
    steps = get_steps(app, intent)

    return {
        "text": text,
        "app": app,
        "intent": intent,
        "steps": steps
    }

# transcription = stt.recognize("audio2.mp3")
# print(transcription)
# sentence = stt.recognize("audio_samples/audio2.mp3")
# sentence = "বিদ্যুৎ বিলটা নগদ দিয়া দিতে চাই"
# print(sentence)
# intent, app = predict_text(sentence) #predict_text("বিক্ষাসক ই লাটে খাফাটা ইত্যাম।")
# print(f"intent: {intent}, app: {app}")

# speak_steps(app, intent)
