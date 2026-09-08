"""AI assistant functionality."""

import os
from typing import Optional

import google.generativeai as genai
from dotenv import load_dotenv

_chat_session = None


def _get_chat_session() -> Optional[object]:
	"""Create the shared Gemini chat session on its first use."""
	global _chat_session
	if _chat_session is not None:
		return _chat_session

	load_dotenv()
	api_key = os.getenv("GEMINI_API_KEY")
	if not api_key:
		return None

	try:
		genai.configure(api_key=api_key)
		for model_name in ("gemini-3.6-flash", "gemini-1.5-flash"):
			try:
				model = genai.GenerativeModel(model_name)
				_chat_session = model.start_chat(history=[])
				return _chat_session
			except Exception:
				continue
	except Exception:
		return None

	return None


def get_response(user_text: str) -> str:
	"""Return a response from the ongoing Gemini conversation."""
	chat_session = _get_chat_session()
	if chat_session is None:
		return "Sorry, I couldn't process that."

	try:
		response = chat_session.send_message(user_text)
		return response.text
	except Exception:
		return "Sorry, I couldn't process that."
