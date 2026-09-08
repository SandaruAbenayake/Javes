"""Speech-to-text functionality."""

import speech_recognition as sr
from typing import Optional


def listen() -> Optional[str]:
	"""Listen through the microphone and return the recognized speech."""
	recognizer = sr.Recognizer()

	with sr.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		return recognizer.recognize_google(audio)
	except sr.UnknownValueError:
		print("Sorry, I could not understand what you said.")
	except sr.RequestError:
		print("Sorry, I could not reach the speech recognition service.")

	return None
