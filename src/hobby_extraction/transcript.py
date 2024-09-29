from ..model_initialization import initialize
initialize()

from typing import Callable

import torch
from transformers import pipeline

def load_model() -> Callable[[str], str]:
    whisper = pipeline("automatic-speech-recognition", "openai/whisper-small", device="cuda")

    def get_transcript(source: str) -> str:
        transcription = whisper(source)

        # maybe split based on sentences

        return transcription["text"]
    
    return get_transcript
    
if __name__ == "__main__":
    model = load_model()

    print(model("reels\\3879014472440780437.mp4"))
    