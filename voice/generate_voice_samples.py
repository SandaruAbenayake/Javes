"""Generate robot voice variations for comparison."""

import os
import tempfile

from gtts import gTTS
from pydub import AudioSegment

from robot_voice import generate_robot_voice


TEXT = "Hello, I am Javes, your assistant"


def generate_natural_voice(output_path: str) -> None:
    """Generate a plain gTTS WAV without robotic processing."""
    temporary_mp3 = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    temporary_mp3.close()

    try:
        gTTS(text=TEXT, lang="en").save(temporary_mp3.name)
        AudioSegment.from_mp3(temporary_mp3.name).export(output_path, format="wav")
    finally:
        os.remove(temporary_mp3.name)


os.makedirs("audio", exist_ok=True)
generate_robot_voice(TEXT, "audio/sample_subtle.wav", pitch_shift=-1, doubling_volume_db=-12)
generate_robot_voice(TEXT, "audio/sample_medium.wav", pitch_shift=-2, doubling_volume_db=-6)
generate_robot_voice(TEXT, "audio/sample_heavy.wav", pitch_shift=-4, doubling_volume_db=-3)
generate_natural_voice("audio/sample_natural.wav")

for filename in (
    "audio/sample_subtle.wav",
    "audio/sample_medium.wav",
    "audio/sample_heavy.wav",
    "audio/sample_natural.wav",
):
    print(f"Created {filename}")