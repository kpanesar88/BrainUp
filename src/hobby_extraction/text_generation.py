from ..model_initialization import initialize
initialize()

import os

import torch

from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.quantization import quantize_dynamic

model = "mistralai/Mistral-7B-Instruct-v0.3"
access_token = os.environ['ACCESS_TOKEN']

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(model, token=access_token)
model = AutoModelForCausalLM.from_pretrained(model, token=access_token)
# model.half()

model.config.pad_token_id = model.config.eos_token_id
# model.half()

model.to(device)

prompt = """What are some hobbies that would recommend based on the following prompts:
- A man skate boarding down a hill.
- A women surfing in australia.

answer with 3 words without explanation:
"""

inputs = tokenizer(prompt, return_tensors="pt").to(device)

outputs = model.generate(**inputs, max_new_tokens=20)

answer = tokenizer.decode(outputs[0], skip_special_tokens=True)[len(prompt):].strip()

print(answer)

from gliner.model import GLiNER
ner_model = GLiNER.from_pretrained("urchade/gliner_base")

print(ner_model.predict_entities(answer, ["Hobbies"]))




