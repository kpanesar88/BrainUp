from pathlib import Path

from dotenv import load_dotenv
import os


def initialize():
    load_dotenv()
    MODEL_DIR: Path = Path(os.environ['MODEL_DIR'])
    os.environ['TRANSFORMERS_CACHE'] = f"{MODEL_DIR}"
    os.environ['HF_HOME'] = f"{MODEL_DIR}"