import googletrans as gt
import os
import speech_recognition as sr

from googletrans import Translator
from gtts import gTTS # Google Text-to-Speech

# # Uncomment to list languages
# print(gt.LANGUAGES)
# print(f"number of lanugages: {len(gt.LANGUAGES)}")


# Configure audio
mic = sr.Microphone()
rec = sr.Recognizer()


# Capture audio
with mic as source:
    # Initialize the translator
    translator = Translator()

    # Define input and output languages
    input_lang = 'en'   # English
    output_lang = 'es'    # Spanish

    # Prompt for speech
    print("Talk now.")

    # Calibrate recording threshold
    rec.adjust_for_ambient_noise(source, duration=0.2)

    # Listen until there is silence
    audio = rec.listen(source)

# Detect words in audio clip
recorded_audio = rec.recognize_google(audio)
# Uncomment to debug
print(f"RECORDED: {recorded_audio}")


# # Detect the language
lang = translator.detect(recorded_audio)
print(f"LANG: {lang}")

# Translate the text
data = translator.translate(recorded_audio, src=input_lang, dest=output_lang)
text_translated = data.text
print(f"TRANSLATED: {text_translated}")

# Save and speak the text
speak = gTTS(text=text_translated, lang=output_lang, slow=False)
speak.save("translated_audio.mp3")
os.system("start translated_audio.mp3")