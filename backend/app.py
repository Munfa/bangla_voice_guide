from fastapi import FastAPI, UploadFile, File
from speech_to_text import process_audio, process_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins= ["http://localhost:5173"],
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"]
)

# @app.post("/transcribe")
# def transcribe(audio_path: str):
#     text = process_audio(audio_path)
#     return text

@app.post("/transcribe")
def transcribe(audio: UploadFile = File(...)):
    audio_path = f"{audio.filename}"
    with open(audio_path, "wb") as f:
        f.write(audio.file.read())
    
    data_dict = process_audio(audio_path)
    return data_dict

@app.post("/predict")
def predict(text: str):
    data_dict = process_text(text)
    return data_dict

# @app.get("/guide/{app}/{intent}")
# def get_guide(app: str, intent:str):
#     steps = 