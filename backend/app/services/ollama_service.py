import os
from ollama import Client

MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

client = Client(host=OLLAMA_HOST)

def chat_with_model(messages: list[dict]) -> str:
    response = client.chat(
        model=MODEL,
        messages=messages
    )
    return response["message"]["content"]