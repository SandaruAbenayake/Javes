# JAVES

JAVES is a voice assistant that listens through the Mac microphone, sends each utterance to Gemini, remembers the current conversation, and speaks replies through the Mac speaker.

## Requirements

- macOS
- Python 3.10 or newer recommended
- Homebrew
- A Gemini API key

## Setup

```bash
brew install portaudio flac ffmpeg
python3 -m venv venv
./venv/bin/python -m pip install speechrecognition pyaudio pyttsx3 google-generativeai python-dotenv gtts pydub
```

Create `.env` in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Keep `.env` private. It is ignored by Git.

## Run

```bash
./venv/bin/python app.py
```

JAVES continuously listens after each response. Say `stop`, `goodbye`, or `exit` to hear the goodbye message and end the program. If speech is not understood, it returns to listening.

The normal runtime flow is:

```text
microphone -> speech-to-text -> Gemini -> terminal output -> Mac speaker
```

## Conversation Memory

Gemini memory is kept in-process by the module-level chat session in `ai/assistant.py`. The first request creates a Gemini chat with `history=[]`; later requests use the same session, so Gemini can refer to earlier turns in the current run.

Memory is temporary. It disappears when the program exits or restarts. JAVES does not yet store conversation history in a file or database.

## Robot Voice Samples

The independent robot voice generator is in `voice/robot_voice.py`. The current Captain Price sample is:

```bash
afplay audio/captain_price.wav
```

To generate another robotic WAV:

```python
from voice.robot_voice import generate_robot_voice

generate_robot_voice("Hello, I am Captain Price", "audio/captain_price.wav")
```
