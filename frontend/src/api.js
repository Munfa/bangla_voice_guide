

const API_URL = "http://127.0.0.1:8000";

export async function processAudio(audioFile) {
    const formData = new FormData();
    formData.append("audio", audioFile);

    const response = await fetch(`${API_URL}/transcribe`,{
        method : "POST",
        body : formData,
    });

    if (!response.ok){
        throw new Error(`FastAPI Error: ${response.status}`);
    }

    return await response.json();
}