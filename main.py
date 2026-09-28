from backend.speech_to_text import process_audio, process_text

# sentence = "বিদ্যুৎ বিলটা নগদ দিয়া দিতে চাই"
# data_dict = process_text(sentence)

# print(data_dict)

audio_path = "audio_samples/audio2.mp3"
data_dict = process_audio(audio_path)
print(data_dict)