import json
from gtts import gTTS
import os

# Load JSON steps guide
with open("steps_guide.json", encoding="utf-8") as f:
    guide = json.load(f)

def speak_steps(app, intent):
    app_data = guide["apps"].get(app, {})
    intent_data = app_data.get(intent)

    if not intent_data:
        print("দুঃখিত, এই তথ্যের নির্দেশিকা খুঁজে পাওয়া যায়নি।")
        return

    print(f"\n--------{intent_data['title']}--------")

    for idx, step in enumerate(intent_data['steps'], 1):
        full_text = f"ধাপ {idx}. {step}"
        print(full_text)

        tts = gTTS(full_text, lang="bn", slow=True)
        tts.save(f"step_{idx}.mp3")