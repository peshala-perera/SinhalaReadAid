from gtts import gTTS

def text_to_speech_sinhala(text, output_path="sinhala_audio.mp3"):
    tts = gTTS(text=text, lang='si')
    tts.save(output_path)
    return output_path
