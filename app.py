"""Application entry point."""

from ai.assistant import get_response
from voice.speech_to_text import listen
from voice.text_to_speech import speak


def main() -> None:
    """Start the JAVES assistant."""
    print("Captain Price assistant is ready.")
    while True:
        print("Listening...")
        text = listen()
        if text is None:
            continue

        print(f"You said: {text}")
        if text.strip().lower() in {"stop", "goodbye", "exit", "thank you"}:
            print("Goodbye!")
            speak("Goodbye!")
            break

        response = get_response(text)
        print(f"Captain Price: {response}")
        speak(response)


if __name__ == "__main__":
    main()
