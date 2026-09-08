"""List available text-to-speech voices."""

import pyttsx3


engine = pyttsx3.init()
for index, voice in enumerate(engine.getProperty("voices")):
    print(f"{index}: id={voice.id}, name={voice.name}")
