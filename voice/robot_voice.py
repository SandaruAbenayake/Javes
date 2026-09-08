"""Generate robotic speech audio independent of macOS system voices."""

import os
import tempfile

from gtts import gTTS
from pydub import AudioSegment


def _shift_pitch(audio: AudioSegment, factor: float) -> AudioSegment:
    """Shift pitch by changing playback rate and restoring the sample rate."""
    shifted = audio._spawn(
        audio.raw_data,
        overrides={"frame_rate": int(audio.frame_rate * factor)},
    )
    return shifted.set_frame_rate(audio.frame_rate)


def generate_robot_voice(
    text: str,
    output_path: str,
    pitch_shift: float = -2,
    doubling_offset: float = 0.5,
    doubling_volume_db: float = -6,
) -> None:
    """Generate a pitch-shifted and doubled robotic WAV voice."""
    output_directory = os.path.dirname(output_path)
    if output_directory:
        os.makedirs(output_directory, exist_ok=True)

    temporary_mp3 = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    temporary_mp3.close()

    try:
        gTTS(text=text, lang="en").save(temporary_mp3.name)
        original = AudioSegment.from_mp3(temporary_mp3.name)
        primary_factor = 2 ** (pitch_shift / 12)
        duplicate_factor = 2 ** ((pitch_shift + doubling_offset) / 12)
        primary = _shift_pitch(original, primary_factor)
        duplicate = _shift_pitch(original, duplicate_factor).apply_gain(
            doubling_volume_db
        )
        robotic_audio = primary.overlay(duplicate)
        robotic_audio.export(output_path, format="wav")
    finally:
        os.remove(temporary_mp3.name)
