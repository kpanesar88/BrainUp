from ..model_initialization import initialize
initialize()

from typing import List
import os

import torch

from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.quantization import quantize_dynamic

from gliner.model import GLiNER

from functional import seq

access_token = os.environ['ACCESS_TOKEN']

def load_model():
    model_name = "mistralai/Mistral-7B-Instruct-v0.3"

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=access_token)
    model = AutoModelForCausalLM.from_pretrained(model_name, token=access_token)
    # model.half()

    model.config.pad_token_id = model.config.eos_token_id
    # model.half()

    model.to(device)

    ner_model = GLiNER.from_pretrained("urchade/gliner_base")

    def eval(examples: List[str]) -> List[str]:
        examples = ['- '+example for example in examples].join('\n')
        prompt = f"What are some hobbies that would recommend based on the following prompts:\n{examples}\nanswer with 3 words without explanation:\n"

        inputs = tokenizer(prompt, return_tensors="pt").to(device)

        outputs = model.generate(**inputs, max_new_tokens=20)

        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)[len(prompt):].strip()

        labels = ner_model.predict_entities(answer, ["Hobbies"])
        return (seq(labels)
            .map(lambda x: x["text"])
            .list()
        )

    return eval


if __name__ == "__main__":
    model = load_model()

    print(
        model([
            "A girl is snowboarding down a hill.",
            "A guy is longboarding down a hill",
            "A group skies across the mountain"
        ])
    )

