from vosk import Model, KaldiRecognizer
import pyaudio
import playsound
import json
from gtts import gTTS
import os

devmode = True
target = "Alita"

# Load light model in devmode for faster loading
modelName = "models/vosk-model-fr-0.22"
if devmode:
    modelName = "models/vosk-model-small-fr-pguyot-0.3"
    target = "Pauline"

# Load model
model = Model(modelName)
recognizer = KaldiRecognizer(model, 16000)
print(target, " est prêt(e)")

# Microphone stream config
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=16384)
stream.start_stream()
print(target, " écoute")

# Listen to microphone in continuous loop
while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = json.loads(recognizer.Result())["text"]
        
        # Ignore empty text
        if(text == ""):
            continue

        # Show text detected
        print(text)

        # If text starts with target name
        if text.split()[0].lower() == target.lower():

            print(target, "a entendu")

            # Play sound to confirm that target heard
            playsound.playsound("sounds/okay.mp3", False)

            # Generate mp3 from text
            my_tts = text
            tts = gTTS(text=my_tts, lang='fr')
            tts.save("tmp/voice.mp3")

            # Play then remove mp3
            playsound.playsound("tmp/voice.mp3", False)
            os.remove("tmp/voice.mp3")