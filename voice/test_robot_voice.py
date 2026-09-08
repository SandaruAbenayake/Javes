"""Test the generated robot voice."""

import os

from robot_voice import generate_robot_voice


output_path = "audio/test_robot.wav"
generate_robot_voice("Hello, I am Javes", output_path)

if not os.path.isfile(output_path):
    raise RuntimeError(f"Expected audio file was not created: {output_path}")

print(f"Created {output_path}")
