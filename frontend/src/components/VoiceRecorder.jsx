import {useRef, useState} from 'react';

function VoiceRecorder({onRecordingComplete}){
    const [isRecording, setIsRecording] = useState(false);

    const mediaRecorderRef = useRef(null);
    const audioChunksRef = useRef([]);

    const startRecording = async () => {
        const stream = await navigator.mediaDevices.getUserMedia({
            audio: true,
        });

        const mediaRecorder = new MediaRecorder(stream);
    
        mediaRecorderRef.current = mediaRecorder;
        audioChunksRef.current = [];

        mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                audioChunksRef.current.push(event.data);
            }
        };

        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunksRef.current, {
                type: mediaRecorder.mimeType,
            });

            const audioFile = new File(
                [audioBlob],
                "recording.webm",
                { type: audioBlob.type }
            );

            onRecordingComplete(audioFile);

            stream.getTracks().forEach((track) => track.stop());
        };

        mediaRecorder.start();
        setIsRecording(true);
    };

    const stopRecording = () => {
        if (mediaRecorderRef.current){
            mediaRecorderRef.current.stop();
            setIsRecording(false);
        }
    };

    return (
        <div>
            { !isRecording ? (
                <button onClick={startRecording}>
                    Start Recording
                </button>
            ) : (
                <button onClick={stopRecording}>
                    Stop Recording 
                </button>
            )}
        </div>
    );
}

export default VoiceRecorder;