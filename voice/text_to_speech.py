"""Text-to-speech functionality."""

import pyttsx3


def speak(text: str) -> None:
	"""Speak the provided text through the Mac speaker."""
	engine = pyttsx3.init()
	engine.setProperty("rate", 175)
	engine.say(text)
	engine.runAndWait()
