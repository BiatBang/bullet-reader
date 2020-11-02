from google.cloud import texttospeech
from pydub import AudioSegment
from pydub.playback import play
import io

def playaudio(text):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="zh-CN", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    song = AudioSegment.from_file(io.BytesIO(response.audio_content), format="mp3")
    print("playing ", text, "...")
    # pip install simpleaudio solves the problem:
    # PermissionError: [Errno 13] Permission denied: 'C:\\Users\\***\\AppData\\Local\\Temp\\tmpj5yymayl.wav'
    # how did they notice this?
    play(song)