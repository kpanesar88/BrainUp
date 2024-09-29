from ..model_initialization import initialize
initialize()

from typing import List, Tuple

from sentence_transformers import SentenceTransformer

import torch

def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2", device=device)

    def eval(input_val: str) -> Tuple[str, List[float]]:
        embedding = []

        embedding = model.encode(input_val)

        return (input_val, embedding.tolist())
    return eval

if __name__ == "__main__":
    texts = ["Hello world 1", "good bye fucker", "AGA AGA"]

    model = load_model()

    for text in texts:
        print(model(text))